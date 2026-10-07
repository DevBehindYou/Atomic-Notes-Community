"""Figures for L1: What Is a Local First Notes App and Why Does It Matter?"""
from atomic_viz import figure, banner, box, phone, arrow


def build():
    out = {}

    art = (phone(3, 820, 92, 300, crop=560)
           + box(690, 452, 300, 118,
                 '<div class="lbl">SAVED ON DEVICE</div><div class="ttl" style="font-size:44px">0 MS · OFFLINE</div>',
                 cls="sigshadow", style="padding:16px 20px"))
    out["01-banner"] = banner(
        "LOCAL FIRST · THE GUIDE",
        'WHAT IS A <span class="s">LOCAL FIRST</span> NOTES APP?',
        "Your phone holds the real copy. The cloud holds a backup. Here is why that order matters.",
        art, title_size=96, text_width=620)

    # Two ways to save one note.
    def lane(y, label, steps, note, sig):
        html = f'<div class="lbl" style="position:absolute;left:56px;top:{y - 40}px">{label}</div>'
        x = 56
        for i, (t, d, cls) in enumerate(steps):
            html += box(x, y, 238, 132, f'<div class="ttl" style="margin-top:0;font-size:36px">{t}</div><div class="txt muted" style="font-size:21px">{d}</div>',
                        cls=cls, style="padding:16px 18px")
            x += 278
        html += f'<p style="position:absolute;left:56px;top:{y + 152}px;font-size:22px;color:#2B2E34;width:1080px">{note}</p>'
        return html

    body = lane(214, "CLOUD-FIRST APP", [
        ("You type", "A new line in a note.", ""),
        ("Network", "The app sends it out.", "surface flat"),
        ("Server saves", "The real copy lives there.", "surface flat"),
        ("Phone shows saved", "Only after the reply.", ""),
    ], "Every save waits on a round trip. No network means no save, or a cache that may not survive.", False)
    body += lane(496, "LOCAL-FIRST APP", [
        ("You type", "A new line in a note.", ""),
        ("Phone saves", "Written to device storage.", "signal flat"),
        ("Sync later", "Queued until a network shows up.", "surface flat"),
        ("Cloud copy", "A backup that follows you.", ""),
    ], "The save finishes on the device. Sync is a separate job that can wait.", True)
    lines = ""
    for y, color, dash in ((280, "ink", False), (562, "sig", False)):
        for i in range(3):
            x1 = 56 + 238 + i * 278 + 6
            lines += arrow(x1, y, x1 + 26, y, color=color, dash=(dash or (y == 562 and i == 1)), width=3)
    out["02-two-ways-to-save"] = figure("FIG 1 · THE WRITE PATH", 'TWO WAYS TO <span class="s">SAVE A NOTE</span>', body, lines=lines, h=712)

    # The spectrum of where the source of truth lives.
    stops = [
        ("CLOUD ONLY", "The server holds the only real copy. Your screen is a window onto it.", "Most web notes tools", ""),
        ("OFFLINE CACHE", "Recent notes are cached for reading. New writes may fail or wait.", "Many sync apps", ""),
        ("OFFLINE FIRST", "Writes queue on the device, but the server's copy wins any argument.", "Apps built to survive bad signal", "surface"),
        ("LOCAL FIRST", "The device owns the data. Sync copies it to other devices and the cloud.", "Atomic Notes, Obsidian, Logseq", "signal"),
    ]
    body = ""
    for i, (t, d, ex, cls) in enumerate(stops):
        x = 56 + i * 280
        body += box(x, 256, 248, 330,
                    f'<div class="lbl">{"0" + str(i + 1)}</div><div class="ttl">{t}</div><div class="txt {"muted" if cls != "signal" else ""}" style="font-size:21px">{d}</div>'
                    f'<div style="position:absolute;left:22px;right:22px;bottom:18px;font-family:Mono;font-size:17px;letter-spacing:.5px">{ex}</div>',
                    cls=cls + (" sigshadow" if cls == "signal" else ""), style="padding:18px 20px")
    body += ('<div style="position:absolute;left:56px;right:56px;top:186px;display:flex;justify-content:space-between;font-family:Mono;font-size:19px;letter-spacing:1.6px">'
             '<span>THE SERVER OWNS IT</span><span class="s">YOU OWN IT</span></div>')
    lines = arrow(56, 228, 1136, 228, color="sig", width=4)
    out["03-source-of-truth-spectrum"] = figure("FIG 2 · THE SPECTRUM", 'WHERE DOES <span class="s">THE REAL COPY</span> LIVE?', body,
                                                "Offline support is a feature. Local first is an architecture.", lines=lines, h=680)

    # Seven ideals, Ink & Switch 2019.
    ideals = [("NO SPINNERS", "Instant, because the data is already on the device."),
              ("MULTI-DEVICE", "Your work is not trapped on one device."),
              ("NETWORK OPTIONAL", "Full reading and writing with no connection."),
              ("COLLABORATION", "Real-time work with other people."),
              ("THE LONG NOW", "Data that still opens years from now."),
              ("PRIVACY BY DEFAULT", "Security and privacy are not an upgrade."),
              ("YOU OWN IT", "Ultimate ownership and control stay with you.")]
    body = ""
    for i, (t, d) in enumerate(ideals):
        col, row = (i % 4, i // 4)
        x = 56 + col * 276 + (138 if row == 1 else 0)
        y = 196 + row * 244
        body += box(x, y, 246, 214,
                    f'<div class="num" style="font-size:52px">{i + 1:02d}</div><div class="ttl" style="font-size:34px">{t}</div><div class="txt muted" style="font-size:21px">{d}</div>',
                    cls="signal sigshadow" if i == 6 else "", style="padding:16px 18px")
    out["04-seven-ideals"] = figure("FIG 3 · INK & SWITCH, 2019", 'THE SEVEN IDEALS OF <span class="s">LOCAL-FIRST SOFTWARE</span>', body,
                                    "Source: \"Local-first software\", Ink & Switch, 2019.", h=740)

    # How Atomic Notes applies it.
    body = phone(7, 64, 196, 250, crop=470, shadow="ink")
    body += box(390, 190, 360, 196,
                '<div class="lbl">1 · YOUR PHONE</div><div class="ttl">THE REAL COPY</div><div class="txt" style="font-size:21px">Hive storage on the device. Every note saves as you type, online or not.</div>',
                cls="sigshadow")
    body += box(390, 430, 360, 196,
                '<div class="lbl">2 · SYNC SERVER</div><div class="ttl">METADATA ONLY</div><div class="txt muted" style="font-size:21px">IDs, timestamps, flags, and versions. Never your titles or note text.</div>',
                cls="surface")
    body += box(800, 190, 344, 436,
                '<div class="lbl">3 · YOUR GOOGLE DRIVE</div><div class="ttl">MY-ATOMIC-NOTES</div>'
                '<div style="margin-top:14px;font-family:Mono;font-size:19px;line-height:2.1">3f2a9c41….atomic<br>8b17e0d2….atomic<br>c04d5b9e….atomic</div>'
                '<div class="txt muted" style="font-size:21px;margin-top:10px">One file per note, in a folder you own. The app can only see files it created.</div>')
    body += ('<div style="position:absolute;left:390px;top:660px;width:754px;display:flex;gap:14px;align-items:center">'
             '<span class="chip on" style="white-space:nowrap">VAULT · OPTIONAL</span><span style="font-size:21px">Turn it on and the server and Drive only ever hold ciphertext.</span></div>')
    lines = arrow(752, 288, 796, 288, color="sig") + arrow(570, 388, 570, 426, color="ink", dash=True) + arrow(752, 528, 796, 528, color="ink", dash=True)
    out["05-atomic-notes-layers"] = figure("FIG 4 · ATOMIC NOTES", 'PHONE FIRST. <span class="s">DRIVE SECOND.</span>', body, lines=lines, h=760)

    # The honest tradeoffs.
    rows = [
        ("CONFLICTS", "Two devices can edit the same note offline.", "A stale edit is refused and saved as a conflict copy. Nothing is overwritten."),
        ("LOST PHONE", "Edits that never synced live on one device.", "Auto sync runs a few seconds after you stop typing, on resume, and on reconnect."),
        ("HARDER TO BUILD", "Retries, queues, and versions are real engineering.", "Replay-safe requests and one transaction per push."),
        ("COLLABORATION", "Real-time co-editing needs CRDTs or similar.", "Not supported. Atomic Notes is a personal notes app."),
    ]
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td><td class=\"hl\">{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:200px;width:1088px"><thead><tr><th style="width:230px">TRADEOFF</th><th>WHAT IT MEANS</th>'
            f'<th class="hl">HOW ATOMIC NOTES HANDLES IT</th></tr></thead><tbody>{trs}</tbody></table>')
    out["06-local-first-tradeoffs"] = figure("FIG 5 · THE COST", 'WHAT LOCAL FIRST <span class="s">ASKS OF YOU</span>', body,
                                             "Local first moves the hard work from the server into the sync engine.", h=740)
    return out
