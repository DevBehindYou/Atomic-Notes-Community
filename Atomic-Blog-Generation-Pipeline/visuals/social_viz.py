"""Social images in the Atomic "Technical Editorial" style, built on atomic_viz.

    carousel_cover / carousel_slide / carousel_cta   Instagram 4:5, 720 x 900 page -> 1080 x 1350 PNG at scale 1.5
    pin                                              Pinterest 2:3, 667 x 1000 page -> 1000 x 1500 PNG at scale 1.5
"""
from atomic_viz import HEAD, ICON, css

IG_W, IG_H = 720, 900
PIN_W, PIN_H = 667, 1000

EXTRA = """
.sv { position:absolute; inset:0; padding:44px 46px; display:flex; flex-direction:column; }
.sv .top { display:flex; justify-content:space-between; align-items:center; font-family:Mono; font-size:15px; letter-spacing:2.4px; text-transform:uppercase; color:var(--signal); }
.sv.dark .top { color:var(--light); }
.sv .top .mk { display:flex; align-items:center; gap:8px; color:var(--slate); }
.sv.dark .top .mk { color:rgba(244,245,241,.7); }
.sv .top img { width:24px; height:24px; border-radius:6px; }
.sv h1 { font-family:Bebas; font-weight:400; text-transform:uppercase; line-height:.92; margin-top:auto; }
.sv .num { font-family:Bebas; color:var(--signal); line-height:.9; }
.sv.dark .num, .sv.dark .s { color:var(--light); }
.sv p { font-size:30px; line-height:1.36; }
.sv .card { background:#fff; border:2.5px solid var(--ink); border-radius:9px; box-shadow:8px 8px 0 var(--signal); padding:26px 28px; }
.sv .foot { position:static; margin-top:auto; font-family:Mono; font-size:14px; letter-spacing:1.6px; text-transform:uppercase; color:var(--slate); display:flex; justify-content:space-between; }
.sv.dark .foot { color:rgba(244,245,241,.6); }
.sv ul { list-style:none; }
.sv li { display:grid; grid-template-columns:52px 1fr; gap:6px; padding:16px 0; border-top:1.5px solid var(--line); font-size:28px; line-height:1.28; }
.sv li:first-child { border-top:0; }
.sv li b { font-family:Mono; font-weight:500; font-size:20px; color:var(--signal); padding-top:5px; }
"""


def _page(w, h, inner, theme=""):
    stage = f'<div class="stage {theme}">{inner}</div>'
    return HEAD.format(css=css(w, h) + EXTRA) + stage + "</body></html>", w, h


def _top(label, theme=""):
    return (f'<div class="top"><span>{label}</span>'
            f'<span class="mk"><img src="{ICON}" alt="">ATOMIC NOTES</span></div>')


def carousel_cover(label, title, sub, n_slides):
    inner = (f'<div class="sv">{_top(label)}'
             f'<h1 style="font-size:104px">{title}</h1>'
             f'<p style="margin-top:24px;color:#2B2E34">{sub}</p>'
             f'<div class="foot" style="margin-top:44px;flex:none"><span>SWIPE →</span><span>1 / {n_slides}</span></div></div>')
    return _page(IG_W, IG_H, inner, "dots")


def carousel_slide(label, num, title, body, i, n_slides, dark=False):
    inner = (f'<div class="sv {"dark" if dark else ""}">{_top(label)}'
             f'<div class="num" style="font-size:190px;margin-top:auto">{num}</div>'
             f'<h1 style="font-size:84px;margin-top:4px">{title}</h1>'
             f'<p style="margin-top:24px">{body}</p>'
             f'<div class="foot" style="margin-top:auto;flex:none"><span>ATOMIC-NOTES.DEVBEHINDYOU.COM</span><span>{i} / {n_slides}</span></div></div>')
    return _page(IG_W, IG_H, inner, "dark" if dark else "")


def carousel_cta(label, title, line, n_slides):
    inner = (f'<div class="sv dark">{_top(label)}'
             f'<h1 style="font-size:84px">{title}</h1>'
             f'<p style="margin-top:20px;color:rgba(244,245,241,.85)">{line}</p>'
             f'<div class="card" style="margin-top:28px;background:var(--signal);color:#fff;border-color:var(--paper);box-shadow:8px 8px 0 var(--paper)">'
             f'<div style="font-family:Mono;font-size:16px;letter-spacing:2px">READ THE FULL GUIDE</div>'
             f'<div style="font-family:Bebas;font-size:44px;margin-top:6px">LINK IN BIO</div></div>'
             f'<div class="foot" style="margin-top:44px;flex:none"><span>ATOMIC NOTES BY DEVBEHINDYOU</span><span>{n_slides} / {n_slides}</span></div></div>')
    return _page(IG_W, IG_H, inner, "dark")


def pin(label, title, items, footer="READ THE FULL GUIDE"):
    li = "".join(f"<li><b>{i + 1:02d}</b><span>{x}</span></li>" for i, x in enumerate(items))
    inner = (f'<div class="sv">{_top(label)}'
             f'<h1 style="font-size:96px;margin-top:auto">{title}</h1>'
             f'<div class="card" style="margin-top:34px"><ul>{li}</ul></div>'
             f'<div class="foot" style="margin-top:auto;flex:none;padding-top:24px"><span>{footer}</span><span>ATOMIC-NOTES.DEVBEHINDYOU.COM</span></div></div>')
    return _page(PIN_W, PIN_H, inner, "dots")


def carousel(label, cover_title, cover_sub, slides, cta_title, cta_line):
    """slides: [(num, title, body), ...]. Returns {name: page} for the full carousel."""
    n = len(slides) + 2
    out = {"slide-01": carousel_cover(label, cover_title, cover_sub, n)}
    for i, (num, title, body) in enumerate(slides):
        out[f"slide-{i + 2:02d}"] = carousel_slide(label, num, title, body, i + 2, n, dark=(i % 2 == 1))
    out[f"slide-{n:02d}"] = carousel_cta(label, cta_title, cta_line, n)
    return out
