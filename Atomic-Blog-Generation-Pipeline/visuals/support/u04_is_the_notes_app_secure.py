"""U04 · P1-S1 · 7 Ways Your Notes App Could Expose You (Medium)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "PRIVACY · NOTES APPS"
PATHS = [("PROVIDER KEYS", "The company can decrypt"), ("ACCOUNT TAKEOVER", "Leaked or reused password"),
         ("TRACKERS AND AI", "Usage and text sent elsewhere"), ("SYNC METADATA", "When, how much, how often"),
         ("SHARED LINKS", "Still open years later"), ("OLD DEVICES", "Still signed in"), ("BACKUPS", "Copies protected differently")]


def build():
    out = {}
    rows = "".join(f'<div style="display:grid;grid-template-columns:40px 1fr;gap:8px;padding:7px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:17px;color:#BA1A1A">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:28px;line-height:1">{t}</span></div>' for i, (t, _) in enumerate(PATHS))
    art = box(740, 92, 400, 460, f'<div class="lbl" style="margin-bottom:6px">EXPOSURE PATHS</div>{rows}', cls="sigshadow", style="padding:16px 22px")
    out["01-banner"] = banner("PRIVACY · SECURITY", '7 WAYS YOUR NOTES APP <span class="s">COULD EXPOSE YOU</span>',
                              "Is the notes app secure? Usually. The leaks happen around it.", art, title_size=86, text_width=640)

    body = box(470, 330, 260, 150, '<div class="lbl">IN THE MIDDLE</div><div class="ttl" style="font-size:40px">YOUR NOTES APP</div>', cls="ink")
    pos = [(56, 196), (56, 356), (56, 516), (880, 196), (880, 356), (880, 516), (470, 560)]
    lines = ""
    for i, ((t, d), (x, y)) in enumerate(zip(PATHS, pos)):
        body += box(x, y, 264, 120, f'<div class="lbl" style="color:#BA1A1A">{i + 1:02d}</div><div class="ttl" style="font-size:28px;margin-top:2px">{t}</div><div class="txt muted" style="font-size:17px;margin-top:2px">{d}</div>', style="padding:10px 16px")
        tx, ty = (x + 264, y + 60) if x < 470 else (x, y + 60) if x > 470 else (x + 132, y)
        ex, ey = (466, 405) if x < 470 else (734, 405) if x > 470 else (600, 486)
        lines += arrow(tx, ty, ex, ey, color="err", dash=True, width=2.5)
    out["02-seven-paths"] = figure("FIG 1 · AROUND THE APP", 'SEVEN WAYS IN, <span class="s">MOSTLY AROUND THE APP</span>', body,
                                   "Most exposure comes from keys, accounts, extra code, and copies.", lines=lines, h=740)

    data = [("ACCOUNT TAKEOVER", "High", "10 minutes", "Unique password, two-step"),
            ("PROVIDER KEYS", "High", "Choose a setting or app", "End-to-end encryption"),
            ("TRACKERS AND AI", "Medium", "5 minutes", "Exodus scan, AI settings off"),
            ("SHARED LINKS", "Medium", "5 minutes", "Revoke old links"),
            ("OLD DEVICES", "Medium", "5 minutes", "Sign out unknown devices"),
            ("BACKUPS", "Medium", "15 minutes", "Find and delete old exports"),
            ("SYNC METADATA", "Low to medium", "Choose an app", "Apps that list what they keep")]
    trs = "".join(f"<tr><th style=\"font-size:24px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>PATH</th><th>RISK</th><th>EFFORT</th>'
            f'<th>FIX</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-fix-order"] = figure("FIG 2 · FIX ORDER", 'WHAT TO FIX <span class="s">FIRST</span>', body,
                                 "Risk ratings are my judgment for a typical user. Your threat model may differ.", h=700)
    return out


def social():
    out = {}
    slides = [("01", "PROVIDER KEYS", "If the company can decrypt your notes, it can read them. Look for end-to-end encryption."),
              ("02", "ACCOUNT TAKEOVER", "Most notes get exposed through a reused password, not a hacked app."),
              ("03", "TRACKERS AND AI", "Analytics report how you use the app. AI features may send your text elsewhere."),
              ("04", "METADATA AND LINKS", "The server sees when you write. Old shared links still open your notes."),
              ("05", "DEVICES AND BACKUPS", "Old phones stay signed in. Exports and backups hold full copies.")]
    for k, v in carousel(LABEL, 'IS YOUR NOTES APP <span class="s">SECURE?</span>', "Usually the app is fine. Seven ways your notes leak around it.",
                         slides, 'FIX THE ACCOUNT <span class="s">AND THE KEYS FIRST</span>', "They expose everything at once. The rest are quick tidy-ups.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("PRIVACY CHECKLIST", 'IS YOUR NOTES APP <span class="s">SECURE?</span>',
                                  ["Who holds the encryption keys?", "Is your account protected with two-step?", "Any trackers or AI features?",
                                   "Old shared links still open?", "Old devices and backups checked?"])
    return out
