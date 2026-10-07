"""Figures for P5: Notes App Metadata: 8 Things It Knows Without Reading Notes."""
import random
from atomic_viz import figure, banner, box

POINTS = [("EMAIL ADDRESS", "Ties every note to your real identity."),
          ("IP ADDRESS", "Your rough location, and when it changes."),
          ("DEVICE MODEL", "What you own, and when you switch phones."),
          ("OS AND APP VERSION", "How current, and how exposed, your phone is."),
          ("SIGN-IN TIMES", "When you start your day, and from where."),
          ("SYNC ACTIVITY", "When you write, and how much."),
          ("USAGE FREQUENCY", "How much the app matters to your routine."),
          ("NOTE COUNTS AND EDIT TIMES", "The shape of your thinking over time.")]


def build():
    out = {}

    log = "".join(f'<div style="padding:7px 0;border-top:1.5px solid #C6C6CB;font-family:Mono;font-size:18px">{x}</div>' for x in
                  ["23:52 · sync · 1 note · 2.1 KB", "23:47 · sync · 1 note · 2.4 KB", "09:12 · sign-in · new device", "14:03 · sync · 6 notes",
                   "00:21 · sync · 1 note · 3.6 KB", "11:40 · delete · 1 note"])
    art = box(700, 92, 440, 450, f'<div class="lbl">SERVER LOG · NO NOTE TEXT</div><div class="ttl" style="font-size:36px">STILL A STORY</div><div style="margin-top:10px">{log}</div>',
              cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("PRIVACY · WHAT APPS KNOW", 'NOTES APP <span class="s">METADATA</span>',
                              "8 things a notes app can know about you without reading a single note.", art, title_size=110, text_width=620)

    content = ["Note titles", "Note text", "Checklist items", "Attachments"]
    meta = ["Email address", "IP address", "Device model", "OS and app version", "Sign-in times", "Sync activity", "Usage frequency", "Note counts and edit times"]
    c = "".join(f'<div style="padding:9px 0;border-top:1.5px solid rgba(244,245,241,.2);font-size:23px">{x}</div>' for x in content)
    m = "".join(f'<div style="padding:8px 0;border-top:1.5px solid #C6C6CB;font-size:22px">{x}</div>' for x in meta)
    body = box(56, 196, 450, 500, f'<div class="lbl">CONTENT</div><div class="ttl big">WHAT YOU WROTE</div><div style="margin-top:12px">{c}</div>'
                                   '<div class="txt" style="font-size:20px;margin-top:16px;color:rgba(244,245,241,.75)">End-to-end encryption can hide this.</div>', cls="ink")
    body += box(566, 196, 578, 500, f'<div class="lbl" style="color:#BA1A1A">METADATA</div><div class="ttl big">EVERYTHING AROUND IT</div><div style="margin-top:10px">{m}</div>', cls="flat")
    out["02-content-vs-metadata"] = figure("FIG 1 · TWO KINDS OF DATA", 'CONTENT VS <span class="s">METADATA</span>', body,
                                           "Encryption protects the left box. Data minimization protects the right one.", h=760)

    body = ""
    for i, (t, d) in enumerate(POINTS):
        x, y = 56 + (i % 4) * 276, 196 + (i // 4) * 262
        body += box(x, y, 246, 230, f'<div class="num" style="font-size:48px">{i + 1:02d}</div><div class="ttl" style="font-size:31px">{t}</div>'
                                    f'<div class="txt muted" style="font-size:20px">{d}</div>', style="padding:14px 18px")
    out["03-eight-data-points"] = figure("FIG 2 · THE LIST", 'EIGHT THINGS <span class="s">IT CAN KNOW</span>', body,
                                         "None of these needs a single word of your notes.", h=760)

    # A week of sync timestamps as a heatmap.
    random.seed(7)
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    hits = {(d, h) for d in range(7) for h in (23,) if d < 5} | {(d, 0) for d in (1, 3, 4)} | {(2, 9), (3, 14), (3, 15), (5, 11), (6, 10), (0, 8), (4, 8)}
    grid = ""
    for d in range(7):
        grid += f'<div style="position:absolute;left:56px;top:{220 + d * 56}px;font-family:Mono;font-size:18px;letter-spacing:1.4px;line-height:44px">{days[d]}</div>'
        for h in range(24):
            on = (d, h) in hits
            grid += (f'<div style="position:absolute;left:{130 + h * 42}px;top:{220 + d * 56}px;width:36px;height:44px;border-radius:4px;'
                     f'background:{"#3A2FF0" if on else "#E2E3DD"};{"box-shadow:3px 3px 0 #15171B" if on else ""}"></div>')
    for h in (0, 6, 12, 18, 23):
        grid += f'<div style="position:absolute;left:{130 + h * 42}px;top:616px;font-family:Mono;font-size:17px;color:#4A4D55">{h:02d}:00</div>'
    grid += box(130, 660, 1010, 96, '<div class="txt" style="margin:0;font-size:22px"><b>What it suggests:</b> a long note almost every night near midnight, short bursts on Thursday afternoon, and quiet weekend mornings.</div>',
                cls="flat", style="padding:14px 20px")
    out["04-week-of-sync-times"] = figure("FIG 3 · ONE WEEK OF TIMESTAMPS", 'METADATA <span class="s">MAKES A PATTERN</span>', grid, h=800)

    yes, no, part = '<span class="yes">NEEDED</span>', '<span class="no">EXTRA</span>', '<span class="part">BRIEFLY</span>'
    rows = [("ACCOUNT EMAIL", yes, "To sign you in and own your notes"), ("IP ADDRESS", part, "Every request carries one. Keeping it is a choice"),
            ("DEVICE MODEL", part, "Useful for spotting a strange sign-in"), ("SYNC TIMES AND VERSIONS", yes, "To merge edits without losing any"),
            ("SCREEN AND TAP ANALYTICS", no, "Product dashboards, not your notes"), ("ADVERTISING ID", no, "Only needed to target ads"),
            ("LOCATION OR CONTACTS", no, "Nothing a notes app needs")]
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th style="width:360px">DATA</th><th style="width:170px">TO SYNC NOTES?</th>'
            f'<th>WHY</th></tr></thead><tbody>{trs}</tbody></table>')
    out["05-needed-vs-extra"] = figure("FIG 4 · DATA MINIMIZATION", 'NEEDED OR <span class="s">JUST COLLECTED?</span>', body,
                                       "A sync service needs a little metadata. Everything past that is a business choice.", h=780)

    keeps = [("ACCOUNT", "Email and display name from Google"), ("SESSIONS", "A SHA-256 hash of each token, the device's user agent, expiry"),
             ("NOTE METADATA", "IDs, kind, pinned, deleted, versions, Drive file IDs, a content hash, timestamps"),
             ("ENERGY LEDGER", "Energy and coin balance changes"), ("SECURITY LOG", "Sign-ins and sync events, deleted after 30 days")]
    never = ["Note titles or text", "Analytics or ad IDs", "Location or contacts", "Crash-reporting SDKs"]
    k = "".join(f'<div style="display:grid;grid-template-columns:230px 1fr;gap:14px;padding:10px 0;border-top:1.5px solid #C6C6CB">'
                f'<span style="font-family:Bebas;font-size:28px;line-height:1">{a}</span><span style="font-size:20px;line-height:1.3">{b}</span></div>' for a, b in keeps)
    nv = "".join(f'<div style="padding:10px 0;border-top:1.5px solid rgba(255,255,255,.3);font-size:22px">✕ {x}</div>' for x in never)
    body = box(56, 196, 700, 520, f'<div class="lbl">THE SERVER KEEPS</div><div class="ttl big">METADATA ONLY</div><div style="margin-top:10px">{k}</div>', cls="flat")
    body += box(804, 196, 340, 520, f'<div class="lbl">NEVER</div><div class="ttl big">NOT COLLECTED</div><div style="margin-top:10px">{nv}</div>', cls="signal sigshadow")
    out["06-what-atomic-notes-keeps"] = figure("FIG 5 · OUR OWN LIST", 'WHAT ATOMIC NOTES <span class="s">ACTUALLY KEEPS</span>', body,
                                               "The hosting provider sees IP addresses with each request, like every web service.", h=780)
    return out
