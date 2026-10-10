"""U02 · L1-S2 · Local First vs Offline First vs Cloud First (DEV Community)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "LOCAL FIRST · ARCHITECTURE"


def build():
    out = {}
    def lane(y, tag, title, first, cls):
        return box(740, y, 400, 136, f'<div class="lbl">{tag}</div><div class="ttl" style="font-size:36px">{title}</div><div class="txt" style="font-size:19px;margin-top:2px">{first}</div>', cls=cls, style="padding:14px 20px")
    art = (lane(92, "CLOUD FIRST", "SERVER WRITES FIRST", "No network, no save.", "surface flat")
           + lane(250, "OFFLINE FIRST", "QUEUE, THEN SERVER", "Works offline. Server decides.", "")
           + lane(408, "LOCAL FIRST", "DEVICE IS THE TRUTH", "Server only helps sync.", "signal"))
    out["01-banner"] = banner("ARCHITECTURE · SYNC", 'LOCAL FIRST VS <span class="s">OFFLINE FIRST</span>',
                              "Works offline isn't the same thing. Seven differences, with code.", art, title_size=96, text_width=640)

    rows = [("SOURCE OF TRUTH", "Server", "Server, local replica", "Device"),
            ("WRITE PATH", "Network round trip", "Local write, queued", "Local write"),
            ("OFFLINE SCOPE", "Little or none", "Most features", "Everything but sync"),
            ("CONFLICTS", "Server decides", "Server rules", "Merged on device"),
            ("SYNC SHAPE", "Request, response", "Queue or replication", "Replication"),
            ("DATA OWNERSHIP", "Provider", "Provider", "User"),
            ("BACKEND DIES", '<span class="no">APP STOPS</span>', '<span class="part">GOES STALE</span>', '<span class="yes">KEEPS WORKING</span>')]
    trs = "".join(f"<tr><th style=\"font-size:24px\">{a}</th><td>{b}</td><td>{c}</td><td class=\"hl\">{d}</td></tr>" for a, b, c, d in rows)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>DIFFERENCE</th><th>CLOUD FIRST</th>'
            f'<th>OFFLINE FIRST</th><th class="hl">LOCAL FIRST</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-seven-differences"] = figure("FIG 1 · SEVEN DIFFERENCES", 'THREE MODELS, <span class="s">SIDE BY SIDE</span>', body,
                                         "The first row decides the other six.", h=720)
    return out


def social():
    out = {}
    slides = [("01", "SOURCE OF TRUTH", "Cloud first and offline first trust the server. Local first trusts the device."),
              ("02", "WRITE PATH", "Cloud first waits for a round trip. The other two save locally in milliseconds."),
              ("03", "CONFLICTS", "Offline first lets the server settle them. Local first merges on the device or keeps both copies."),
              ("04", "OWNERSHIP", "If the server is the truth, the provider owns the data in practice. Local first hands it back."),
              ("05", "THE REAL TEST", "Switch the backend off for a week. Offline first goes stale. Local first doesn't notice.")]
    for k, v in carousel(LABEL, 'LOCAL FIRST <span class="s">VS OFFLINE FIRST</span>', "Both work without a network. Only one makes the device the source of truth.",
                         slides, 'WORKS OFFLINE <span class="s">IS NOT LOCAL FIRST</span>', "Seven differences and a code sketch of each write path.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("ARCHITECTURE", 'LOCAL FIRST VS <span class="s">OFFLINE FIRST</span>',
                                  ["Who holds the source of truth", "Where the first write goes", "Who settles conflicts",
                                   "Who owns the data", "What happens when the backend dies"])
    return out
