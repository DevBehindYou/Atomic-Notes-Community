"""U06 · P1-S3 · Is Open Source More Secure? (Substack)."""
from atomic_viz import figure, banner, box
from social_viz import carousel, pin

LABEL = "PRIVACY · SOURCE CODE"
CHECKS = [("WHAT DATA LEAVES", "Every network call is in the code"),
          ("HOW ENCRYPTION WORKS", "Cipher, key derivation, where the key is made"),
          ("WHICH SDKS SHIP", "Trackers show up by name"),
          ("WHICH PERMISSIONS", "The manifest lists every one"),
          ("WHAT CHANGED", "History shows each new data flow"),
          ("BUILD MATCHES CODE", "Reproducible builds close the gap")]


def build():
    out = {}
    rows = "".join(f'<div style="display:grid;grid-template-columns:40px 1fr;gap:8px;padding:9px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#3A2FF0">{i + 1:02d}</span>'
                   f'<span style="font-family:Bebas;font-size:29px;line-height:1">{t}</span></div>' for i, (t, _) in enumerate(CHECKS))
    art = box(740, 140, 400, 350, f'<div class="lbl" style="margin-bottom:6px">YOU CAN VERIFY</div>{rows}', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("PRIVACY · TRANSPARENCY", 'IS OPEN SOURCE <span class="s">MORE SECURE?</span>',
                              "Public code doesn't make software safe. It makes it checkable.", art, title_size=96, text_width=640)

    y, p, n = '<span class="yes">YES</span>', '<span class="part">PARTLY</span>', '<span class="no">NO</span>'
    data = [("READ THE CODE", n, y, y),
            ("VERIFY PRIVACY CLAIMS", n, y, y),
            ("BUILD IT YOURSELF", n, p + " · TO VERIFY", y),
            ("MODIFY AND REDISTRIBUTE", n, n, y),
            ("FORK IT IF ABANDONED", n, n, y)]
    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td class=\"hl\">{c}</td><td>{d}</td></tr>" for a, b, c, d in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th style="width:360px">WHAT YOU CAN DO</th><th>CLOSED</th>'
            f'<th class="hl">SOURCE-AVAILABLE</th><th>OPEN SOURCE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-three-models"] = figure("FIG 1 · THREE MODELS", 'READ, VERIFY, BUILD, <span class="s">REUSE</span>', body,
                                    "For verification, source-available and open source are close. Reuse is where they split.", h=640)

    rungs = [("PRIVACY POLICY", "Describes intent"), ("PERMISSION LIST", "Shows what the app may touch"),
             ("PUBLIC CODE", "Shows what the app does"), ("MATCHING CHECKSUMS", "Your file is the published file"),
             ("REPRODUCIBLE BUILDS", "Your file came from that code"), ("INDEPENDENT AUDIT", "Someone qualified actually looked")]
    body = ""
    for i, (t, d) in enumerate(rungs):
        x, yy = 56 + i * 178, 520 - i * 64
        cls = "signal" if i == 5 else ""
        body += box(x, yy, 168, 600 - yy + 40, f'<div class="num" style="font-size:34px">{i + 1:02d}</div><div class="ttl" style="font-size:26px">{t}</div>'
                    f'<div class="txt{"" if i == 5 else " muted"}" style="font-size:17px">{d}</div>', cls=cls, style="padding:12px 14px")
    out["03-evidence-ladder"] = figure("FIG 2 · EVIDENCE", 'FROM WEAKEST <span class="s">TO STRONGEST</span>', body,
                                       "Each step up removes one thing you have to take on trust.", h=720)
    return out


def social():
    out = {}
    slides = [("01", "OPEN IS NOT SAFE", "Open code makes bugs findable, not absent. Someone still has to look."),
              ("02", "HEARTBLEED", "A serious OpenSSL bug sat in public code from 2011 until 2014."),
              ("03", "THE XZ BACKDOOR", "Caught in 2024 because one engineer noticed slow SSH logins and read the code."),
              ("04", "WHAT YOU CAN CHECK", "Network calls, encryption, trackers, permissions, and every change between versions."),
              ("05", "WHAT YOU CAN'T", "That anyone reviewed it, that the server matches, or that your build came from that code.")]
    for k, v in carousel(LABEL, 'IS OPEN SOURCE <span class="s">MORE SECURE?</span>', "Not automatically. Public code makes software checkable, not safe.",
                         slides, 'TREAT IT AS <span class="s">AN INVITATION</span>', "Public code earns trust only when someone uses it to check.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("PRIVACY CHECKLIST", 'WHAT PUBLIC CODE <span class="s">LETS YOU VERIFY</span>',
                                  ["What data leaves the app", "How the encryption works", "Which trackers are bundled",
                                   "Which permissions it asks for", "Whether your build matches the code"])
    return out
