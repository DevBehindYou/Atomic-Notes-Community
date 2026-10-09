"""Figures for S5: Switch Notes App Safely, 7 Checks Before You Move."""
from atomic_viz import figure, banner, box, phone, arrow

CHECKS = [("EXPORT FORMAT", "Markdown, HTML, or JSON travel well"), ("ATTACHMENTS", "Count them before you move"),
          ("ENCRYPTION", "Unlock on your own device to export"), ("RECOVERY", "Know the new app's way back in"),
          ("OFFLINE", "Open the new app in airplane mode"), ("STORAGE", "Who holds the synced copy?"),
          ("SHUTDOWN RISK", "How would you leave the new app?")]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:40px 1fr;gap:8px;padding:8px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:29px;line-height:1">{a}</span></div>' for i, (a, _) in enumerate(CHECKS))
    art = box(740, 92, 400, 460, f'<div class="lbl" style="margin-bottom:6px">BEFORE YOU MOVE</div>{rows}', cls="sigshadow", style="padding:16px 22px")
    out["01-banner"] = banner("MIGRATION · 2026", 'SWITCH NOTES APP <span class="s">SAFELY</span>',
                              "Seven checks, a rollback copy, and a two-week overlap. Nothing left behind.", art, title_size=96, text_width=640)

    body = ""
    for i, (t, d) in enumerate(CHECKS):
        x, yy = 56 + (i % 4) * 275, 196 + (i // 4) * 230
        body += box(x, yy, 255, 205, f'<div class="num" style="font-size:44px">{i + 1:02d}</div><div class="ttl" style="font-size:31px">{t}</div><div class="txt muted" style="font-size:19px">{d}</div>',
                    cls="sigshadow" if i == 0 else "", style="padding:14px 18px")
    body += box(881, 426, 255, 205, '<div class="lbl">THEN</div><div class="ttl" style="font-size:31px">FOLLOW THE PLAN</div><div class="txt" style="font-size:19px">Export, freeze a copy, import, count, wait.</div>', cls="signal", style="padding:14px 18px")
    out["02-seven-checks"] = figure("FIG 1 · THE CHECKS", 'SEVEN CHECKS <span class="s">BEFORE YOU MOVE</span>', body,
                                    "Each one has cost someone their notes. Most take a minute.", h=700)

    data = [("GOOGLE KEEP", "Google Takeout", "HTML and JSON", "Each note as two files"),
            ("APPLE NOTES", "Export as Markdown", "Markdown + images", "iOS 26 or macOS Tahoe. No folders"),
            ("EVERNOTE", "Desktop app only", "ENEX or HTML", "100 notes at a time, or notebooks"),
            ("NOTION", "Settings or page menu", "Markdown + CSV, HTML, PDF", "Databases arrive as CSV"),
            ("OBSIDIAN", "Nothing to do", "Markdown files", "Plugins' data may not travel"),
            ("ATOMIC NOTES", "No button yet", "JSON files in your Drive", "Vault notes stay encrypted")]
    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>HOW</th><th>YOU GET</th>'
            f'<th>WATCH FOR</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-export-formats"] = figure("FIG 2 · EXPORTS", 'HOW POPULAR APPS <span class="s">LET YOU LEAVE</span>', body,
                                      "Checked against each app's help pages on October 9, 2026.", h=680)

    steps = [("01", "EXPORT", "Everything, with attachments."), ("02", "FREEZE A COPY", "Zip it. Put it somewhere else. Don't touch it."),
             ("03", "IMPORT", "From a second copy, never the frozen one."), ("04", "COUNT", "Notes, checklists, attachments."),
             ("05", "OVERLAP", "Use both apps for two weeks."), ("06", "RETIRE", "Close the old account last.")]
    body = ""
    for i, (num, t, d) in enumerate(steps):
        body += box(56 + i * 183, 230, 165, 300, f'<div class="num" style="font-size:46px">{num}</div><div class="ttl" style="font-size:30px">{t}</div><div class="txt muted" style="font-size:19px">{d}</div>',
                    cls="sigshadow" if i == 1 else "", style="padding:14px 14px")
    out["04-migration-plan"] = figure("FIG 3 · THE PLAN", 'A MOVE WITH <span class="s">A WAY BACK</span>', body,
                                      "Step 2 is the rollback copy. It exists so you never have to use it.", h=620)

    marks = [(0, "DAY 0", "Export and freeze the rollback copy"), (1, "DAY 1", "Import, then count"),
             (2, "DAYS 2 TO 14", "Use both apps. Search for old notes"), (3, "DAY 15", "Close the old account"),
             (4, "ONE YEAR", "Keep the rollback copy until then")]
    body = '<div style="position:absolute;left:156px;width:888px;top:250px;height:6px;background:#15171B"></div>'
    for i, lbl, d in marks:
        x = 56 + i * 222
        cx = x + 100
        body += f'<div style="position:absolute;left:{cx - 13}px;top:240px;width:26px;height:26px;border-radius:50%;background:{"#3A2FF0" if i in (0, 4) else "#15171B"};border:4px solid #F4F5F1"></div>'
        body += box(x, 300, 200, 170, f'<div class="lbl">{lbl}</div><div class="txt" style="font-size:21px">{d}</div>',
                    cls="sigshadow" if i in (0, 4) else "", style="padding:14px 16px")
    out["05-timeline"] = figure("FIG 4 · TIMING", 'TWO WEEKS OF OVERLAP, <span class="s">ONE YEAR OF BACKUP</span>', body,
                                "Yearly notes, like tax lists, won't show up in two weeks. The rollback copy covers them.", h=560)

    body = phone(3, 64, 190, 260, crop=470, shadow="ink")
    facts = [("WHERE NOTES LIVE", "One JSON file per note in your own Drive"), ("GETTING OUT", "Download the folder, convert with a script"),
             ("VAULT NOTES", "Stay encrypted. Only the app opens them"), ("GETTING IN", "No import tool yet. Paste by hand"),
             ("EXPORT BUTTON", "Not built yet. It's planned"), ("LOCK-IN", "None by format. The files are yours")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:230px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">MOVING WITH ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 5 · OUR APP, HONESTLY", 'IN AND OUT OF <span class="s">ATOMIC NOTES</span>', body,
                                         "I build it. The way out works today with a script. A one-tap export is still to come.", h=760)
    return out
