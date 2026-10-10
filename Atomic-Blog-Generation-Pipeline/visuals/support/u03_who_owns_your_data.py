"""U03 · L1-S3 · Who Owns Your Data? (Substack)."""
from atomic_viz import figure, banner, box
from social_viz import carousel, pin

LABEL = "DATA OWNERSHIP"
QS = [("WHERE DOES THE FILE LIVE?", "A copy you can open without the app's servers"),
      ("WHAT DOES THE LICENSE SAY?", "Scope, duration, and AI training"),
      ("CAN YOU TAKE IT OUT?", "Complete, readable, self-serve export"),
      ("IF THE ACCOUNT GOES?", "A copy that doesn't need you to sign in"),
      ("IF THE COMPANY GOES?", "Open formats and a recent export")]


def build():
    out = {}
    rows = "".join(f'<div style="display:grid;grid-template-columns:40px 1fr;gap:8px;padding:12px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:30px;line-height:1">{q}</span></div>' for i, (q, _) in enumerate(QS))
    art = box(740, 100, 400, 440, f'<div class="lbl" style="margin-bottom:8px">FIVE QUESTIONS</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("DATA OWNERSHIP · NOTES", 'WHO OWNS <span class="s">YOUR DATA?</span>',
                              "The terms say your content is yours. Here's how to check if you can actually keep it.", art, title_size=104, text_width=640)

    body = ""
    for i, (q, d) in enumerate(QS):
        x, y = 56 + (i % 3) * 370, 196 + (i // 3) * 240
        body += box(x, y, 340, 210, f'<div class="num" style="font-size:46px">{i + 1:02d}</div><div class="ttl" style="font-size:34px">{q}</div><div class="txt muted" style="font-size:20px">{d}</div>',
                    cls="sigshadow" if i == 2 else "", style="padding:14px 20px")
    body += box(796, 436, 340, 210, '<div class="lbl">THE TEST</div><div class="ttl" style="font-size:34px">KEEP IT. MOVE IT. LEAVE.</div><div class="txt" style="font-size:20px">If you can do all three, you own it.</div>', cls="signal", style="padding:14px 20px")
    out["02-five-questions"] = figure("FIG 1 · THE CHECK", 'FIVE QUESTIONS ABOUT <span class="s">OWNING YOUR NOTES</span>', body,
                                      "Legal ownership is the floor. Practical ownership is these five answers.", h=720)

    y, p, n = '<span class="yes">YES</span>', '<span class="part">PARTLY</span>', '<span class="no">NO</span>'
    data = [("WHERE THE FILE LIVES", y, "Your phone, plus one JSON file per note in your own Google Drive"),
            ("THE LICENSE", y, "Used only to run sync. No ads, no AI, no analytics"),
            ("A USABLE EXPORT", p, "Files are yours to download from Drive. No export button yet"),
            ("IF THE ACCOUNT GOES", p, "Phone and Drive copies remain. Vault notes need the phrase"),
            ("IF THE COMPANY GOES", y, "Your files stay in your Drive in a documented format")]
    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th style="width:330px">QUESTION</th><th style="width:150px">ANSWER</th>'
            f'<th>HOW</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-atomic-scorecard"] = figure("FIG 2 · MY OWN APP", 'ATOMIC NOTES, <span class="s">SAME FIVE QUESTIONS</span>', body,
                                        "I build Atomic Notes by DevBehindYou. Partly means partly, and the export button is still to come.", h=700)
    return out


def social():
    out = {}
    slides = [(f"0{i + 1}", q, d + ".") for i, (q, d) in enumerate(QS)]
    for k, v in carousel(LABEL, 'WHO OWNS <span class="s">YOUR DATA?</span>', "The terms say it's yours. Five questions show whether you can actually keep it.",
                         slides, 'KEEP IT. MOVE IT. <span class="s">LEAVE WITH IT.</span>', "If you can do all three, you own your notes.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("DATA OWNERSHIP", 'WHO OWNS <span class="s">YOUR NOTES?</span>',
                                  ["Where does the file actually live?", "What does the license allow?", "Can you export in a usable format?",
                                   "What if your account is locked?", "What if the company shuts down?"])
    return out
