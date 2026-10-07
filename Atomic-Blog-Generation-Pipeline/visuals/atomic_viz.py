"""Blog visuals in the Atomic "Technical Editorial" design system.

Every figure is an HTML page rendered to PNG by headless Chrome:
ink #15171B on paper #F4F5F1, one Signal accent #3A2FF0, Bebas Neue headlines,
Hanken Grotesk body, JetBrains Mono labels, ink borders and hard offset shadows
(no blur, no gradients, dot grid on banners only).

Figures are drawn on a 1200 px wide canvas and shown about 760 px wide in an article
(a 0.63 scale), so text is sized up: body >= 22 px, mono labels >= 19 px.

    python visuals/render.py what-is-a-local-first-notes-app
"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PIPELINE = os.path.dirname(HERE)
COMMUNITY = os.path.dirname(PIPELINE)
WORKSPACE = os.path.dirname(COMMUNITY)
CHROME = os.environ.get("CHROME", "C:/Program Files/Google/Chrome/Application/chrome.exe")
# The app repository ships the three brand fonts. Override with ATOMIC_FONTS.
FONTS = os.environ.get("ATOMIC_FONTS", os.path.join(WORKSPACE, "Atomic-Notes-App-V0.2", "assets", "fonts"))
PUBLIC = os.path.join(COMMUNITY, "public")


def file_url(path):
    return "file:///" + os.path.abspath(path).replace(os.sep, "/")


def mockup(n):
    return file_url(os.path.join(PUBLIC, "mockups", f"atomic-notes-mockup-image-{n:02d}.png"))


ATOM = file_url(os.path.join(PUBLIC, "icons", "atom.svg"))
ICON = file_url(os.path.join(PUBLIC, "icon.png"))

CSS = """
@font-face { font-family: Bebas; src: url("__F__/BebasNeue-Regular.ttf"); }
@font-face { font-family: Hanken; font-weight: 400; src: url("__F__/HankenGrotesk-Regular.ttf"); }
@font-face { font-family: Hanken; font-weight: 500; src: url("__F__/HankenGrotesk-Medium.ttf"); }
@font-face { font-family: Hanken; font-weight: 700; src: url("__F__/HankenGrotesk-Bold.ttf"); }
@font-face { font-family: Mono; font-weight: 400; src: url("__F__/JetBrainsMono-Regular.ttf"); }
@font-face { font-family: Mono; font-weight: 500; src: url("__F__/JetBrainsMono-Medium.ttf"); }
:root { --ink:#15171B; --paper:#F4F5F1; --white:#FFFFFF; --surface:#EDEEE8; --signal:#3A2FF0;
        --slate:#4A4D55; --line:#C6C6CB; --light:#8F88FF; --mist:#D8D6FF; --deep:#1D14A0;
        --error:#BA1A1A; --error-bg:#FFDAD6; --on-error:#93000A; --high:#EB7D00; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:__W__px; height:__H__px; overflow:hidden; background:var(--paper); color:var(--ink);
       font-family:Hanken, sans-serif; -webkit-font-smoothing:antialiased; }
.stage { position:relative; width:__W__px; height:__H__px; overflow:hidden; background:var(--paper); }
.stage.dots { background-image:radial-gradient(rgba(21,23,27,.12) 1.6px, transparent 1.8px); background-size:30px 30px; }
.stage.dark { background:var(--ink); color:var(--paper); }
.hdr { position:absolute; left:56px; right:56px; top:40px; display:flex; justify-content:space-between; align-items:center; }
.eyebrow { font-family:Mono; font-size:19px; letter-spacing:3px; text-transform:uppercase; color:var(--signal); }
.dark .eyebrow { color:var(--light); }
.mark { display:flex; align-items:center; gap:10px; font-family:Mono; font-size:17px; letter-spacing:2.5px; color:var(--slate); }
.dark .mark { color:rgba(244,245,241,.62); }
.mark img { width:30px; height:30px; border-radius:7px; box-shadow:2px 2px 0 var(--ink); }
.dark .mark img { box-shadow:2px 2px 0 var(--signal); }
h1.t { position:absolute; left:56px; right:56px; top:78px; font-family:Bebas; font-weight:400; font-size:62px;
       line-height:.95; letter-spacing:.5px; text-transform:uppercase; }
.s { color:var(--signal); }
.dark .s { color:var(--light); }
.rule { position:absolute; left:56px; right:56px; height:0; border-top:1.5px solid var(--ink); }
.dark .rule { border-color:rgba(244,245,241,.3); }
.foot { position:absolute; left:56px; right:56px; bottom:30px; font-family:Mono; font-size:18px; letter-spacing:.6px; color:var(--slate); }
.dark .foot { color:rgba(244,245,241,.62); }
.box { position:absolute; background:var(--white); border:2.5px solid var(--ink); border-radius:9px;
       box-shadow:8px 8px 0 var(--ink); padding:20px 22px; }
.box.sigshadow { box-shadow:8px 8px 0 var(--signal); }
.box.flat { box-shadow:none; }
.box.surface { background:var(--surface); }
.box.signal { background:var(--signal); color:#fff; }
.box.ink { background:var(--ink); color:var(--paper); box-shadow:8px 8px 0 var(--signal); }
.box.warn { background:var(--error-bg); border-color:var(--error); box-shadow:8px 8px 0 var(--error); color:var(--on-error); }
.dark .box { box-shadow:8px 8px 0 var(--signal); border-color:var(--paper); }
.dark .box.panel { background:rgba(244,245,241,.05); border:2px solid rgba(244,245,241,.32); box-shadow:none; color:var(--paper); }
.lbl { font-family:Mono; font-size:19px; letter-spacing:1.6px; text-transform:uppercase; color:var(--signal); }
.box.signal .lbl, .box.ink .lbl { color:var(--mist); }
.box.ink .lbl { color:var(--light); }
.dark .box.panel .lbl { color:var(--light); }
.box.warn .lbl { color:var(--error); }
.muted { color:var(--slate); }
.box.ink .muted, .dark .muted { color:rgba(244,245,241,.7); }
.box.signal .muted { color:var(--mist); }
.ttl { font-family:Bebas; font-size:40px; line-height:.95; text-transform:uppercase; margin-top:8px; }
.ttl.big { font-size:54px; }
.txt { font-size:23px; line-height:1.38; margin-top:8px; }
.num { font-family:Bebas; font-size:60px; line-height:.9; color:var(--signal); }
.box.signal .num { color:#fff; }
.chip { display:inline-block; font-family:Mono; font-size:17px; letter-spacing:1.4px; text-transform:uppercase;
        padding:6px 12px; border:2px solid var(--ink); border-radius:999px; background:var(--paper); }
.chip.on { background:var(--signal); border-color:var(--signal); color:#fff; }
.chip.ink { background:var(--ink); color:var(--paper); }
.chip.bad { background:var(--error-bg); border-color:var(--error); color:var(--on-error); }
.chip.ghost { background:transparent; }
.dark .chip { border-color:var(--paper); background:transparent; color:var(--paper); }
.dark .chip.on { background:var(--signal); border-color:var(--signal); }
.phone { position:absolute; background:var(--ink); border-radius:34px; padding:9px; box-shadow:10px 10px 0 var(--signal); }
.phone.inkshadow { box-shadow:10px 10px 0 var(--ink); }
.phone img { display:block; width:100%; border-radius:26px; }
.phone .cam { position:absolute; top:16px; left:50%; width:9px; height:9px; margin-left:-4px; border-radius:50%; background:#2c2f36; }
table.d { position:absolute; border-collapse:separate; border-spacing:0; background:var(--white); border:2.5px solid var(--ink);
          border-radius:9px; overflow:hidden; box-shadow:8px 8px 0 var(--ink); }
table.d th, table.d td { padding:15px 18px; border-bottom:1.5px solid var(--line); text-align:left; vertical-align:middle; }
table.d thead th { font-family:Mono; font-weight:500; font-size:18px; letter-spacing:1.4px; text-transform:uppercase; background:var(--surface);
                   border-bottom:2.5px solid var(--ink); }
table.d thead th.hl { background:var(--signal); color:#fff; }
table.d tbody th { font-family:Bebas; font-weight:400; font-size:30px; line-height:1; text-transform:uppercase; white-space:nowrap; }
table.d td { font-size:21px; line-height:1.3; }
table.d td.hl { background:rgba(58,47,240,.06); font-weight:500; }
table.d tr:last-child th, table.d tr:last-child td { border-bottom:0; }
.yes { color:var(--signal); font-family:Mono; font-weight:500; }
.no { color:var(--error); font-family:Mono; font-weight:500; }
.part { color:var(--slate); font-family:Mono; font-weight:500; }
svg.lines { position:absolute; inset:0; overflow:visible; }
"""

HEAD = '<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'


def css(w, h):
    return CSS.replace("__F__", file_url(FONTS)).replace("__W__", str(w)).replace("__H__", str(h))


def figure(eyebrow, title, body, foot="", w=1200, h=760, theme="", lines="", title_top=78):
    """A standard figure: eyebrow + brand mark, a split headline (wrap the accent in <span class="s">), content, footnote."""
    hdr = (f'<div class="hdr"><span class="eyebrow">{eyebrow}</span>'
           f'<span class="mark"><img src="{ICON}" alt="">ATOMIC NOTES</span></div>')
    t = f'<h1 class="t" style="top:{title_top}px">{title}</h1>' if title else ""
    f = f'<div class="foot">{foot}</div>' if foot else ""
    svg = f'<svg class="lines" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{ARROWS}{lines}</svg>' if lines else ""
    return HEAD.format(css=css(w, h)) + f'<div class="stage {theme}">{hdr}{t}{svg}{body}{f}</div></body></html>', w, h


ARROWS = """<defs>
<marker id="a-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#15171B"/></marker>
<marker id="a-sig" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#3A2FF0"/></marker>
<marker id="a-err" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#BA1A1A"/></marker>
<marker id="a-light" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#8F88FF"/></marker>
</defs>"""

COLORS = {"ink": "#15171B", "sig": "#3A2FF0", "err": "#BA1A1A", "light": "#8F88FF"}


def arrow(x1, y1, x2, y2, color="ink", dash=False, width=3.5, curve=None):
    c = COLORS[color]
    d = f"M{x1} {y1} Q{curve[0]} {curve[1]} {x2} {y2}" if curve else f"M{x1} {y1} L{x2} {y2}"
    da = ' stroke-dasharray="10 8"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{width}"{da} marker-end="url(#a-{color})"/>'


def box(x, y, w, h, inner, cls="", style=""):
    return f'<div class="box {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{inner}</div>'


def phone(n, x, y, w, crop=None, shadow="sig"):
    """A product screenshot in the phone frame. crop = visible screen height in px."""
    inner = f'<img src="{mockup(n)}" alt="">'
    if crop:
        inner = f'<div style="height:{crop}px;overflow:hidden;border-radius:26px">{inner}</div>'
    cls = "phone" + (" inkshadow" if shadow == "ink" else "")
    return f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px"><span class="cam"></span>{inner}</div>'


def banner(eyebrow, title, sub, art, w=1200, h=630, title_size=92, text_width=640):
    """Article cover and social card: dot-grid paper, giant split headline with an ink offset shadow, art on the right."""
    body = (f'<div class="hdr"><span class="eyebrow">{eyebrow}</span>'
            f'<span class="mark"><img src="{ICON}" alt="">ATOMIC NOTES</span></div>'
            f'<h1 class="t" style="top:96px;width:{text_width}px;font-size:{title_size}px;line-height:.92">{title}</h1>'
            f'<p style="position:absolute;left:56px;bottom:62px;width:{text_width - 40}px;font-size:25px;line-height:1.35;color:#2B2E34">{sub}</p>'
            f'<div class="rule" style="bottom:38px"></div>'
            f'<div class="foot" style="bottom:12px;font-size:15px">ATOMIC-NOTES.DEVBEHINDYOU.COM</div>{art}')
    return HEAD.format(css=css(w, h)) + f'<div class="stage dots">{body}</div></body></html>', w, h


def render(name, page, out_dir, scale=1.5):
    """Writes <name>.html next to the PNG (for review), then screenshots it at the given device scale."""
    html, w, h = page
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(out_dir, "_src")
    os.makedirs(src, exist_ok=True)
    path = os.path.join(src, name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    png = os.path.join(out_dir, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    f"--force-device-scale-factor={scale}", f"--window-size={w},{h}", "--virtual-time-budget=4000",
                    f"--user-data-dir={os.path.join(HERE, '.chrome-profile')}",
                    f"--screenshot={png}", file_url(path)], check=True, capture_output=True)
    return png
