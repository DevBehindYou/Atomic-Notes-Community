"""Figures for S1: Encrypted Notes Explained: T2T vs End to End Encryption."""
from atomic_viz import figure, banner, box, arrow

CIPHER = "q3Nf0Vb8LJ2kYp9Hc4WuR1mE7TzaX6oPdgKs5tB0iQwlUvC2rh8eMyFnG7jA3SxD"


def build():
    out = {}

    art = (box(690, 96, 450, 196,
               '<div class="lbl">VAULT OFF · T2T</div>'
               '<div style="font-family:Mono;font-size:20px;line-height:1.55;margin-top:12px">{"enc_v": 0,<br>&nbsp;"body": "Locker code 4471.<br>&nbsp;&nbsp;Call Dr. Rao."}</div>',
               style="padding:18px 22px")
           + box(730, 330, 430, 210,
                 '<div class="lbl">VAULT ON · END TO END</div>'
                 f'<div style="font-family:Mono;font-size:19px;line-height:1.5;margin-top:12px;word-break:break-all;color:#D8D6FF">{{"enc_v": 1, "payload":<br>"{CIPHER[:44]}…"}}</div>',
                 cls="ink", style="padding:18px 22px"))
    out["01-banner"] = banner("SECURITY · THE GUIDE", 'ENCRYPTED NOTES, <span class="s">EXPLAINED</span>',
                              "Three things \"encrypted\" can mean, and the one that keeps the company out of your notes.",
                              art, title_size=104, text_width=600)

    # Where plain text exists under each model.
    plain, locked = '<span class="chip bad">PLAIN</span>', '<span class="chip on">LOCKED</span>'
    rows = [("HTTPS ONLY", [plain, locked, plain, plain]),
            ("AT REST", [plain, locked, plain, locked]),
            ("END TO END", [plain, locked, locked, locked])]
    trs = "".join(f"<tr><th>{n}</th>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>" for n, cells in rows)
    body = (f'<table class="d" style="left:56px;top:200px;width:1088px"><thead><tr><th style="width:250px">MODEL</th>'
            f'<th>YOUR PHONE</th><th>THE NETWORK</th><th>THE SERVER</th><th>THE DISK</th></tr></thead><tbody>{trs}</tbody></table>'
            '<p style="position:absolute;left:56px;top:560px;width:1088px;font-size:23px;line-height:1.4;color:#2B2E34">'
            'Your own phone always shows plain text, because you read your notes there. The question is where else plain text exists. '
            'Only end-to-end encryption keeps it off the server and the disk.</p>')
    out["02-three-meanings"] = figure("FIG 1 · THREE MEANINGS", 'WHERE IS YOUR NOTE <span class="s">READABLE?</span>', body, h=720)

    # Key flow in the Atomic Notes vault.
    words = " ".join(f'<span class="chip ink" style="margin:0 6px 8px 0">{w}</span>' for w in ["gopher", "beckon", "cultivate", "dolphin", "mentor", "clause"])
    body = box(56, 196, 330, 262, f'<div class="lbl">1 · RECOVERY PHRASE</div><div style="margin-top:12px">{words}</div>'
                                   '<div class="txt muted" style="font-size:20px">6 words from 1,024. Shown once.</div>', cls="sigshadow")
    body += box(456, 196, 300, 262, '<div class="lbl">2 · ARGON2ID</div><div class="ttl">64 MIB · 3 PASSES</div>'
                                     '<div class="txt muted" style="font-size:20px">Salt = SHA-256 of an app tag plus your account ID. Slow on purpose.</div>')
    body += box(826, 196, 318, 262, '<div class="lbl">3 · 256-BIT KEY</div><div class="ttl">NEVER LEAVES THE PHONE</div>'
                                     '<div class="txt" style="font-size:20px">Same phrase, same key, on every device.</div>', cls="signal sigshadow")
    body += box(56, 520, 500, 210, '<div class="lbl">4 · AES-256-GCM</div><div class="ttl">SEAL EACH NOTE</div>'
                                    '<div class="txt muted" style="font-size:20px">Fresh 12-byte nonce, 16-byte tag. Title, body, and checklist items go into one sealed payload.</div>')
    body += box(626, 520, 518, 210, f'<div class="lbl">5 · WHAT LEAVES THE PHONE</div><div style="font-family:Mono;font-size:18px;line-height:1.45;margin-top:10px;word-break:break-all;color:#D8D6FF">{CIPHER}</div>'
                                     '<div class="txt" style="font-size:20px;margin-top:8px">The server and Drive store only this.</div>', cls="ink")
    lines = arrow(392, 326, 450, 326, color="sig") + arrow(762, 326, 820, 326, color="sig") + arrow(985, 464, 360, 514, color="sig", curve=(700, 500)) + arrow(562, 624, 620, 624, color="sig")
    out["03-vault-key-flow"] = figure("FIG 2 · THE VAULT", 'FROM SIX WORDS <span class="s">TO CIPHERTEXT</span>', body,
                                      "The server keeps a verifier: a known phrase sealed with your key, so a wrong phrase fails without revealing anything.", lines=lines, h=820)

    # T2T vs vault.
    rows = [("LEAVES YOUR PHONE", "Plain text over HTTPS", "Ciphertext over HTTPS"),
            ("SYNC SERVER SEES", "Note text in transit, never stored", "Ciphertext only"),
            ("YOUR DRIVE HOLDS", "Readable JSON file", "Sealed JSON file"),
            ("WHO CAN READ IT", "You, and anyone in your Google account", "Only your devices with the phrase"),
            ("LOSE THE PHRASE", "Nothing to lose", "Vault notes are gone for good")]
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td><td class=\"hl\">{c}</td></tr>" for a, b, c in rows)
    body = (f'<table class="d" style="left:56px;top:196px;width:1088px"><thead><tr><th style="width:300px"></th><th>T2T · DEFAULT</th>'
            f'<th class="hl">VAULT · OPTIONAL</th></tr></thead><tbody>{trs}</tbody></table>')
    out["04-t2t-vs-vault"] = figure("FIG 3 · ATOMIC NOTES", 'TWO MODES. <span class="s">YOUR CHOICE.</span>', body,
                                    "T2T means transport encryption: HTTPS protects the trip, not the destination.", h=700)

    # What end-to-end hides and what it doesn't.
    hidden = "".join(f'<div style="padding:9px 0;border-top:1.5px solid rgba(244,245,241,.2);font-size:23px">{x}</div>' for x in ["Note titles", "Note text", "Checklist items"])
    visible = "".join(f'<div style="padding:9px 0;border-top:1.5px solid #C6C6CB;font-size:23px">{x}</div>' for x in
                      ["That a note exists, and its ID", "Text note or checklist", "Pinned or deleted", "When it was created and changed", "Roughly how big it is", "Which Google account owns it"])
    body = box(56, 196, 470, 470, f'<div class="lbl">HIDDEN BY THE VAULT</div><div class="ttl big">THE CONTENT</div><div style="margin-top:14px">{hidden}</div>', cls="ink")
    body += box(586, 196, 558, 470, f'<div class="lbl" style="color:#4A4D55">STILL VISIBLE TO THE SERVER</div><div class="ttl big">THE METADATA</div><div style="margin-top:14px">{visible}</div>', cls="surface flat")
    out["05-what-e2e-hides"] = figure("FIG 4 · THE LIMITS", 'WHAT END-TO-END <span class="s">CAN AND CAN\'T HIDE</span>', body,
                                      "Every end-to-end encrypted app leaks some metadata. Good ones keep it small and say what it is.", h=740)

    # Recovery tradeoff.
    body = box(56, 196, 520, 400, '<div class="lbl" style="color:#4A4D55">PROVIDER CAN RESET</div><div class="ttl big">CONVENIENT</div>'
                                   '<div class="txt" style="font-size:22px;margin-top:14px">Forget your password and support restores your notes.</div>'
                                   '<div class="txt" style="font-size:22px;margin-top:14px"><b>The catch:</b> if the company can restore your notes, it can read them.</div>',
               cls="surface flat")
    body += box(624, 196, 520, 400, '<div class="lbl">ONLY YOUR PHRASE</div><div class="ttl big">IN CONTROL</div>'
                                     '<div class="txt" style="font-size:22px;margin-top:14px">Nobody else holds a copy of the key, including the developer.</div>'
                                     '<div class="txt" style="font-size:22px;margin-top:14px"><b>The catch:</b> lose the phrase and the vault stays locked forever.</div>',
                cls="signal sigshadow")
    body += ('<p style="position:absolute;left:56px;top:636px;width:1088px;font-size:23px;line-height:1.4;color:#2B2E34">'
             'Pick by threat model. A shopping list doesn\'t need the vault. A note about your health, money, or safety probably does.</p>')
    out["06-recovery-tradeoff"] = figure("FIG 5 · THE TRADE", 'WHO CAN RECOVER <span class="s">YOUR NOTES?</span>', body, h=740)
    return out
