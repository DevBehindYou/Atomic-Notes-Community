"""Figures for S3: Storing Passwords in Notes App, 5 Real Dangers."""
from atomic_viz import figure, banner, box, phone, arrow


def build():
    out = {}

    note = ("<div class=\"lbl\" style=\"margin-bottom:10px\">NOTE · LOGINS</div>"
            + "".join(f'<div style="font-family:Mono;font-size:19px;padding:7px 0;border-top:1.5px solid #C6C6CB">{a}</div>'
                      for a in ["email: ••••••••••", "bank: ••••••••", "wifi: ••••••••••", "phone carrier: •••••", "mother's maiden name: ••••", "netflix: same as bank"]))
    art = box(740, 110, 400, 400, note, cls="warn", style="padding:18px 22px")
    out["01-banner"] = banner("SECURITY · PASSWORDS", 'STORING PASSWORDS <span class="s">IN A NOTES APP</span>',
                              "Five real dangers of a note called logins, and how to move out in twenty minutes.", art, title_size=88, text_width=640)

    # Blast radius.
    body = box(56, 360, 240, 130, '<div class="lbl">ONE NOTE</div><div class="ttl" style="font-size:40px">"LOGINS"</div>', cls="warn")
    body += box(410, 360, 240, 130, '<div class="lbl">THE MASTER KEY</div><div class="ttl" style="font-size:40px">EMAIL</div>', cls="ink")
    targets = [("BANK", 200), ("SOCIAL", 330), ("CLOUD STORAGE", 460), ("SHOPPING", 590)]
    for t, y in targets:
        body += box(800, y - 10, 340, 96, f'<div class="lbl" style="font-size:16px">RESET BY EMAIL</div><div class="ttl" style="font-size:34px">{t}</div>', style="padding:12px 18px")
    lines = arrow(300, 425, 402, 425, color="err", width=4.5)
    for _, y in targets:
        lines += arrow(654, 425, 792, y + 38, color="err")
    out["02-blast-radius"] = figure("FIG 2 · THE BLAST RADIUS", 'ONE NOTE, <span class="s">EVERY ACCOUNT</span>', body,
                                    "Most accounts reset through your inbox. Whoever reads the email password can reach the rest.", lines=lines, h=740)

    y, n, p = '<span class="yes">YES</span>', '<span class="no">NO</span>', '<span class="part">SOMETIMES</span>'
    rows = [("Encrypts each stored secret", p, y), ("Fills only on the matching site", n, y), ("Warns about breached passwords", n, y),
            ("Generates strong passwords", n, y), ("Flags reused passwords", n, y), ("Separate master password", p, y),
            ("Hidden from normal search", n, y)]
    trs = "".join(f"<tr><td style=\"font-size:22px\">{a}</td><td>{b}</td><td class=\"hl\">{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>FEATURE</th><th style="width:260px">NOTES APP</th>'
            f'<th class="hl" style="width:300px">PASSWORD MANAGER</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-notes-vs-manager"] = figure("FIG 1 · TWO DIFFERENT TOOLS", 'A NOTE IS NOT <span class="s">A PASSWORD MANAGER</span>', body,
                                        "Sometimes: a few notes apps can lock or encrypt a note, but none adds the other features.", h=740)

    rows = [("GOOGLE KEEP", n, n, n, n), ("SAMSUNG NOTES", '<span class="yes">NOTE LOCK</span>', n, n, n),
            ("APPLE NOTES", '<span class="yes">NOTE LOCK</span>', '<span class="part">WITH ADP</span>', n, n),
            ("ATOMIC NOTES", '<span class="yes">APP LOCK</span>', '<span class="part">OPTIONAL VAULT</span>', n, n),
            ("PASSWORD MANAGER", y, y, y, y)]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>LOCK</th><th>E2E SYNC</th>'
            f'<th>BREACH ALERTS</th><th>SAFE AUTOFILL</th></tr></thead><tbody>{trs}</tbody></table>')
    out["04-apps-compared"] = figure("FIG 3 · POPULAR APPS", 'IS YOUR NOTES APP <span class="s">SAFE FOR PASSWORDS?</span>', body,
                                     "Checked October 9, 2026. ADP is Apple's Advanced Data Protection, off by default.", h=640)

    steps = [("01", "PICK A MANAGER", "Protect it with a long passphrase used nowhere else."),
             ("02", "EMAIL FIRST", "Move it and change it. Email resets everything."),
             ("03", "MONEY AND PHONE", "Bank, card, and phone carrier logins next."),
             ("04", "TWO-STEP ON", "Authenticator app or passkey on those accounts."),
             ("05", "DELETE THE NOTE", "Then empty the notes app's trash.")]
    body = ""
    for i, (num, t, d) in enumerate(steps):
        body += box(56 + i * 220, 220, 200, 320, f'<div class="num" style="font-size:52px">{num}</div><div class="ttl" style="font-size:32px">{t}</div><div class="txt muted" style="font-size:20px">{d}</div>',
                    cls="sigshadow" if i == 1 else "", style="padding:16px 16px")
    out["05-move-out"] = figure("FIG 4 · MOVING OUT", 'TWENTY MINUTES, <span class="s">IN THIS ORDER</span>', body,
                                "Highest blast radius first. A deleted note often stays in the trash for 30 days.", h=620)

    body = phone(12, 64, 190, 260, crop=470, shadow="ink")
    facts = [("GOOD FOR", "Journals, health notes, plans, drafts"), ("PROTECTION", "App lock and an optional end-to-end vault"),
             ("NO AUTOFILL", "Can't stop you pasting into a fake site"), ("NO BREACH ALERTS", "Won't tell you a password leaked"),
             ("NO GENERATOR", "Can't create unique passwords"), ("VERDICT", "Not a password manager. Use one.")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:230px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES, HONESTLY</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 5 · RIGHT TOOL, RIGHT JOB", 'MY APP IS <span class="s">NOT A PASSWORD MANAGER</span>', body,
                                         "I build Atomic Notes. I'd rather you used it for notes and a password manager for passwords.", h=760)
    return out
