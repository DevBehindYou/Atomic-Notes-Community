"""U08 · S1-S2 · Zero Knowledge Encryption Explained in 6 Questions (Medium)."""
from atomic_viz import figure, banner, box, arrow
from social_viz import carousel, pin

LABEL = "SECURITY · KEY CUSTODY"


def build():
    out = {}
    art = (box(740, 110, 400, 170, '<div class="lbl">YOUR PHONE</div><div class="ttl" style="font-size:40px">HOLDS THE KEY</div>'
               '<div class="txt" style="font-size:19px">Made from a secret only you know</div>', cls="signal", style="padding:16px 22px")
           + box(740, 350, 400, 170, '<div class="lbl">THE PROVIDER</div><div class="ttl" style="font-size:40px">HOLDS CIPHERTEXT</div>'
                 '<div class="txt muted" style="font-size:19px">Stores and syncs. Never gets the key.</div>', style="padding:16px 22px"))
    lines = arrow(940, 290, 940, 344, color="sig", width=3)
    out["01-banner"] = banner("SECURITY · ENCRYPTION", 'WHO HOLDS THE <span class="s">ENCRYPTION KEY?</span>',
                              "Zero knowledge encryption explained in six questions.", art + f'<svg class="lines" width="1200" height="630" style="position:absolute;left:0;top:0">{lines}</svg>',
                              title_size=88, text_width=640)

    conds = [("THE KEY IS MADE ON YOUR DEVICE", "From a password or phrase, through a slow key derivation function."),
             ("THE KEY NEVER LEAVES IT", "Not in sign-in, not in a backup, not in a support tool."),
             ("ONLY CIPHERTEXT REACHES THE SERVER", "Every note is encrypted before upload, every time.")]
    body, lines = "", ""
    for i, (t, d) in enumerate(conds):
        x = 56 + i * 372
        body += box(x, 200, 340, 240, f'<div class="num" style="font-size:52px">{i + 1:02d}</div><div class="ttl" style="font-size:36px">{t}</div>'
                    f'<div class="txt muted" style="font-size:20px">{d}</div>', cls="sigshadow" if i == 2 else "", style="padding:16px 22px")
        if i < 2:
            lines += arrow(x + 344, 320, x + 368, 320, color="sig", width=3)
    body += box(56, 480, 1088, 76, '<div class="ttl" style="font-size:30px;margin-top:0">ALL THREE TRUE = ZERO KNOWLEDGE. ANY ONE FALSE = THE PROVIDER CAN READ IT.</div>', cls="ink", style="padding:20px 24px")
    out["02-three-conditions"] = figure("FIG 1 · THE CLAIM", 'THREE THINGS <span class="s">MUST BE TRUE</span>', body,
                                        "Zero knowledge is a promise about key custody, not about the cipher.", lines=lines, h=640)

    body = (box(56, 230, 300, 150, '<div class="lbl">START</div><div class="ttl" style="font-size:38px">YOU FORGET YOUR PASSWORD</div>', cls="ink", style="padding:16px 22px")
            + box(450, 230, 300, 150, '<div class="lbl">ASK</div><div class="ttl" style="font-size:34px">CAN THE COMPANY RESTORE YOUR DATA?</div>', cls="sigshadow", style="padding:16px 22px")
            + box(844, 170, 300, 140, '<div class="lbl" style="color:#BA1A1A">YES</div><div class="ttl" style="font-size:32px">IT HOLDS A KEY</div>'
                  '<div class="txt muted" style="font-size:18px">Key escrow. Not zero knowledge.</div>', style="padding:14px 20px")
            + box(844, 350, 300, 140, '<div class="lbl">NO</div><div class="ttl" style="font-size:32px">CONSISTENT WITH ZERO KNOWLEDGE</div>', cls="signal", style="padding:14px 20px")
            + box(56, 470, 694, 120, '<div class="lbl">SOFTER RECOVERY THAT KEEPS THE PROVIDER OUT</div>'
                  '<div class="txt" style="font-size:21px">A printed recovery key, or a trusted contact you chose.</div>', cls="surface flat", style="padding:16px 22px"))
    lines = (arrow(360, 305, 444, 305) + arrow(754, 290, 838, 240, color="err") + arrow(754, 320, 838, 420, color="sig"))
    out["03-recovery-test"] = figure("FIG 2 · THE RECOVERY TEST", 'THE FASTEST WAY <span class="s">TO CHECK THE CLAIM</span>', body,
                                     "Read the provider's forgot-password help page. It answers the key question.", lines=lines, h=680)
    return out


def social():
    out = {}
    slides = [("01", "WHAT IT MEANS", "The provider stores your data but never holds the key to read it."),
              ("02", "WHERE THE NAME COMES FROM", "Zero-knowledge proofs. Most apps borrow the name, not the protocol."),
              ("03", "VS END-TO-END", "Same key rule. End-to-end comes from messaging, zero knowledge from storage."),
              ("04", "THE RECOVERY TEST", "If the company can restore your data after you forget your password, it holds a key."),
              ("05", "THE PRICE", "Lose the password or phrase, and nobody can recover the data. That's also the proof.")]
    for k, v in carousel(LABEL, 'WHO HOLDS THE <span class="s">ENCRYPTION KEY?</span>', "Zero knowledge encryption explained in six questions.",
                         slides, 'ASK WHO HOLDS THE KEY. <span class="s">THEN ASK ABOUT RECOVERY.</span>', "Six questions to test any zero knowledge claim.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("ENCRYPTION GUIDE", 'IS IT REALLY <span class="s">ZERO KNOWLEDGE?</span>',
                                  ["Is the key made on your device?", "Does the key ever leave it?", "Is only ciphertext uploaded?",
                                   "Can the company restore your data?", "Does it search your content on the server?"])
    return out
