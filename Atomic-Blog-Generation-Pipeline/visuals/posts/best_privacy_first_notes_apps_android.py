"""Figures for P2: 7 Best Private Notes Apps for Android in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

APPS = ["Atomic Notes", "SilentNotes", "CypherLeaf", "NoteSR", "Quillpad", "Fossify Notes", "Notes (Privacy Friendly)"]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:9px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:19px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:31px;line-height:1">{a}</span></div>' for i, a in enumerate(APPS))
    art = box(740, 92, 400, 460, f'<div class="lbl" style="margin-bottom:8px">CHECKED OCTOBER 2026</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("PRIVACY · ANDROID · 2026", '7 BEST PRIVATE NOTES APPS <span class="s">FOR ANDROID</span>',
                              "No ads, no trackers, public source code. Picked for how they treat your notes.", art, title_size=88, text_width=640)

    y, n, p = '<span class="yes">YES</span>', '<span class="no">NO</span>', '<span class="part">OPTIONAL</span>'
    data = [("ATOMIC NOTES", "Phone + your Google Drive", p, y, "Google", "Source-available"),
            ("SILENTNOTES", "Phone + storage you pick", y, y, "None", "MPL-2.0"),
            ("CYPHERLEAF", "Phone only", "Locked notes", n, "None", "MIT"),
            ("NOTESR", "Phone only", y, n, "None", "MIT"),
            ("QUILLPAD", "Phone + your Nextcloud", n, y, "None", "GPL-3.0"),
            ("FOSSIFY NOTES", "Phone only", n, n, "None", "GPL-3.0"),
            ("PRIVACY FRIENDLY", "Phone only", n, n, "None", "GPL-3.0")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>" for a, b, c, d, e, f in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>WHERE NOTES LIVE</th><th>ENCRYPTED</th>'
            f'<th>SYNC</th><th>ACCOUNT</th><th>LICENSE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-comparison"] = figure("FIG 1 · AT A GLANCE", 'SEVEN APPS, <span class="s">SIDE BY SIDE</span>', body,
                                  "Checked against each app's repository or F-Droid listing on October 7, 2026.", h=790)

    rules = [("NO ADS", "No ad slots, no ad SDKs."), ("NO TRACKERS", "No analytics or tracking libraries."),
             ("PUBLIC CODE", "Source you can read and check."), ("ALIVE IN 2026", "Updated recently, not abandoned."),
             ("PRIVATE BY DEFAULT", "Notes stay on the phone unless you choose sync."), ("HONEST LIMITS", "Each pick's weak spot is named.")]
    body = ""
    for i, (t, d) in enumerate(rules):
        x, yy = 56 + (i % 3) * 370, 196 + (i // 3) * 236
        body += box(x, yy, 340, 206, f'<div class="num" style="font-size:48px">{i + 1:02d}</div><div class="ttl" style="font-size:36px">{t}</div>'
                                     f'<div class="txt muted" style="font-size:21px">{d}</div>', cls="sigshadow" if i == 0 else "", style="padding:16px 20px")
    out["03-how-we-picked"] = figure("FIG 2 · THE RULES", 'HOW THESE APPS <span class="s">MADE THE LIST</span>', body,
                                     "Popular apps with ads, trackers, or closed code were left out on purpose.", h=720)

    # Pick by need.
    q = lambda x, yy, t: box(x, yy, 300, 110, f'<div class="lbl">QUESTION</div><div class="ttl" style="font-size:34px;margin-top:4px">{t}</div>', cls="surface flat", style="padding:12px 18px")
    a = lambda x, yy, t, d: box(x, yy, 300, 120, f'<div class="ttl" style="font-size:32px;margin-top:0">{t}</div><div class="txt muted" style="font-size:19px">{d}</div>', style="padding:12px 18px")
    body = q(56, 220, "SYNC ACROSS DEVICES?")
    body += q(450, 150, "ENCRYPTED BY DEFAULT?") + q(450, 470, "STORE FILES TOO?")
    body += a(844, 100, "SILENTNOTES", "Always encrypted, your storage") + a(844, 250, "ATOMIC NOTES", "Your Google Drive, optional vault")
    body += a(844, 420, "NOTESR", "Encrypted notes and files") + a(844, 570, "FOSSIFY NOTES", "Fast, simple, widgets")
    body += ('<div style="position:absolute;left:376px;top:196px;font-family:Mono;font-size:17px;color:#3A2FF0">YES</div>'
             '<div style="position:absolute;left:376px;top:420px;font-family:Mono;font-size:17px;color:#4A4D55">NO</div>'
             '<div style="position:absolute;left:776px;top:130px;font-family:Mono;font-size:17px;color:#3A2FF0">YES</div>'
             '<div style="position:absolute;left:770px;top:262px;font-family:Mono;font-size:16px;color:#4A4D55">OPTIONAL</div>'
             '<div style="position:absolute;left:776px;top:452px;font-family:Mono;font-size:17px;color:#3A2FF0">YES</div>'
             '<div style="position:absolute;left:776px;top:602px;font-family:Mono;font-size:17px;color:#4A4D55">NO</div>')
    lines = (arrow(362, 260, 444, 210, color="sig") + arrow(362, 300, 444, 520, color="ink")
             + arrow(756, 190, 838, 160, color="sig") + arrow(756, 220, 838, 300, color="ink")
             + arrow(756, 510, 838, 480, color="sig") + arrow(756, 545, 838, 620, color="ink"))
    out["04-pick-by-need"] = figure("FIG 3 · QUICK PICK", 'WHICH ONE <span class="s">FITS YOU?</span>', body,
                                    "Quillpad suits Nextcloud users. CypherLeaf and Privacy Friendly Notes suit offline-only notebooks.", lines=lines, h=800)

    perms = [("ATOMIC NOTES", "Yes, for sync", "Biometric lock"),
             ("SILENTNOTES", "Yes, for sync", "Nearby Wi-Fi devices"),
             ("CYPHERLEAF", "No", "Notifications, biometric lock"),
             ("NOTESR", "No", "Storage, background sync"),
             ("QUILLPAD", "Yes, for Nextcloud", "Microphone for audio notes"),
             ("FOSSIFY NOTES", "No", "Storage, alarms, widgets"),
             ("PRIVACY FRIENDLY", "No", "Camera and microphone for media notes")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in perms)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th style="width:330px">APP</th><th style="width:300px">INTERNET</th>'
            f'<th>OTHER NOTABLE PERMISSIONS</th></tr></thead><tbody>{trs}</tbody></table>')
    out["05-permissions"] = figure("FIG 4 · PERMISSIONS", 'WHO CAN EVEN <span class="s">REACH THE INTERNET?</span>', body,
                                   "From each app's AndroidManifest.xml or F-Droid listing. No internet permission means notes can't leave by the app itself.", h=790)

    body = phone(12, 64, 190, 260, crop=470, shadow="ink")
    facts = [("WHERE NOTES LIVE", "Your phone first, then your own Google Drive"), ("ENCRYPTION", "Optional end-to-end vault, off by default"),
             ("SERVER", "Metadata only, never note titles or text"), ("NO", "Ads, trackers, or AI"),
             ("PRICE", "Free, 30 notes, daily sync energy"), ("HONEST LIMITS", "Google sign-in required. No export button yet")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:240px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 5 · OUR PICK, DISCLOSED", 'WHY ATOMIC NOTES <span class="s">IS FIRST</span>', body,
                                         "It's my app, so it goes first. Every fact on this card is checkable in its public code.", h=760)
    return out
