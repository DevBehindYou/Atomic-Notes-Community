"""Figures for P1: 9 Privacy Red Flags to Check Before Trusting Any Notes App in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

FLAGS = [
    ("ACCOUNT FIRST", "No note until you sign up."),
    ("NO EXPORT", "No way out in an open format."),
    ("VAGUE ENCRYPTION", "\"Encrypted\", but who holds the key?"),
    ("GREEDY PERMISSIONS", "Contacts, location, call logs."),
    ("AD SDKS", "Ads need a profile of you."),
    ("TRACKERS", "Analytics that watch you write."),
    ("FORCED AI", "Your notes sent to a model."),
    ("LOCKED FORMAT", "Exports nothing else can open."),
    ("NO STORAGE ANSWER", "Can't say where notes live."),
]


def build():
    out = {}

    rows = "".join(
        f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:7px 0;border-top:1.5px solid #C6C6CB">'
        f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#BA1A1A">{i + 1:02d}</span>'
        f'<span style="font-family:Bebas;font-size:28px;line-height:1">{t}</span></div>'
        for i, (t, _) in enumerate(FLAGS))
    art = box(760, 84, 380, 494, f'<div class="lbl" style="margin-bottom:8px">CHECK BEFORE YOU TRUST</div>{rows}',
              cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner(
        "PRIVACY · CHECKLIST · 2026",
        '9 PRIVACY <span class="s">RED FLAGS</span>',
        "Nine signs a notes app knows, keeps, or shares more than it tells you.",
        art, title_size=100, text_width=640)

    # The nine flags at a glance.
    checks = ["Open the app before signing in.", "Look for Export in settings.", "Find who holds the key.",
              "Read the permission list.", "Scan the store page for ads.", "Run an Exodus Privacy scan.",
              "Look for an AI off switch.", "Open an export in a text editor.", "Ask: device, cloud, or both?"]
    body = ""
    for i, ((t, d), c) in enumerate(zip(FLAGS, checks)):
        col, row = i % 3, i // 3
        x, y = 56 + col * 370, 194 + row * 186
        body += box(x, y, 340, 158,
                    f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="num" style="font-size:46px;color:#BA1A1A">{i + 1:02d}</span>'
                    f'<span class="lbl" style="font-size:17px">CHECK</span></div>'
                    f'<div class="ttl" style="font-size:32px;margin-top:2px">{t}</div><div class="txt muted" style="font-size:20px;margin-top:4px">{c}</div>',
                    style="padding:12px 18px")
    out["02-nine-red-flags"] = figure("FIG 1 · THE CHECKLIST", 'NINE FLAGS. <span class="s">ONE MINUTE EACH.</span>', body,
                                      "One flag is a question. Three or more is a pattern.", h=790)

    # Where a note's text and data can travel.
    body = box(76, 330, 250, 150,
               '<div class="lbl">YOUR NOTE</div><div class="ttl big">ON YOUR PHONE</div>', cls="signal sigshadow")
    dests = [
        ("APP SERVER", "Plain text unless end-to-end encrypted.", 182),
        ("ANALYTICS SDK", "Screens, taps, sessions, device.", 300),
        ("AD NETWORK", "An interest profile for targeting.", 418),
        ("AI PROVIDER", "Note text sent for processing.", 536),
        ("BACKUPS", "Copies that outlive a delete.", 654),
    ]
    lines = ""
    for t, d, y in dests:
        body += box(640, y - 8, 504, 96,
                    f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="ttl" style="margin:0;font-size:34px">{t}</span>'
                    f'<span class="lbl" style="font-size:16px;color:#BA1A1A">CAN LEAK</span></div><div class="txt muted" style="font-size:20px;margin-top:2px">{d}</div>',
                    cls="flat", style="padding:12px 18px")
        lines += arrow(334, 405, 630, y + 40, color="err", dash=True, width=3)
    out["03-where-notes-travel"] = figure("FIG 2 · EXPOSURE MAP", 'WHERE A NOTE <span class="s">CAN TRAVEL</span>', body,
                                          "Nobody has to read a note for it to expose you. Each path is a flag on the checklist.", lines=lines, h=800)

    # Three layers of evidence, strongest on top.
    layers = [
        ("PUBLIC CODE + TRACKER SCAN", "Anyone can check the libraries an app ships and the trackers inside its APK.", "STRONGEST", "signal"),
        ("PRIVACY POLICY", "Legally binding, but often written in broad phrases like \"trusted partners\".", "BETTER", "surface"),
        ("STORE PRIVACY LABEL", "Self-declared. Google says developers alone are responsible for its accuracy.", "WEAKEST", ""),
    ]
    body = ""
    for i, (t, d, tag, cls) in enumerate(layers):
        y = 196 + i * 150
        body += box(170, y, 974, 124,
                    f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="ttl" style="margin:0;font-size:40px">{t}</span>'
                    f'<span class="chip {"" if cls == "signal" else "ghost"}" style="{"border-color:#fff;background:transparent;color:#fff" if cls == "signal" else ""}">{tag}</span></div>'
                    f'<div class="txt {"" if cls == "signal" else "muted"}" style="font-size:21px;margin-top:8px">{d}</div>',
                    cls=cls + (" sigshadow" if cls == "signal" else ""), style="padding:16px 22px")
    body += ('<div style="position:absolute;left:56px;top:190px;width:90px;text-align:center;font-family:Mono;font-size:18px;letter-spacing:1.4px;color:#3A2FF0">MORE<br>PROOF</div>'
             '<div style="position:absolute;left:56px;top:592px;width:90px;text-align:center;font-family:Mono;font-size:18px;letter-spacing:1.4px">LESS<br>PROOF</div>')
    lines = arrow(101, 584, 101, 250, color="sig", width=4)
    out["04-evidence-ladder"] = figure("FIG 3 · TRUST, BUT VERIFY", 'THREE LAYERS OF <span class="s">EVIDENCE</span>', body,
                                       "A label is a claim. A policy is a promise. Code and scans are evidence.", lines=lines, h=720)

    # Permissions a notes app needs, and ones it doesn't.
    perms = [
        ("INTERNET", "Sync and sign-in", "needed", "Requested"),
        ("ACCESS_NETWORK_STATE", "Knowing when to sync", "needed", "Requested"),
        ("USE_BIOMETRIC", "Fingerprint app lock", "needed", "Requested"),
        ("RECORD_AUDIO", "Only for voice notes", "maybe", "Not requested"),
        ("READ_CONTACTS", "Nothing a notes app needs", "no", "Not requested"),
        ("ACCESS_FINE_LOCATION", "Rarely justified", "no", "Not requested"),
        ("READ_PHONE_STATE", "Device identity", "no", "Not requested"),
    ]
    mark = {"needed": '<span class="yes">NEEDED</span>', "maybe": '<span class="part">DEPENDS</span>', "no": '<span class="no">RED FLAG</span>'}
    trs = "".join(f'<tr><td style="font-family:Mono;font-size:19px">{p}</td><td>{why}</td><td>{mark[k]}</td><td class="hl">{a}</td></tr>'
                  for p, why, k, a in perms)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th>ANDROID PERMISSION</th><th>WHAT IT IS FOR</th><th>VERDICT</th>'
            f'<th class="hl">ATOMIC NOTES</th></tr></thead><tbody>{trs}</tbody></table>')
    out["05-permissions-check"] = figure("FIG 4 · PERMISSIONS", 'WHAT A NOTES APP <span class="s">SHOULD ASK FOR</span>', body,
                                         "Atomic Notes 2.03.5 requests three permissions. Check any app in Settings, Apps, Permissions.", h=760)

    # Atomic Notes, checked against its own list.
    status = [("PARTIAL", "A Google account is required. Notes still save on the phone first."),
              ("PARTIAL", "No export button yet. Synced notes are readable JSON in your Drive."),
              ("CLEAR", "Optional vault with a key only you hold. Off by default."),
              ("CLEAR", "Three permissions: internet, network state, biometric lock."),
              ("CLEAR", "No ads and no ad SDKs."),
              ("CLEAR", "No analytics, crash, or tracker SDKs."),
              ("CLEAR", "No AI features."),
              ("CLEAR", "One JSON file per note."),
              ("CLEAR", "Phone first, then your own Google Drive.")]
    body = ""
    for i, ((t, _), (st, d)) in enumerate(zip(FLAGS, status)):
        col, row = i % 3, i // 3
        x, y = 56 + col * 370, 194 + row * 196
        clear = st == "CLEAR"
        body += box(x, y, 340, 170,
                    f'<div style="display:flex;justify-content:space-between;align-items:center"><span class="lbl" style="color:#4A4D55">{i + 1:02d} · {t}</span></div>'
                    f'<span class="chip {"on" if clear else ""}" style="margin-top:10px;{"" if clear else "border-color:#4A4D55;color:#4A4D55"}">{st}</span>'
                    f'<div class="txt" style="font-size:19px;margin-top:8px;line-height:1.3">{d}</div>',
                    cls="" if clear else "surface flat", style="padding:14px 18px")
    out["06-atomic-notes-scorecard"] = figure("FIG 5 · OUR OWN SCORE", 'ATOMIC NOTES, <span class="s">CHECKED HONESTLY</span>', body,
                                              "Seven clear, two partial. Email sign-in and an export button are on the roadmap.", h=830)
    return out
