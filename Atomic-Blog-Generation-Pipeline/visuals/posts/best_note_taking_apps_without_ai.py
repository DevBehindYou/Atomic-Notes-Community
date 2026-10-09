"""Figures for P4: 7 Best Note Taking Apps Without AI in 2026."""
from atomic_viz import figure, banner, box, phone, arrow

APPS = ["Atomic Notes", "Markor", "TiddlyWiki", "Zim", "Saber", "Dynalist", "CherryTree"]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:9px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:19px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:31px;line-height:1">{a}</span></div>' for i, a in enumerate(APPS))
    art = box(740, 92, 400, 460, f'<div class="lbl" style="margin-bottom:8px">CHECKED OCTOBER 9, 2026</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("PRIVACY · NO AI · 2026", '7 BEST NOTE TAKING APPS <span class="s">WITHOUT AI</span>',
                              "No assistant reading along. You write, it saves, and that's all.", art, title_size=90, text_width=640)

    none = '<span class="yes">NONE</span>'
    data = [("ATOMIC NOTES", "Android", "Phone + your Drive", "Optional vault", none, "Source-available"),
            ("MARKOR", "Android", "Files you choose", "AES-256 text", none, "Apache-2.0"),
            ("TIDDLYWIKI", "Browser, Node.js", "One HTML file", "AES-256 option", none, "BSD 3-Clause"),
            ("ZIM", "Desktop", "Plain text files", '<span class="no">NONE</span>', none, "GPL-2.0"),
            ("SABER", "Phone, tablet, PC", "Device + Nextcloud", "Before upload", none, "GPL-3.0"),
            ("DYNALIST", "Web, all platforms", "Their servers", '<span class="no">NO E2E</span>', none, "Closed"),
            ("CHERRYTREE", "Desktop", "One local file", "Password", none, "GPL-3.0")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>" for a, b, c, d, e, f in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>PLATFORMS</th><th>NOTES LIVE</th>'
            f'<th>ENCRYPTION</th><th>BUILT-IN AI</th><th>LICENSE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-comparison"] = figure("FIG 2 · AT A GLANCE", 'SEVEN APPS, <span class="s">ZERO ASSISTANTS</span>', body,
                                  "Checked against each app's repository, website, or changelog on October 9, 2026.", h=900)

    # Where a note travels.
    def stop(x, yy, t, d, cls=""):
        return box(x, yy, 230, 120, f'<div class="lbl" style="font-size:16px">{d}</div><div class="ttl" style="font-size:32px">{t}</div>', cls=cls, style="padding:14px 16px")
    body = '<div class="lbl" style="position:absolute;left:56px;top:196px">WITHOUT AI</div>'
    body += stop(56, 226, "YOUR PHONE", "WRITE", "signal") + stop(346, 226, "YOUR STORAGE", "SYNC, IF YOU CHOOSE", "")
    body += '<div class="lbl" style="position:absolute;left:56px;top:420px;color:#BA1A1A">WITH A CLOUD AI FEATURE</div>'
    body += (stop(56, 450, "YOUR PHONE", "TAP SUMMARIZE", "signal") + stop(346, 450, "APP SERVER", "FORWARDS TEXT", "")
             + stop(636, 450, "AI PROVIDER", "RUNS THE MODEL", "warn") + stop(926, 450, "LOGS?", "KEPT HOW LONG?", "warn"))
    lines = (arrow(292, 286, 338, 286, color="sig") + arrow(292, 510, 338, 510, color="ink")
             + arrow(582, 510, 628, 510, color="err") + arrow(872, 510, 918, 510, color="err", dash=True))
    out["03-ai-path"] = figure("FIG 1 · FOLLOW THE NOTE", 'AI ADDS STOPS <span class="s">TO YOUR NOTE\'S TRIP</span>', body,
                               "A general model. Some AI features run on the device. Each app's policy has the details.", lines=lines, h=680)

    steps = [("01", "READ THE NOTES", "Open the release notes before you tap update."),
             ("02", "SEARCH FOR AI WORDS", "Assistant, summarize, generate, Gemini, Copilot."),
             ("03", "OPEN THE SETTINGS", "Find any AI toggle after the update lands."),
             ("04", "WHAT GOES WHERE", "Which text is sent, and to which company."),
             ("05", "HOW LONG IT STAYS", "Retention, human review, and training terms.")]
    body = ""
    for i, (num, t, d) in enumerate(steps):
        body += box(56 + i * 220, 220, 200, 330, f'<div class="num" style="font-size:52px">{num}</div><div class="ttl" style="font-size:31px">{t}</div><div class="txt muted" style="font-size:20px">{d}</div>',
                    cls="sigshadow" if i == 0 else "", style="padding:16px 16px")
    out["04-check-steps"] = figure("FIG 5 · BEFORE YOU UPDATE", 'A TWO-MINUTE <span class="s">AI CHECK</span>', body,
                                   "Apps change. A no-AI app today can ship an assistant next year.", h=640)

    cards = [("LINKED WIKI PAGES", "TIDDLYWIKI", "One file you own. Tags, links, and views from plain text."),
             ("DEEP PAGE TREES", "CHERRYTREE", "Hundreds of nested pages in one local file."),
             ("NESTED OUTLINES", "DYNALIST", "Bullets inside bullets. Online, in maintenance mode.")]
    body = ""
    for i, (habit, app, d) in enumerate(cards):
        body += box(56 + i * 370, 210, 340, 310, f'<div class="lbl">IF YOU USE NOTION FOR</div><div class="ttl" style="font-size:36px">{habit}</div>'
                                                 f'<div class="chip on" style="margin-top:18px">{app}</div><div class="txt muted" style="margin-top:18px">{d}</div>',
                    cls="sigshadow" if i == 0 else "")
    out["05-notion-alternatives"] = figure("FIG 4 · NOTION, WITHOUT THE AI", 'NOTION ALTERNATIVES <span class="s">WITHOUT AI</span>', body,
                                           "Zim also works for a simple desktop wiki. None of these has Notion's database views.", h=610)

    body = phone(4, 64, 190, 260, crop=470, shadow="ink")
    facts = [("AI", "None. No model library in the app"), ("ALSO NONE", "Analytics, ads, or crash reporting"),
             ("NOTES LIVE", "Your phone, then your own Google Drive"), ("ENCRYPTION", "Optional end-to-end vault"),
             ("CHECK IT", "The dependency list is public in pubspec.yaml"), ("HONEST LIMITS", "Android only. Google sign-in. 30 free notes")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:200px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-notes-card"] = figure("FIG 3 · OUR PICK, DISCLOSED", 'WHY ATOMIC NOTES <span class="s">IS FIRST</span>', body,
                                         "It's my app, so it goes first. Every fact here is checkable in its public code.", h=760)
    return out
