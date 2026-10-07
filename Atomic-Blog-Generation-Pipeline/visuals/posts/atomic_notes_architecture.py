"""Figures for L5: Local First Architecture: 4 Layers Behind Atomic Notes."""
from atomic_viz import figure, banner, box, phone, arrow

LAYERS = [("01 · DEVICE", "THE REAL COPY", "Flutter app, Hive CE storage. Every note saves here first."),
          ("02 · SYNC SERVER", "THE COORDINATOR", "Hono on Vercel, MongoDB Atlas. Metadata, versions, energy."),
          ("03 · YOUR DRIVE", "THE CLOUD COPY", "One .atomic file per note, in a folder you own."),
          ("04 · VAULT", "THE OPTIONAL LOCK", "Argon2id + AES-256-GCM on the device. Off by default.")]


def build():
    out = {}

    art = ""
    for i, (l, t, _) in enumerate(LAYERS):
        cls = "signal sigshadow" if i == 0 else ("ink" if i == 3 else "")
        art += box(700 + i * 22, 96 + i * 118, 420, 100, f'<div class="lbl">{l}</div><div class="ttl" style="font-size:36px;margin-top:4px">{t}</div>',
                   cls=cls, style="padding:12px 20px")
    out["01-banner"] = banner("ARCHITECTURE · ATOMIC NOTES", 'LOCAL FIRST <span class="s">ARCHITECTURE</span>',
                              "Four layers behind Atomic Notes, and what each one can and can't see.", art, title_size=104, text_width=600)

    body = ""
    for i, (l, t, d) in enumerate(LAYERS[:3]):
        y = 196 + i * 162
        cls = "signal sigshadow" if i == 0 else ("surface" if i == 1 else "")
        body += box(56, y, 800, 136, f'<div class="lbl">{l}</div><div class="ttl" style="font-size:40px;margin-top:4px">{t}</div><div class="txt {"" if i == 0 else "muted"}" style="font-size:21px">{d}</div>',
                    cls=cls, style="padding:14px 22px")
    l, t, d = LAYERS[3]
    body += box(906, 196, 238, 460, f'<div class="lbl">{l}</div><div class="ttl" style="font-size:40px">{t}</div><div class="txt" style="font-size:21px;margin-top:12px">{d}</div>'
                                    '<div class="txt" style="font-size:20px;margin-top:14px;color:rgba(244,245,241,.7)">Wraps layers 2 and 3: they hold ciphertext once it is on.</div>', cls="ink")
    lines = arrow(456, 336, 456, 352, color="ink") + arrow(456, 498, 456, 514, color="ink")
    out["02-four-layers"] = figure("FIG 1 · THE STACK", 'FOUR LAYERS, <span class="s">ONE JOB EACH</span>', body, lines=lines, h=690)

    # Push and pull.
    body = phone(3, 64, 210, 230, crop=420, shadow="ink")
    body += box(420, 210, 330, 210, '<div class="lbl">SYNC SERVER</div><div class="ttl">LOCK · CHECK · CHARGE</div><div class="txt muted" style="font-size:20px">Per-user lock, base-version check, one transaction per push.</div>', cls="surface")
    body += box(870, 210, 274, 210, '<div class="lbl">GOOGLE DRIVE</div><div class="ttl">WRITE FILES</div><div class="txt muted" style="font-size:20px">8 writes in flight, with retry.</div>')
    body += box(420, 500, 724, 170, '<div class="lbl">PULL</div><div class="ttl">OTHER DEVICES CATCH UP</div><div class="txt muted" style="font-size:20px">They ask for changes since their last cursor, 10 files per page, and open each note on the device.</div>')
    body += ('<div style="position:absolute;left:308px;top:262px;font-family:Mono;font-size:16px;color:#3A2FF0;width:104px;text-align:center">PUSH +<br>REQUEST ID</div>'
             '<div style="position:absolute;left:760px;top:262px;font-family:Mono;font-size:17px;color:#3A2FF0;width:110px;text-align:center">.ATOMIC<br>FILES</div>')
    lines = (arrow(306, 320, 414, 320, color="sig") + arrow(756, 320, 864, 320, color="sig")
             + arrow(1006, 426, 1006, 494, color="ink", dash=True) + arrow(414, 585, 300, 585, color="ink", dash=True, curve=(330, 600)))
    out["03-push-and-pull"] = figure("FIG 2 · THE DATA FLOW", 'PUSH UP. <span class="s">PULL DOWN.</span>', body,
                                     "Measured in production: a 9-note push took 3.2 s, a 22-note push 6.8 s.", lines=lines, h=740)

    rows = [("YOUR PHONE", "Everything", "Everything, after unlock"),
            ("SYNC SERVER", "Metadata. Note text in transit only", "Metadata and ciphertext"),
            ("GOOGLE (YOUR DRIVE)", "Readable .atomic files", "Ciphertext files"),
            ("THE DEVELOPER", "Metadata in the database", "Metadata in the database"),
            ("ANYONE IN YOUR GOOGLE ACCOUNT", "Your notes", "Ciphertext they can't open")]
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td><td class=\"hl\">{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th style="width:380px">WHO</th><th>VAULT OFF</th>'
            f'<th class="hl">VAULT ON</th></tr></thead><tbody>{trs}</tbody></table>')
    out["04-who-sees-what"] = figure("FIG 3 · VISIBILITY", 'WHO SEES <span class="s">WHAT</span>', body,
                                     "The server never stores note titles or text, with the vault on or off.", h=700)

    rows = [("NO NETWORK", "Notes save locally. Sync waits and runs on reconnect."),
            ("TIMEOUT MID-PUSH", "The same request ID is resent. The server replays its answer, so nothing is charged or written twice."),
            ("TWO DEVICES EDIT ONE NOTE", "The stale edit is refused and kept as a conflict copy. Nothing is overwritten."),
            ("STALE DELETE", "A delete based on an old version is refused, so a newer edit survives."),
            ("DRIVE IS SLOW", "Writes retry. The note stays pending on the phone until confirmed."),
            ("PHONE IS LOST", "Synced notes are in your Drive. Sign in on a new phone to pull them back.")]
    trs = "".join(f"<tr><th>{a}</th><td class=\"hl\">{b}</td></tr>" for a, b in rows)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th style="width:380px">WHEN THIS HAPPENS</th>'
            f'<th class="hl">WHAT ATOMIC NOTES DOES</th></tr></thead><tbody>{trs}</tbody></table>')
    out["05-failure-modes"] = figure("FIG 4 · WHEN THINGS GO WRONG", 'DESIGNED FOR <span class="s">BAD DAYS</span>', body, h=800)

    stack = [("APP", "Flutter (Dart), flutter_bloc, Hive CE. Android 9 or newer."),
             ("SERVER", "Hono (TypeScript) on Vercel, Mumbai region."),
             ("DATABASE", "MongoDB Atlas. Metadata, sessions, energy ledger."),
             ("STORAGE", "Google Drive API with the drive.file scope only."),
             ("CRYPTO", "Argon2id (64 MiB, 3 passes) and AES-256-GCM, on the device."),
             ("WEBSITE", "Next.js 15. Cookieless page analytics, no ad pixels.")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:200px 1fr;gap:16px;align-items:baseline;padding:13px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:19px">{a}</span><span style="font-size:23px">{b}</span></div>' for a, b in stack)
    body = box(56, 196, 1088, 500, f'<div class="ttl big" style="margin-top:0">THE STACK, IN ONE CARD</div><div style="margin-top:12px">{rws}</div>', cls="sigshadow")
    out["06-the-stack"] = figure("FIG 5 · TECH STACK", 'WHAT IT\'S <span class="s">BUILT WITH</span>', body, h=760)
    return out
