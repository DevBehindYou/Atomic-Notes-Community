"""U05 · P1-S2 · What App Permissions Should You Allow a Notes App? (Medium)."""
from atomic_viz import figure, banner, box
from social_viz import carousel, pin

LABEL = "ANDROID · PERMISSIONS"
FIVE = [("CONTACTS", "Sharing works without it", "Deny"),
        ("LOCATION", "Location reminders, geotags", "Only this time"),
        ("MICROPHONE", "Voice notes", "Only when recording"),
        ("CAMERA", "Scanning, photo notes", "Only this time"),
        ("ALL FILES ACCESS", "File-based Markdown apps", "Deny unless that's why you chose it")]


def build():
    out = {}
    chips = "".join(f'<div class="chip bad" style="margin:8px 8px 0 0;font-size:19px">{t}</div>' for t, _, _ in FIVE)
    art = box(740, 120, 400, 380, f'<div class="lbl">QUESTION THESE FIVE</div><div style="margin-top:10px">{chips}</div>'
                                  f'<div class="lbl" style="margin-top:26px">USUALLY FINE</div><div style="margin-top:6px">'
                                  + "".join(f'<div class="chip on" style="margin:8px 8px 0 0;font-size:19px">{t}</div>' for t in ("INTERNET", "NOTIFICATIONS", "BIOMETRIC"))
                                  + '</div>', cls="sigshadow")
    out["01-banner"] = banner("ANDROID · PRIVACY", 'WHAT APP PERMISSIONS <span class="s">SHOULD YOU ALLOW?</span>',
                              "A notes app needs very little. Five permissions worth questioning.", art, title_size=84, text_width=640)

    good = [("INTERNET", "For sync. Install-time, no dialog"), ("NETWORK STATE", "Checks if you're online"),
            ("BIOMETRIC", "For an app lock"), ("NOTIFICATIONS", "For reminders")]
    bad = [(t, d) for t, d, _ in FIVE]
    def col(x, title, items, cls, tone):
        li = "".join(f'<div style="padding:10px 0;border-top:1.5px solid {"rgba(255,255,255,.35)" if cls=="signal" else "#C6C6CB"}"><div style="font-family:Bebas;font-size:30px;line-height:1">{t}</div>'
                     f'<div style="font-size:19px;margin-top:3px">{d}</div></div>' for t, d in items)
        return box(x, 196, 520, 520, f'<div class="lbl">{tone}</div><div class="ttl" style="font-size:42px;margin-bottom:6px">{title}</div>{li}', cls=cls)
    body = col(56, "USUALLY FINE", good, "signal", "IF THE FEATURE IS ON") + col(624, "WORTH QUESTIONING", bad, "warn", "NEEDS A REASON")
    out["02-permission-groups"] = figure("FIG 1 · TWO GROUPS", 'NOTES APP PERMISSIONS, <span class="s">SORTED</span>', body,
                                         "Storage for the app's own notes needs no permission at all.", h=790)

    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in FIVE)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th style="width:280px">PERMISSION</th><th>FAIR REASON</th>'
            f'<th>IF YOU DON\'T USE THAT FEATURE</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-five-to-question"] = figure("FIG 2 · THE FIVE", 'FIVE PERMISSIONS <span class="s">TO QUESTION</span>', body,
                                        "From Android's permission docs. Only this time exists for location, microphone, and camera since Android 11.", h=670)
    return out


def social():
    out = {}
    slides = [("01", "CONTACTS", "A notes app almost never needs your address book. Sharing works without it."),
              ("02", "LOCATION", "Only for location reminders. Pick Only this time, never Allow all the time."),
              ("03", "MICROPHONE", "Fair for voice notes. Grant it when you record, not at first launch."),
              ("04", "CAMERA", "Fair for scanning or photo notes. Otherwise, deny it."),
              ("05", "ALL FILES ACCESS", "Opens every document on your phone. Only file-based Markdown apps have a reason.")]
    for k, v in carousel(LABEL, 'WHAT PERMISSIONS <span class="s">SHOULD YOU ALLOW?</span>', "A notes app needs very little. Here are five to question.",
                         slides, 'INTERNET HAS <span class="s">NO DIALOG</span>', "It's granted at install. Check the full permission list before you install.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("ANDROID CHECKLIST", 'NOTES APP <span class="s">PERMISSIONS</span>',
                                  ["Contacts: deny", "Location: only this time", "Microphone: only for voice notes",
                                   "Camera: only for scanning", "All files access: almost never"])
    return out
