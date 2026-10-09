"""Figures for L4: 8 Best Offline Notes Apps for Android in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

APPS = ["Atomic Notes", "Material Notes", "Open Notes", "sNotz", "Easy Notes", "Orgzly Revived", "Notes", "Butterfly"]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:7px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:29px;line-height:1">{a}</span></div>' for i, a in enumerate(APPS))
    art = box(740, 88, 400, 472, f'<div class="lbl" style="margin-bottom:6px">CHECKED OCTOBER 9, 2026</div>{rows}', cls="sigshadow", style="padding:16px 22px")
    out["01-banner"] = banner("OFFLINE · ANDROID · 2026", '8 BEST OFFLINE NOTES APPS <span class="s">FOR ANDROID</span>',
                              "Create, edit, and search with no connection. Four can't go online at all.", art, title_size=88, text_width=640)

    y, n = '<span class="yes">NO</span>', '<span class="no">YES</span>'
    data = [("ATOMIC NOTES", n + " (sync)", "Google", "Your Google Drive", "Vault, lock", "Source-available"),
            ("MATERIAL NOTES", y, "None", "Export only", "Locks, encrypted export", "AGPL-3.0"),
            ("OPEN NOTES", y, "None", "ZIP backup", "Lock, no screenshots", "GPL-3.0"),
            ("SNOTZ", y, "None", "Backup file", "Biometric or PIN", "GPL-3.0"),
            ("EASY NOTES", y, "None", "None built in", "Encrypted vault", "GPL-3.0"),
            ("ORGZLY REVIVED", n + " (sync)", "None", "Folder, WebDAV, Dropbox", "Lock", "GPL-3.0"),
            ("NOTES", n + " (extras)", "None", "Text files, ZIP", "None", "GPL-3.0"),
            ("BUTTERFLY", n + " (sync)", "None", "WebDAV, Nextcloud", "None", "AGPL-3.0")]
    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>" for a, b, c, d, e, f in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>INTERNET</th><th>ACCOUNT</th>'
            f'<th>SYNC OR BACKUP</th><th>PROTECTION</th><th>LICENSE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-comparison"] = figure("FIG 2 · AT A GLANCE", 'EIGHT APPS, <span class="s">SIDE BY SIDE</span>', body,
                                  "From each app's F-Droid listing, manifest, or repository on October 9, 2026.", h=920)

    def group(x, lbl, title, apps, note, cls):
        st = "background:transparent;color:#F4F5F1;border-color:#F4F5F1;" if cls == "ink" else ""
        chips = "".join(f'<div class="chip{" on" if a == "ATOMIC NOTES" else ""}" style="margin:8px 8px 0 0;{st}">{a}</div>' for a in apps)
        return box(x, 196, 520, 330, f'<div class="lbl">{lbl}</div><div class="ttl" style="font-size:44px">{title}</div>'
                                     f'<div style="margin-top:14px">{chips}</div><div class="txt" style="margin-top:22px">{note}</div>', cls=cls)
    body = group(56, "NO INTERNET PERMISSION", "CAN'T GO ONLINE", ["MATERIAL NOTES", "OPEN NOTES", "SNOTZ", "EASY NOTES"],
                 "Nothing in the app can send a note anywhere. Back up by hand.", "ink")
    body += group(624, "OFFLINE FIRST, ONLINE LATER", "SYNCS WHEN IT CAN", ["ATOMIC NOTES", "ORGZLY REVIVED", "NOTES", "BUTTERFLY"],
                  "Every daily action works offline. The network is used for sync or extras.", "sigshadow")
    out["03-internet-split"] = figure("FIG 1 · TWO KINDS OF OFFLINE", 'CAN THE APP <span class="s">EVEN GO ONLINE?</span>', body,
                                      "Checked against each app's permissions. Network state alone doesn't count as internet.", h=610)

    q = lambda x, yy, t: box(x, yy, 300, 110, f'<div class="lbl">QUESTION</div><div class="ttl" style="font-size:34px;margin-top:4px">{t}</div>', cls="surface flat", style="padding:12px 18px")
    a = lambda x, yy, t, d: box(x, yy, 300, 120, f'<div class="ttl" style="font-size:32px;margin-top:0">{t}</div><div class="txt muted" style="font-size:19px">{d}</div>', style="padding:12px 18px")
    body = q(56, 330, "NEED SYNC?")
    body += q(450, 170, "WHERE TO?") + q(450, 490, "NEED ENCRYPTION?")
    body += a(844, 110, "ATOMIC NOTES", "Your own Google Drive") + a(844, 260, "ORGZLY · BUTTERFLY", "WebDAV, folders, Nextcloud")
    body += a(844, 440, "EASY NOTES", "Encrypted vault, no internet") + a(844, 590, "MATERIAL NOTES", "Fewest permissions")
    body += ('<div style="position:absolute;left:368px;top:246px;font-family:Mono;font-size:17px;color:#3A2FF0">YES</div>'
             '<div style="position:absolute;left:346px;top:482px;font-family:Mono;font-size:17px;color:#4A4D55">NO</div>'
             '<div style="position:absolute;left:770px;top:140px;font-family:Mono;font-size:16px;color:#3A2FF0">DRIVE</div>'
             '<div style="position:absolute;left:728px;top:326px;font-family:Mono;font-size:16px;color:#4A4D55">OWN SETUP</div>'
             '<div style="position:absolute;left:776px;top:472px;font-family:Mono;font-size:17px;color:#3A2FF0">YES</div>'
             '<div style="position:absolute;left:776px;top:622px;font-family:Mono;font-size:17px;color:#4A4D55">NO</div>')
    lines = (arrow(362, 370, 444, 230, color="sig") + arrow(362, 410, 444, 540, color="ink")
             + arrow(756, 210, 838, 170, color="sig") + arrow(756, 240, 838, 310, color="ink")
             + arrow(756, 530, 838, 500, color="sig") + arrow(756, 565, 838, 640, color="ink"))
    out["04-pick-by-need"] = figure("FIG 5 · QUICK PICK", 'WHICH ONE <span class="s">FITS YOU?</span>', body,
                                    "Open Notes and sNotz suit lists with reminders. Notes suits plain text files.", lines=lines, h=800)

    steps = [("01", "EXPORT ON A SCHEDULE", "Use the app's backup or export once a week, or set it to run by itself where it can."),
             ("02", "COPY IT OFF THE PHONE", "Move the file to a computer, a USB drive, or storage you trust. One copy is not a backup."),
             ("03", "TEST A RESTORE ONCE", "Import it on a spare phone or after a reinstall. A backup you never opened is a guess.")]
    body = ""
    for i, (num, t, d) in enumerate(steps):
        body += box(56 + i * 370, 210, 340, 380, f'<div class="num">{num}</div><div class="ttl" style="font-size:38px">{t}</div><div class="txt muted">{d}</div>',
                    cls="sigshadow" if i == 2 else "")
    lines = arrow(400, 400, 422, 400, color="ink") + arrow(770, 400, 792, 400, color="ink")
    out["05-backup-plan"] = figure("FIG 4 · BACKUPS", 'THE PHONE MAY HOLD <span class="s">THE ONLY COPY</span>', body,
                                   "Ten minutes a month. Apps with sync cover a lost phone, not a deleted note.", lines=lines, h=680)

    body = phone(7, 64, 190, 260, crop=470, shadow="ink")
    facts = [("OFFLINE", "Write, edit, search, delete. No connection needed"), ("SAVES", "To the phone as you type"),
             ("SYNC LATER", "To your own Google Drive, on its own"), ("RETRIES", "After 5, 15, and 45 seconds, then waits"),
             ("CONFLICTS", "Both versions kept, one marked conflict copy"), ("HONEST LIMITS", "Sign-in needs internet once. 30 free notes")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:200px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 3 · OUR PICK, DISCLOSED", 'WHY ATOMIC NOTES <span class="s">IS FIRST</span>', body,
                                         "It's my app, so it goes first. The offline behavior is checkable in its public code.", h=760)
    return out
