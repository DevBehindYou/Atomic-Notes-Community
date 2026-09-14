import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { createServer } from 'node:net';
import { resolve } from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';
import test from 'node:test';

test('production routes preserve authentication and public content', { timeout: 90000 }, async (t) => {
  const reservation = createServer();
  reservation.listen(0, '127.0.0.1');
  await once(reservation, 'listening');
  const port = reservation.address().port;
  await new Promise((done) => reservation.close(done));

  const server = spawn(process.execPath, [
    resolve('node_modules/next/dist/bin/next'), 'start',
    '--hostname', '127.0.0.1', '--port', String(port),
  ], {
    windowsHide: true,
    env: {
      ...process.env,
      NODE_ENV: 'production',
      ADMIN_PASSWORD: 'test-first-key',
      ADMIN_PASSWORD_2: 'test-second-key',
      SESSION_SECRET: 'test-only-session-signing-secret',
      // Never contact a deployed backend from this smoke test.
      ATOMIC_SERVER_URL: '',
      ADMIN_API_KEY: '',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  let output = '';
  for (const stream of [server.stdout, server.stderr]) {
    stream.on('data', (chunk) => { output = (output + chunk).slice(-12000); });
  }
  const stopped = once(server, 'exit');
  t.after(async () => {
    if (server.exitCode === null && server.signalCode === null) server.kill();
    await stopped;
  });
  const base = `http://127.0.0.1:${port}`;
  const request = (path, options = {}) => fetch(base + path, {
    ...options, signal: AbortSignal.timeout(10000),
  });
  let ready = false;
  for (let attempt = 0; attempt < 120; attempt++) {
    if (server.exitCode !== null) throw new Error(output);
    try {
      ready = (await request('/api/controller/session')).ok;
      if (ready) break;
    } catch { /* Wait for the owned server to start. */ }
    await delay(250);
  }
  assert.ok(ready, `Production server did not become ready:\n${output}`);

  await t.test('every admin operation rejects an anonymous request', async () => {
    for (const [route, method] of [
      ['health', 'GET'], ['stats', 'GET'], ['user', 'GET'], ['energy', 'POST'],
      ['notifications', 'GET'], ['notifications', 'POST'],
      ['notifications', 'PATCH'], ['notifications', 'DELETE'],
    ]) {
      const response = await request(`/api/controller/${route}`, { method });
      assert.equal(response.status, 401, `${method} ${route}`);
    }
  });

  await t.test('both passwords are required and signed cookies resolve to booleans', async () => {
    assert.deepEqual(await (await request('/api/controller/session')).json(), { admin: false });
    const login = (body) => request('/api/controller/login', {
      method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body),
    });
    for (const body of [
      { password: 'test-first-key' },
      { password: 'wrong', password2: 'test-second-key' },
    ]) assert.equal((await login(body)).status, 401);
    const response = await login({ password: 'test-first-key', password2: 'test-second-key' });
    assert.equal(response.status, 200);
    const setCookie = response.headers.get('set-cookie');
    assert.match(setCookie, /HttpOnly/i);
    const headers = { cookie: setCookie.split(';')[0] };
    assert.deepEqual(await (await request('/api/controller/session', { headers })).json(), { admin: true });
    assert.equal((await request('/api/controller/health', { headers })).status, 200);
    assert.deepEqual(await (await request('/api/controller/session', {
      headers: { cookie: headers.cookie + 'tampered' },
    })).json(), { admin: false });
    const logout = await request('/api/controller/logout', { method: 'POST' });
    assert.equal(logout.status, 200);
    assert.match(logout.headers.get('set-cookie'), /Max-Age=0/i);
  });

  await t.test('static article, missing article and RSS feed remain available', async () => {
    const article = await request('/blog/atomic-notes-v1-18-2');
    assert.equal(article.status, 200);
    assert.match(await article.text(), /<title>[^<]*Atomic/i);
    assert.equal((await request('/blog/nonexistent-smoke-test-article')).status, 404);
    const feed = await request('/feed.xml');
    assert.equal(feed.status, 200);
    assert.match(await feed.text(), /<rss[\s>]/);
  });
});
