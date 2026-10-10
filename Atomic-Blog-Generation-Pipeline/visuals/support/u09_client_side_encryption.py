"""U09 · S1-S3 · Client-Side Encryption Explained (DEV Community)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "SECURITY · CLIENT-SIDE"


def build():
    out = {}
    code = ('const key = await deriveKey(phrase, salt);\nconst iv = crypto.getRandomValues(\n  new Uint8Array(12));\n'
            'const sealed = await crypto.subtle\n  .encrypt({ name: "AES-GCM", iv },\n    key, note);\n// upload sealed, never the key')
    art = box(720, 175, 430, 270, f'<div class="lbl">ON THE DEVICE, BEFORE UPLOAD</div>'
              f'<div style="font-family:Mono;font-size:15px;line-height:1.6;white-space:pre;margin-top:14px">{code}</div>', cls="sigshadow", style="padding:18px 22px")
    out["01-banner"] = banner("SECURITY · WEB CRYPTO", 'CLIENT-SIDE <span class="s">ENCRYPTION</span> EXPLAINED',
                              "What happens before a note reaches the cloud, with runnable code.", art, title_size=92, text_width=640)

    def lane(y, tag, cells, cut):
        h = f'<div class="lbl" style="position:absolute;left:56px;top:{y - 40}px">{tag}</div>'
        lines = ""
        for i, (t, plain) in enumerate(cells):
            x = 56 + i * 280
            h += box(x, y, 240, 120, f'<div class="ttl" style="font-size:30px;margin-top:0">{t}</div>'
                     f'<div class="{"no" if plain else "yes"}" style="font-size:18px;margin-top:8px{"" if plain else ";color:#fff"}">{"PLAINTEXT" if plain else "CIPHERTEXT"}</div>',
                     cls="" if plain else "signal", style="padding:16px 18px")
            if i < 3:
                lines += arrow(x + 244, y + 60, x + 276, y + 60, width=2.5)
        cx = 56 + cut * 280 - 20
        lines += f'<line x1="{cx}" y1="{y - 18}" x2="{cx}" y2="{y + 138}" stroke="#BA1A1A" stroke-width="3" stroke-dasharray="8 6"/>'
        return h, lines
    a, la = lane(230, "SERVER-SIDE ENCRYPTION", [("YOUR PHONE", True), ("NETWORK · TLS", False), ("SERVER", True), ("DISK", False)], 3)
    b, lb = lane(470, "CLIENT-SIDE ENCRYPTION", [("YOUR PHONE", True), ("NETWORK", False), ("SERVER", False), ("DISK", False)], 1)
    body = a + b + '<div class="lbl" style="position:absolute;left:820px;top:150px;color:#BA1A1A">- - PLAINTEXT BOUNDARY</div>'
    out["02-plaintext-boundary"] = figure("FIG 1 · THE BOUNDARY", 'WHERE THE PLAINTEXT <span class="s">STOPS</span>', body,
                                          "Server-side: the line sits in the data center. Client-side: it sits on your phone.", lines=la + lb, h=700)

    body = (box(56, 200, 200, 150, '<div class="lbl">IV · NONCE</div><div class="ttl" style="font-size:38px">12 BYTES</div><div class="txt muted" style="font-size:18px">Random. New every save.</div>', style="padding:14px 18px")
            + box(256, 200, 640, 150, '<div class="lbl">CIPHERTEXT</div><div class="ttl" style="font-size:38px">SAME LENGTH AS THE NOTE</div><div class="txt" style="font-size:18px">Unreadable without the key.</div>', cls="signal", style="padding:14px 18px")
            + box(896, 200, 248, 150, '<div class="lbl">AUTH TAG</div><div class="ttl" style="font-size:38px">16 BYTES</div><div class="txt muted" style="font-size:18px">One changed bit, decrypt fails.</div>', style="padding:14px 18px")
            + box(56, 400, 520, 150, '<div class="lbl">SALT · STORED SEPARATELY</div><div class="ttl" style="font-size:34px">16 RANDOM BYTES</div><div class="txt muted" style="font-size:18px">Not secret. Makes each key unique.</div>', cls="surface flat", style="padding:14px 18px")
            + box(624, 400, 520, 150, '<div class="lbl">THE KEY · NEVER STORED HERE</div><div class="ttl" style="font-size:34px">STAYS ON YOUR DEVICE</div><div class="txt" style="font-size:18px">Derived from your passphrase each time.</div>', cls="ink", style="padding:14px 18px"))
    out["03-sealed-note"] = figure("FIG 2 · ONE SEALED NOTE", 'WHAT THE SERVER <span class="s">ACTUALLY GETS</span>', body,
                                   "AES-GCM output from Web Crypto: the IV travels with the ciphertext, the tag is appended.", h=640)
    return out


def social():
    out = {}
    slides = [("01", "SERVER-SIDE", "The cloud encrypts your data after it arrives, with keys it controls."),
              ("02", "CLIENT-SIDE", "Your device encrypts first. The cloud only ever stores ciphertext."),
              ("03", "THE BOUNDARY", "The last point where your data is readable decides who can read it."),
              ("04", "IN THE BROWSER", "Web Crypto does PBKDF2 and AES-GCM in about 40 lines. HTTPS or localhost only."),
              ("05", "THE COMMON MISTAKES", "Logging plaintext, reusing the IV, uploading the key, and leaving titles unencrypted.")]
    for k, v in carousel(LABEL, 'CLIENT-SIDE <span class="s">ENCRYPTION</span>', "What happens before a note reaches the cloud.",
                         slides, 'PUT THE LINE <span class="s">ON YOUR DEVICE</span>', "Runnable Web Crypto code and the four mistakes to avoid.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("DEVELOPER GUIDE", 'CLIENT-SIDE <span class="s">ENCRYPTION BASICS</span>',
                                  ["Derive the key on the device", "Use AES-GCM with a fresh 12-byte IV", "Store the salt, never the key",
                                   "Encrypt titles too, not only bodies", "Never log plaintext"])
    return out
