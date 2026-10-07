"""Figures for L3: Notes App Without Internet: Why Offline Should Be the Default."""
from atomic_viz import figure, banner, box, phone, arrow


def build():
    out = {}

    art = (phone(4, 830, 92, 290, crop=560)
           + box(660, 330, 330, 210,
                 '<div style="display:flex;gap:8px;flex-wrap:wrap"><span class="chip ink">AIRPLANE MODE · ON</span></div>'
                 '<div class="ttl" style="font-size:44px;margin-top:14px">NOTE SAVED</div>'
                 '<div class="lbl" style="margin-top:8px">0 MS · SYNCS LATER</div>',
                 cls="sigshadow", style="padding:18px 20px"))
    out["01-banner"] = banner("LOCAL FIRST · OFFLINE", 'NOTES THAT WORK <span class="s">WITHOUT INTERNET</span>',
                              "Signal drops all the time. Your notes app shouldn't care.", art, title_size=96, text_width=600)

    spots = [("SUBWAYS AND TRAINS", "Tunnels cut the signal between stations."),
             ("FLIGHTS", "Hours in airplane mode, often with time to think."),
             ("ELEVATORS AND BASEMENTS", "Concrete and steel block the signal."),
             ("RURAL ROADS", "Coverage maps are optimistic between towns."),
             ("CROWDED EVENTS", "Thousands of phones share one set of towers."),
             ("SECURE BUILDINGS", "Hospitals, labs, and offices that limit networks.")]
    body = ""
    for i, (t, d) in enumerate(spots):
        x, y = 56 + (i % 3) * 370, 196 + (i // 3) * 236
        body += box(x, y, 340, 206, f'<div class="num" style="font-size:48px">{i + 1:02d}</div><div class="ttl" style="font-size:34px">{t}</div>'
                                    f'<div class="txt muted" style="font-size:21px">{d}</div>', style="padding:16px 20px")
    out["02-where-signal-drops"] = figure("FIG 1 · REAL LIFE", 'WHERE NOTES <span class="s">LOSE SIGNAL</span>', body,
                                          "These are often the moments you most need to write something down.", h=720)

    yes, no, part = '<span class="yes">WORKS</span>', '<span class="no">FAILS</span>', '<span class="part">MAYBE</span>'
    rows = [("OPEN THE APP", part + " cached screen or spinner", yes + " from device storage"),
            ("READ A NOTE", part + " if it was cached", yes),
            ("WRITE A NEW NOTE", no + " or a fragile queue", yes + " saved on the device"),
            ("SEARCH", no + " search runs on a server", yes + " search runs on the phone"),
            ("DELETE OR EDIT", part, yes),
            ("SYNC", no + " until the network returns", part + " waits, then catches up")]
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td><td class=\"hl\">{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th style="width:300px">WITH NO INTERNET</th>'
            f'<th>CLOUD-FIRST APP</th><th class="hl">LOCAL-FIRST APP</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-offline-actions"] = figure("FIG 2 · THE DIFFERENCE", 'WHAT STILL WORKS <span class="s">OFFLINE?</span>', body,
                                       "Cloud-first apps vary. Many cache recent notes, but few treat offline as normal.", h=760)

    # A morning offline, then the catch-up.
    events = [("09:00", "SIGNAL LOST", "Train enters the tunnel.", "surface flat"),
              ("09:04", "3 EDITS", "Saved on the phone, marked to sync.", "signal flat"),
              ("09:18", "NEW NOTE", "Saved on the phone too.", "signal flat"),
              ("09:40", "SIGNAL BACK", "The app notices the network.", "surface flat"),
              ("09:40", "AUTO SYNC", "All 4 changes upload. Retries at 5, 15, then 45 s if needed.", "")]
    body = ""
    for i, (t, h, d, cls) in enumerate(events):
        x = 56 + i * 222
        body += box(x, 280, 198, 300, f'<div class="lbl">{t}</div><div class="ttl" style="font-size:34px">{h}</div><div class="txt {"" if "signal" in cls else "muted"}" style="font-size:20px">{d}</div>',
                    cls=cls + (" sigshadow" if cls == "" else ""), style="padding:16px 16px")
    body += ('<div style="position:absolute;left:56px;top:214px;width:640px;height:34px;border:2.5px dashed #BA1A1A;border-radius:6px;display:flex;align-items:center;'
             'justify-content:center;font-family:Mono;font-size:18px;letter-spacing:1.6px;color:#BA1A1A">NO NETWORK · 40 MINUTES</div>')
    lines = "".join(arrow(56 + i * 222 + 202, 430, 56 + (i + 1) * 222 - 6, 430, color="ink", width=3) for i in range(4))
    out["04-reconnect-timeline"] = figure("FIG 3 · A MORNING OFFLINE", 'WRITE NOW. <span class="s">SYNC LATER.</span>', body,
                                          "Nothing waited on the network. The network waited on nothing.", lines=lines, h=700)

    works = ["Write and edit notes", "Checklists", "Search every note", "Pin and delete", "Biometric app lock"]
    needs = ["First sign-in", "Sync to your Google Drive", "Atomic Energy and coins", "Notifications"]
    w = "".join(f'<div style="padding:10px 0;border-top:1.5px solid rgba(255,255,255,.3);font-size:23px">→ {x}</div>' for x in works)
    n = "".join(f'<div style="padding:10px 0;border-top:1.5px solid #C6C6CB;font-size:23px">{x}</div>' for x in needs)
    body = phone(3, 64, 196, 250, crop=460, shadow="ink")
    body += box(380, 196, 370, 470, f'<div class="lbl">WORKS OFFLINE</div><div class="ttl big">EVERYDAY NOTES</div><div style="margin-top:12px">{w}</div>', cls="signal sigshadow")
    body += box(800, 196, 344, 470, f'<div class="lbl" style="color:#4A4D55">NEEDS A NETWORK</div><div class="ttl big">THE CLOUD PARTS</div><div style="margin-top:12px">{n}</div>', cls="surface flat")
    out["05-atomic-notes-offline"] = figure("FIG 4 · ATOMIC NOTES", 'WHAT WORKS <span class="s">IN AIRPLANE MODE</span>', body,
                                            "Notes save to on-device Hive storage first. Only cloud features wait for a connection.", h=740)

    checks = ["Opens with no spinner", "New notes survive a restart", "Search runs offline", "Edits and deletes work", "Sync catches up alone", "Notes live in a place you control"]
    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr 36px;align-items:center;padding:12px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:19px;color:#3A2FF0">{i + 1:02d}</span><span style="font-size:24px">{c}</span>'
                   f'<span style="width:30px;height:30px;border:2.5px solid #15171B;border-radius:4px"></span></div>' for i, c in enumerate(checks))
    body = box(260, 186, 680, 500, f'<div class="lbl">SAVE THIS · OFFLINE READINESS</div><div class="ttl big">SIX CHECKS</div><div style="margin-top:10px">{rows}</div>', cls="sigshadow")
    out["06-offline-checklist"] = figure("FIG 5 · THE CHECKLIST", 'IS YOUR NOTES APP <span class="s">OFFLINE READY?</span>', body, h=740)
    return out
