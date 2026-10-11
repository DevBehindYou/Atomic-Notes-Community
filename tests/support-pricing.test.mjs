// Run with: npm run test:pricing (Node 22+, using --experimental-strip-types).
import { test } from "node:test";
import assert from "node:assert/strict";
import {
  DEFAULT_CENTS,
  MEMBERSHIPS,
  PRESET_CENTS,
  REWARD_STEPS,
  formatUsd,
  quote,
  supportMessage,
} from "../src/lib/supportPricing.ts";

// The table from 03_COIN_PRICING_IMPLEMENTATION.md, confirmed by the owner on 2026-10-11.
const TABLE = { 100: 10, 200: 20, 300: 30, 400: 50, 500: 65, 600: 80, 700: 95, 800: 110, 900: 130, 1000: 150 };

test("every whole-dollar amount from $1 to $10 gives the exact table reward", () => {
  for (const [cents, coins] of Object.entries(TABLE)) assert.equal(quote(Number(cents)).coins, coins, `${cents} cents`);
});

test("bonus is measured against 10 coins per dollar", () => {
  assert.deepEqual(
    Object.keys(TABLE).map((c) => quote(Number(c)).bonusCoins),
    [0, 0, 0, 10, 15, 20, 25, 30, 40, 50],
  );
});

test("$2, $4 and $10 route to the Patreon memberships", () => {
  assert.deepEqual(
    [200, 400, 1000].map((c) => [quote(c).channel, quote(c).membership?.name]),
    [
      ["patreon", "Atomic Spark"],
      ["patreon", "Atomic Catalyst"],
      ["patreon", "Atomic Reactor"],
    ],
  );
});

test("every other amount routes to a one-time Ko-fi payment", () => {
  for (const cents of [100, 300, 500, 600, 700, 800, 900]) {
    const q = quote(cents);
    assert.equal(q.channel, "kofi");
    assert.equal(q.membership, null);
  }
});

test("membership rewards equal the table rewards for the same price", () => {
  for (const m of MEMBERSHIPS) assert.equal(m.coins, TABLE[m.cents], m.name);
});

test("amounts outside the table are rejected, never interpolated", () => {
  for (const cents of [0, 50, 150, 450, 1100, -100, 400.5, Number.NaN]) {
    assert.throws(() => quote(cents), /Unsupported/);
  }
});

test("the table covers every dollar from $1 to $10, in order", () => {
  assert.deepEqual(REWARD_STEPS.map((s) => s.cents), Object.keys(TABLE).map(Number));
});

test("presets are the three memberships, and the default is Catalyst", () => {
  assert.deepEqual(PRESET_CENTS, [200, 400, 1000]);
  assert.equal(quote(DEFAULT_CENTS).membership?.id, "catalyst");
});

test("the copied message names the route, amount, coins, and version", () => {
  assert.match(supportMessage(quote(700)), /\$7\.00 one-time support for 95 Atomic Coins, rewards 2026-10-11\.v2/);
  assert.match(supportMessage(quote(400)), /Atomic Catalyst membership \(\$4\.00 a month, 50 Atomic Coins each paid month\)/);
  assert.match(supportMessage(quote(100)), /account email: $/);
  assert.equal(formatUsd(1000), "$10.00");
});

test("copy never calls Atomic Notes open source", () => {
  assert.doesNotMatch(JSON.stringify(MEMBERSHIPS), /open[ -]source/i);
});
