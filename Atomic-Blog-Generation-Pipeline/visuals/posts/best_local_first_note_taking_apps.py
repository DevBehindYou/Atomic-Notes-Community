"""Figures for L2: 6 Best Local First Note Taking Apps in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

APPS = ["Atomic Notes", "Obsidian", "Logseq", "SiYuan", "SilverBullet", "Trilium Notes"]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:19px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:33px;line-height:1">{a}</span></div>' for i, a in enumerate(APPS))
    art = box(740, 100, 400, 440, f'<div class="lbl" style="margin-bottom:8px">CHECKED OCTOBER 9, 2026</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("LOCAL FIRST · 2026", '6 BEST LOCAL FIRST <span class="s">NOTE TAKING APPS</span>',
                              "Your device holds the real copy. The cloud is a helper you can switch off.", art, title_size=90, text_width=640)

    y, n, p = '<span class="yes">YES</span>', '<span class="no">NO</span>', '<span class="part">OPTIONAL</span>'
    data = [("ATOMIC NOTES", "Android phone", "JSON files in your Drive", "Your Google Drive", p, "Source-available"),
            ("OBSIDIAN", "Folder on device", "Markdown files", "Paid or any folder sync", "Obsidian Sync: yes", "Closed"),
            ("LOGSEQ", "Device", "Files (OG) or database", "Folder sync or own E2E", "Logseq sync: yes", "AGPL-3.0"),
            ("SIYUAN", "Local workspace", ".sy JSON documents", "Paid cloud, S3, WebDAV", y, "AGPL-3.0"),
            ("SILVERBULLET", "Folder you host", "Markdown files", "Server you run", n, "MIT"),
            ("TRILIUM NOTES", "Desktop database", "SQLite", "Server you run", "Per note", "AGPL-3.0")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>" for a, b, c, d, e, f in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>PRIMARY COPY</th><th>FORMAT</th>'
            f'<th>SYNC</th><th>ENCRYPTED SYNC</th><th>LICENSE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-comparison"] = figure("FIG 2 · AT A GLANCE", 'SIX APPS, <span class="s">SIDE BY SIDE</span>', body,
                                  "Checked against each app's repository, docs, or changelog on October 9, 2026.", h=870)

    # Which copy is the real one?
    def side(x, label, title, top_t, top_d, top_cls, bot_t, bot_d, bot_cls, sig_top):
        b = f'<div class="lbl" style="position:absolute;left:{x}px;top:186px">{label}</div>'
        b += f'<div style="position:absolute;left:{x}px;top:214px;font-family:Bebas;font-size:44px;line-height:1">{title}</div>'
        b += box(x, 288, 470, 150, f'<div class="lbl">{top_t}</div><div class="txt">{top_d}</div>', cls=top_cls)
        b += box(x, 530, 470, 150, f'<div class="lbl">{bot_t}</div><div class="txt">{bot_d}</div>', cls=bot_cls)
        return b
    body = side(56, "CLOUD FIRST", "THE SERVER OWNS IT", "SERVER · THE REAL NOTE", "Every save goes here first. No server, no save.", "ink",
                "YOUR PHONE · A CACHE", "Goes stale offline. New notes wait in a queue.", "surface flat", True)
    body += side(674, "LOCAL FIRST", "YOUR DEVICE OWNS IT", "CLOUD · A COPY", "Moves notes between devices. You can turn it off.", "surface flat",
                 "YOUR PHONE · THE REAL NOTE", "Every save lands here first, with or without a network.", "signal", False)
    lines = arrow(291, 446, 291, 522, color="ink") + arrow(909, 522, 909, 446, color="sig")
    lines += '<line x1="600" y1="190" x2="600" y2="690" stroke="#C6C6CB" stroke-width="2" stroke-dasharray="8 8"/>'
    out["03-primary-copy"] = figure("FIG 1 · THE ONE QUESTION", 'WHICH COPY IS <span class="s">THE REAL ONE?</span>', body,
                                    "Arrows show which way a new note travels first.", lines=lines, h=760)

    # Sync spectrum.
    cols = [("NO SERVER TO MANAGE", "Storage you already have", ["ATOMIC NOTES", "OBSIDIAN"], "Your Google Drive, or Obsidian Sync and folder tools"),
            ("A SERVICE OR YOUR STORAGE", "Pick either", ["LOGSEQ", "SIYUAN"], "Their encrypted cloud, or your own folders, S3, or WebDAV"),
            ("A SERVER YOU RUN", "Full control, more work", ["SILVERBULLET", "TRILIUM NOTES"], "Docker or a small VPS at home or rented")]
    body = '<div style="position:absolute;left:56px;right:56px;top:214px;height:14px;background:#EDEEE8;border:2px solid #15171B;border-radius:999px"></div>'
    body += '<div style="position:absolute;left:58px;top:216px;width:360px;height:10px;background:#3A2FF0;border-radius:999px"></div>'
    for i, (t, s, apps, d) in enumerate(cols):
        x = 56 + i * 370
        chips = "".join(f'<div class="chip{" on" if a == "ATOMIC NOTES" else ""}" style="margin:6px 8px 0 0">{a}</div>' for a in apps)
        body += box(x, 262, 340, 380, f'<div class="lbl">{s}</div><div class="ttl" style="font-size:38px">{t}</div>'
                                     f'<div style="margin-top:14px">{chips}</div><div class="txt muted" style="font-size:21px;margin-top:18px">{d}</div>',
                    cls="sigshadow" if i == 0 else "")
    out["04-sync-spectrum"] = figure("FIG 5 · WHO RUNS SYNC", 'FROM STORAGE YOU OWN <span class="s">TO A SERVER YOU RUN</span>', body,
                                     "Every app here also works with sync switched off.", h=720)

    # Shutdown test.
    y2, part = '<span class="yes">YES</span>', '<span class="part">EXPORT FIRST</span>'
    data = [("ATOMIC NOTES", "Every note, on the phone", "JSON files in your Drive", y2, "<span class=\"part\">READ THE JSON</span>"),
            ("OBSIDIAN", "Markdown vault", "Your folder sync keeps going", y2, '<span class="yes">NOTHING TO DO</span>'),
            ("LOGSEQ", "Files or database graph", "Your folder sync keeps going", y2, "<span class=\"part\">DB GRAPHS: EXPORT</span>"),
            ("SIYUAN", ".sy JSON workspace", "Encrypted copy in your S3", y2, part),
            ("SILVERBULLET", "Markdown folder", "Your server keeps going", y2, '<span class="yes">NOTHING TO DO</span>'),
            ("TRILIUM NOTES", "SQLite database", "Your server keeps going", y2, part)]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>ON YOUR DEVICE</th><th>THE SYNC COPY</th>'
            f'<th>KEEP WRITING?</th><th>TO MOVE APPS</th></tr></thead><tbody>{trs}</tbody></table>')
    out["05-shutdown-test"] = figure("FIG 4 · THE SHUTDOWN TEST", 'THE COMPANY IS GONE. <span class="s">WHAT IS LEFT?</span>', body,
                                     "From each app's docs. Official cloud services stop. Anything you host or own stays.", h=790)

    body = phone(3, 64, 190, 260, crop=470, shadow="ink")
    facts = [("PRIMARY COPY", "Your phone. Saved as you type, no network needed"), ("SYNC", "Optional, to a folder in your own Google Drive"),
             ("SERVER", "Metadata only, never note titles or text"), ("CONFLICTS", "Kept as a separate conflict copy"),
             ("NO", "Ads, trackers, or AI"), ("HONEST LIMITS", "Android only. Google sign-in. No export button yet")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:230px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 3 · OUR PICK, DISCLOSED", 'WHY ATOMIC NOTES <span class="s">IS FIRST</span>', body,
                                         "It's my app, so it goes first. Every fact on this card is checkable in its public code.", h=760)
    return out
