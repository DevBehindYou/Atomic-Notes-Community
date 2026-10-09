"""Figures for S2: 5 Best End to End Encrypted Notes Apps in 2026."""
from atomic_viz import figure, banner, box, phone

APPS = ["Atomic Notes", "Notesnook", "Standard Notes", "Cryptee", "Joplin"]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:13px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:19px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:35px;line-height:1">{a}</span></div>' for i, a in enumerate(APPS))
    art = box(740, 110, 400, 400, f'<div class="lbl" style="margin-bottom:8px">CHECKED OCTOBER 9, 2026</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("SECURITY · 2026", '5 BEST END TO END <span class="s">ENCRYPTED NOTES APPS</span>',
                              "Judged on one thing first: who holds the key.", art, title_size=88, text_width=640)

    y, n, o = '<span class="yes">ON</span>', '<span class="no">NONE</span>', '<span class="part">OPTIONAL</span>'
    data = [("ATOMIC NOTES", o, "AES-256-GCM", "Argon2id, 6 words", "Your phrase", n, "Source-available"),
            ("NOTESNOOK", y, "XChaCha20-Poly1305", "Argon2", "Recovery key", n, "GPL-3.0"),
            ("STANDARD NOTES", y, "XChaCha20-Poly1305", "Argon2id", "None", '<span class="yes">4 PUBLISHED</span>', "AGPL-3.0"),
            ("CRYPTEE", y, "AES-256", "Your encryption key", "None", n, "MIT (web client)"),
            ("JOPLIN", o, "AES-256-GCM", "PBKDF2", "None", n, "AGPL-3.0")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td><td>{g}</td></tr>" for a, b, c, d, e, f, g in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>DEFAULT</th><th>CIPHER</th>'
            f'<th>KEY FROM</th><th>RECOVERY</th><th>AUDITS</th><th>CODE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-comparison"] = figure("FIG 2 · AT A GLANCE", 'FIVE APPS, <span class="s">SIDE BY SIDE</span>', body,
                                  "From each app's security documentation, checked October 9, 2026.", h=760)

    # Five meanings of encrypted.
    rungs = [("HTTPS ONLY", "Locked on the network", "The company, on arrival"),
             ("ENCRYPTED SERVER DISKS", "Locked on the company's drives", "The company, any time"),
             ("ENCRYPTED PHONE STORAGE", "Locked on your device", "The company, if it syncs plain text"),
             ("CLIENT-SIDE, COMPANY KEY", "Locked before upload", "The company, with its copy of the key"),
             ("END-TO-END", "Locked before upload, your key only", "Only your devices")]
    body = ""
    for i, (t, d, who) in enumerate(rungs):
        top = 196 + (4 - i) * 104
        w = 620 + i * 60
        cls = "signal" if i == 4 else ("" if i == 3 else "surface flat")
        body += box(56, top, w, 88, f'<div style="display:flex;justify-content:space-between;align-items:center;height:100%">'
                                    f'<div><div class="ttl" style="font-size:32px;margin-top:0">{t}</div><div class="txt" style="font-size:19px;margin-top:2px">{d}</div></div>'
                                    f'<div style="text-align:right;max-width:300px"><div class="lbl" style="font-size:16px">WHO CAN READ</div>'
                                    f'<div style="font-size:20px;margin-top:4px">{who}</div></div></div>', cls=cls, style="padding:10px 20px")
    out["03-key-ladder"] = figure("FIG 1 · THE LADDER", 'FIVE THINGS <span class="s">"ENCRYPTED" CAN MEAN</span>', body,
                                  "Only the top rung keeps the company out of your notes.", h=800)

    # Recovery.
    ok, part, lost = '<span class="yes">YES</span>', '<span class="part">PARTLY</span>', '<span class="no">LOST</span>'
    data = [("ATOMIC NOTES", part, ok, lost, "Six-word phrase"),
            ("NOTESNOOK", ok, ok, lost, "Recovery key"),
            ("STANDARD NOTES", lost, ok, lost, "Password only"),
            ("CRYPTEE", lost, ok, lost, "Encryption key only"),
            ("JOPLIN", part, ok, lost, "Master password only")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>FORGOT THE SECRET</th><th>LOST THE PHONE</th>'
            f'<th>LOST BOTH</th><th>WHAT SAVES YOU</th></tr></thead><tbody>{trs}</tbody></table>')
    out["04-recovery"] = figure("FIG 4 · RECOVERY", 'YOU LOST IT. <span class="s">NOW WHAT?</span>', body,
                                "Partly: a device that is already unlocked can still read or export your notes.", h=640)

    # Metadata.
    cols = [("EVERY APP HERE", ["Your account email", "When you sync", "How many items you store", "Rough size of each item"]),
            ("ATOMIC NOTES ALSO", ["Note type: text or checklist", "Pinned and deleted flags", "Created and updated times", "The Drive file ID"]),
            ("HIDDEN EVERYWHERE", ["Note titles", "Note text", "Checklist items", "Attachments, where supported"])]
    body = ""
    for i, (t, items) in enumerate(cols):
        li = "".join(f'<div style="padding:10px 0;border-top:1.5px solid {"rgba(255,255,255,.35)" if i == 2 else "#C6C6CB"};font-size:22px">{x}</div>' for x in items)
        body += box(56 + i * 370, 196, 340, 420, f'<div class="lbl">{"STILL VISIBLE" if i < 2 else "ENCRYPTED"}</div><div class="ttl" style="font-size:38px;margin-bottom:10px">{t}</div>{li}',
                    cls="signal" if i == 2 else "")
    out["05-metadata"] = figure("FIG 5 · METADATA", 'CONTENT HIDDEN. <span class="s">PATTERN VISIBLE.</span>', body,
                                "Every sync service needs some metadata. The honest ones name it.", h=700)

    body = phone(17, 64, 190, 260, crop=470, shadow="ink")
    facts = [("THE KEY", "Six random words, 60 bits, shown once"), ("KEY DERIVATION", "Argon2id, 64 MiB, 3 passes, on the phone"),
             ("CIPHER", "AES-256-GCM for every note"), ("SERVER KEEPS", "A verifier, never the key"),
             ("DEFAULT", "Off. You switch the vault on"), ("HONEST LIMITS", "No independent audit yet")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:230px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES VAULT</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 3 · OUR PICK, DISCLOSED", 'HOW THE <span class="s">VAULT WORKS</span>', body,
                                         "It's my app, so it goes first. The vault code is public in lib/security/.", h=760)
    return out
