"""U07 · S1-S1 · HTTPS vs Encryption at Rest vs E2EE (DEV Community)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "SECURITY · ENCRYPTION"
MONO = "font-family:Mono;font-size:19px;line-height:1.55;white-space:pre"


def build():
    out = {}
    def stage(y, tag, title, cls):
        return box(740, y, 400, 118, f'<div class="lbl">{tag}</div><div class="ttl" style="font-size:34px">{title}</div>', cls=cls, style="padding:14px 20px")
    art = (stage(100, "TLS · IN TRANSIT", "STOPS THE NETWORK", "surface flat")
           + stage(250, "AT REST", "STOPS DISK THEFT", "")
           + stage(400, "END-TO-END", "STOPS THE PROVIDER", "signal"))
    out["01-banner"] = banner("SECURITY · ENCRYPTION", 'HTTPS VS AT REST<br><span class="s">VS E2EE</span>',
                              "Three kinds of encryption, three different attackers. Five differences.", art, title_size=96, text_width=640)

    L, R = '<span class="no">READABLE</span>', '<span class="yes">LOCKED</span>'
    rows = [("TLS ONLY", L, R, L, L), ("TLS + AT REST", L, R, L, R + " · PROVIDER KEY"), ("END-TO-END", L, R, R, R + " · YOUR KEY")]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td class=\"hl\">{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th style="width:230px">MODEL</th><th>YOUR PHONE</th><th>NETWORK</th>'
            f'<th class="hl">SERVER MEMORY</th><th>DISK</th></tr></thead><tbody>{trs}</tbody></table>')
    out["02-where-plaintext-lives"] = figure("FIG 1 · DATA IN USE", 'WHERE THE PLAINTEXT <span class="s">LIVES</span>', body,
                                             "The server memory column is the gap. Only end-to-end closes it.", h=470)

    plain = '{\n  "id": "n_8f2c",\n  "updatedAt": "2026-10-10T09:14Z",\n  "title": "Landlord call",\n  "body": "Deposit dispute...",\n  "pinned": true\n}'
    sealed = '{\n  "id": "n_8f2c",\n  "updatedAt": "2026-10-10T09:14Z",\n  "title": "c2VhbGVkOmFlcy0y...",\n  "body": "q7Jx0Y2b8vWm1kR4...",\n  "pinned": true\n}'
    body = (box(56, 196, 520, 330, f'<div class="lbl" style="color:#BA1A1A">TLS + AT REST</div><div class="ttl" style="font-size:32px">THE SERVER READS THIS</div>'
                f'<div style="{MONO};margin-top:14px">{plain}</div>', style="padding:18px 24px")
            + box(624, 196, 520, 330, f'<div class="lbl">END-TO-END</div><div class="ttl" style="font-size:32px">THE SERVER STORES THIS</div>'
                  f'<div style="{MONO};margin-top:14px">{sealed}</div>', cls="sigshadow", style="padding:18px 24px"))
    out["03-server-view"] = figure("FIG 2 · THE SERVER'S VIEW", 'SAME NOTE, <span class="s">TWO RECORDS</span>', body,
                                   "ID, timestamp, and pinned flag stay readable in both. End-to-end hides content, not metadata.", h=620)
    return out


def social():
    out = {}
    slides = [("01", "TLS IN TRANSIT", "Stops someone on the network. The server decrypts the data on arrival."),
              ("02", "ENCRYPTION AT REST", "Stops someone with a stolen disk. The provider holds the key."),
              ("03", "END-TO-END", "Your device encrypts first. The server only ever stores ciphertext."),
              ("04", "THE GAP", "Between the wire and the disk, data sits in server memory as plaintext."),
              ("05", "THE TRADE", "End-to-end costs server search and easy recovery. Lose the key, lose the data.")]
    for k, v in carousel(LABEL, 'HTTPS VS AT REST <span class="s">VS E2EE</span>', "Encrypted in transit and at rest still means the provider can read it.",
                         slides, 'ASK WHO HOLDS <span class="s">THE KEY</span>', "Five differences, with the JSON a server actually stores.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("ENCRYPTION GUIDE", 'TRANSIT VS AT REST <span class="s">VS END-TO-END</span>',
                                  ["TLS stops network snooping", "At rest stops disk theft", "Neither stops the provider",
                                   "End-to-end keeps plaintext off the server", "Metadata usually stays readable"])
    return out
