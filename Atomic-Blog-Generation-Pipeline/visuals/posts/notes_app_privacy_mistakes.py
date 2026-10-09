"""Figures for P3: Notes App Security, 10 Privacy Mistakes to Fix in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

MISTAKES = ["Guessable screen lock", "No app lock", "Passwords in notes", "Recovery phrase in a synced note", "Forgotten share links",
            "Leaky previews", "Weak cloud account", "Loose exports", "Unchecked APKs", "Trusting \"encrypted\""]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:40px 1fr;gap:6px;padding:6px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:17px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-size:20px;line-height:1.2">{m}</span></div>' for i, m in enumerate(MISTAKES))
    art = box(740, 84, 400, 480, f'<div class="lbl" style="margin-bottom:6px">FIX EACH IN MINUTES</div>{rows}', cls="sigshadow", style="padding:16px 22px")
    out["01-banner"] = banner("PRIVACY · SECURITY · 2026", 'NOTES APP SECURITY: <span class="s">10 MISTAKES TO FIX</span>',
                              "Most leaks come from habits, not hacks. Here's the fix for each.", art, title_size=86, text_width=640)

    groups = [("LOCKS", "Who can open it", [(1, "Guessable screen lock"), (2, "No app lock"), (6, "Leaky previews")]),
              ("SECRETS", "What you keep in it", [(3, "Passwords in notes"), (4, "Recovery phrase in a synced note"), (5, "Forgotten share links")]),
              ("ACCOUNTS AND COPIES", "Where else it lives", [(7, "Weak cloud account"), (8, "Loose exports")]),
              ("INSTALLS AND CLAIMS", "What you trust", [(9, "Unchecked APKs"), (10, "Trusting \"encrypted\"")])]
    body = ""
    for i, (t, s, items) in enumerate(groups):
        x, yy = 56 + (i % 2) * 555, 196 + (i // 2) * 260
        li = "".join(f'<div style="display:grid;grid-template-columns:46px 1fr;padding:7px 0;border-top:1.5px solid #C6C6CB">'
                     f'<span class="lbl" style="font-size:18px">{n:02d}</span><span style="font-size:22px">{m}</span></div>' for n, m in items)
        body += box(x, yy, 533, 236, f'<div class="lbl">{s}</div><div class="ttl" style="font-size:38px;margin-bottom:6px">{t}</div>{li}',
                    cls="sigshadow" if i == 0 else "", style="padding:16px 20px")
    out["02-mistakes-map"] = figure("FIG 1 · THE MAP", 'TEN MISTAKES, <span class="s">FOUR GROUPS</span>', body,
                                    "Most of them take under five minutes to fix.", h=760)

    homes = [("PASSWORDS", "A password manager", "Generates, fills, and warns about breaches.", "signal"),
             ("RECOVERY PHRASES", "Paper, stored offline", "Never in anything that syncs or backs up.", ""),
             ("ID AND BANK NUMBERS", "An encrypted vault", "Only if you need them on the phone at all.", ""),
             ("EVERYDAY NOTES", "Your notes app", "Lists, ideas, drafts. The job it's built for.", "surface flat")]
    body = ""
    for i, (what, home, d, cls) in enumerate(homes):
        x, yy = 56 + (i % 2) * 555, 196 + (i // 2) * 236
        body += box(x, yy, 533, 210, f'<div class="lbl">{what}</div><div class="ttl" style="font-size:42px">{home}</div><div class="txt">{d}</div>', cls=cls)
    out["03-where-secrets-belong"] = figure("FIG 3 · WHERE SECRETS BELONG", 'EVERY SECRET HAS <span class="s">A BETTER HOME</span>', body,
                                            "An ordinary note is the worst place for the first three.", h=740)

    layers = [("SCREEN LOCK", "Stops a stranger with your phone", "The phone"),
              ("APP LOCK", "Stops a friend holding your unlocked phone", "The notes app"),
              ("END-TO-END VAULT", "Stops the company and a breached server", "The synced copy"),
              ("CLOUD ACCOUNT 2-STEP", "Stops someone with your leaked password", "The account")]
    body = ""
    for i, (t, d, guards) in enumerate(layers):
        top = 196 + i * 116
        body += box(56 + i * 40, top, 900 - i * 40, 96, f'<div style="display:flex;justify-content:space-between;align-items:center;height:100%">'
                                                       f'<div><div class="ttl" style="font-size:34px;margin-top:0">{i + 1:02d} · {t}</div><div class="txt" style="font-size:20px;margin-top:2px">{d}</div></div>'
                                                       f'<div style="text-align:right"><div class="lbl" style="font-size:16px">GUARDS</div><div style="font-size:21px">{guards}</div></div></div>',
                    cls="signal" if i == 2 else ("" if i else "surface flat"), style="padding:10px 22px")
    out["04-lock-layers"] = figure("FIG 2 · LAYERS", 'FOUR LOCKS, <span class="s">FOUR THREATS</span>', body,
                                   "Atomic Notes covers layers 2 and 3 in the app. Layers 1 and 4 are your phone and your Google account.", h=770)

    steps = [("01", "OFFICIAL SOURCE ONLY", "The developer's release page or an app store. Never a mirror or a chat link."),
             ("02", "COMPARE SHA-256", "The file's fingerprint must match the one in the release notes."),
             ("03", "CHECK THE CERTIFICATE", "apksigner verify --print-certs shows who signed it.")]
    body = ""
    for i, (num, t, d) in enumerate(steps):
        body += box(56 + i * 370, 210, 340, 340, f'<div class="num">{num}</div><div class="ttl" style="font-size:38px">{t}</div><div class="txt muted">{d}</div>',
                    cls="sigshadow" if i == 1 else "")
    lines = arrow(400, 380, 422, 380, color="ink") + arrow(770, 380, 792, 380, color="ink")
    out["05-apk-check"] = figure("FIG 4 · BEFORE YOU INSTALL", 'THREE CHECKS <span class="s">FOR ANY APK</span>', body,
                                 "Atomic Notes 2.03.5 lists its checksums and certificate in its GitHub release notes.", lines=lines, h=640)

    routine = [("LOCKS", "Screen lock, app lock, and no-screenshots still on"), ("SHARES", "Revoke links you no longer need"),
               ("EXPORTS", "Delete or encrypt stray copies"), ("ACCOUNT", "Unique password and two-step verification"),
               ("UPDATES", "Read release notes for new sharing or AI features")]
    body = phone(9, 64, 190, 260, crop=470, shadow="ink")
    rws = "".join(f'<div style="display:grid;grid-template-columns:44px 170px 1fr;gap:10px;padding:12px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{i + 1:02d}</span><span class="lbl" style="font-size:18px;color:#15171B">{a}</span><span style="font-size:22px">{b}</span></div>'
                  for i, (a, b) in enumerate(routine))
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">EVERY THREE MONTHS</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-routine"] = figure("FIG 5 · THE ROUTINE", 'TEN MINUTES, <span class="s">FOUR TIMES A YEAR</span>', body,
                               "Shown: the Atomic Notes security screen, with biometric unlock armed.", h=760)
    return out
