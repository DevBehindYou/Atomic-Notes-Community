"""U10 · L3-S1 · What Happens to Your Notes When the Cloud Goes Down? (Medium)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "LOCAL FIRST · OUTAGES"
STEPS = [("FORCE-CLOSE", "Airplane mode on, close the app, reopen it"),
         ("OPEN AN OLD NOTE", "Not today's. Is everything there?"),
         ("WRITE AND EDIT", "Close again. Did both changes stay?"),
         ("SEARCH", "Find a word in an old note"),
         ("RECONNECT", "Does it sync by itself?"),
         ("BOOKMARK STATUS", "Know where to check next time")]


def build():
    out = {}
    art = (box(740, 92, 400, 120, '<div class="lbl" style="color:#BA1A1A">THE CLOUD</div><div class="ttl" style="font-size:40px">OFFLINE</div>', cls="surface flat", style="padding:14px 22px")
           + box(790, 280, 300, 190, '<div class="lbl">YOUR PHONE</div><div class="ttl" style="font-size:34px">ALL NOTES STILL HERE</div>'
                 '<div class="txt" style="font-size:19px">Write now. Sync later.</div>', cls="signal", style="padding:18px 22px"))
    lines = f'<line x1="940" y1="216" x2="940" y2="264" stroke="#BA1A1A" stroke-width="3" stroke-dasharray="8 6"/>'
    out["01-banner"] = banner("LOCAL FIRST · RELIABILITY", 'WHEN THE CLOUD <span class="s">GOES DOWN</span>',
                              "What happens to your notes, and how to test your app in ten minutes.",
                              art + f'<svg class="lines" width="1200" height="630" style="position:absolute;left:0;top:0">{lines}</svg>', title_size=100, text_width=640)

    def screen(x, tag, title, items, cls):
        rows = "".join(f'<div style="padding:9px 0;border-top:1.5px solid {"rgba(255,255,255,.3)" if cls == "signal" else "#C6C6CB"};font-size:19px{";opacity:.35" if dim else ""}">{t}</div>' for t, dim in items)
        return box(x, 190, 340, 340, f'<div class="lbl">{tag}</div><div class="ttl" style="font-size:32px;margin-bottom:10px">{title}</div>{rows}', cls=cls, style="padding:18px 22px")
    body = (screen(56, "WEB OR CLOUD-ONLY", "COULDN'T LOAD", [("Error. Try again later.", False)], "")
            + screen(430, "CACHE-FIRST", "SOME NOTES", [("Meeting agenda", False), ("Groceries", False), ("Old trip plan", True), ("2024 ideas", True)], "")
            + screen(804, "LOCAL-FIRST", "EVERY NOTE", [("Meeting agenda", False), ("Groceries", False), ("Old trip plan", False), ("2024 ideas", False), ("Sync waiting", False)], "signal"))
    out["02-three-apps"] = figure("FIG 1 · DURING AN OUTAGE", 'THREE APPS, <span class="s">SAME OUTAGE</span>', body,
                                  "Grayed notes weren't cached. The local-first app only notices that sync is waiting.", h=620)

    body = ""
    for i, (t, d) in enumerate(STEPS):
        x, y = 56 + (i % 3) * 370, 196 + (i // 3) * 200
        body += box(x, y, 340, 170, f'<div class="num" style="font-size:46px">{i + 1:02d}</div><div class="ttl" style="font-size:32px">{t}</div>'
                    f'<div class="txt muted" style="font-size:19px">{d}</div>', cls="sigshadow" if i == 2 else "", style="padding:14px 20px")
    out["03-outage-test"] = figure("FIG 2 · THE TEST", 'AIRPLANE MODE <span class="s">OUTAGE TEST</span>', body,
                                   "Fail steps 1 to 3, and the next outage locks you out of your own notes.", h=670)
    return out


def social():
    out = {}
    slides = [("01", "WEB-ONLY APPS", "The notes live on the server. When it fails, nothing opens."),
              ("02", "CACHE-FIRST APPS", "You can read what was cached. The rest waits for the servers."),
              ("03", "LOCAL-FIRST APPS", "Every note is on the device. Writing and search keep working."),
              ("04", "IT'S RARELY THE APP", "In 2025, AWS and Google Cloud outages started deep inside the providers."),
              ("05", "TEST IT TODAY", "Airplane mode, force-close, open an old note, write, search, reconnect.")]
    for k, v in carousel(LABEL, 'WHEN THE CLOUD <span class="s">GOES DOWN</span>', "What happens to your notes depends on where the app keeps them.",
                         slides, 'AN OUTAGE SHOULD <span class="s">ONLY DELAY SYNC</span>', "Run the ten-minute airplane mode test on your notes app.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("NOTES CHECKLIST", 'OUTAGE-PROOF <span class="s">YOUR NOTES</span>',
                                  ["Open the app in airplane mode", "Check old notes, not just today's", "Write and edit offline",
                                   "Search without a connection", "Bookmark the status page"])
    return out
