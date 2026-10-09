"""Figures for S4: How Does Encryption Protect Privacy? 5 Gaps in Your Notes."""
from atomic_viz import figure, banner, box, phone

GAPS = [("TRANSPORT", "HTTPS ends at the server"), ("KEYS", "The provider may hold them"), ("METADATA", "Dates and sizes stay visible"),
        ("ANALYTICS", "Tracking runs outside encryption"), ("RECOVERY", "A reset path is a key")]


def build():
    out = {}

    rows = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:8px;padding:10px 0;border-top:1.5px solid #C6C6CB">'
                   f'<span style="font-family:Mono;font-weight:500;font-size:18px;color:#BA1A1A">{i + 1:02d}</span>'
                   f'<span><span style="font-family:Bebas;font-size:30px;line-height:1">{a}</span><br><span style="font-size:18px;color:#4A4D55">{b}</span></span></div>'
                   for i, (a, b) in enumerate(GAPS))
    art = box(740, 90, 400, 470, f'<div class="lbl" style="margin-bottom:6px">ENCRYPTED, BUT...</div>{rows}', cls="sigshadow", style="padding:16px 22px")
    out["01-banner"] = banner("SECURITY · PRIVACY", 'HOW DOES ENCRYPTION <span class="s">PROTECT PRIVACY?</span>',
                              "It locks content. Five gaps sit outside the lock.", art, title_size=86, text_width=640)

    descs = ["The server unwraps your note on arrival.", "Server side keys mean the company can read.", "When, how much, how often: all readable.",
             "SDKs report usage beside your notes.", "If they can reset you in, they can read in."]
    body = ""
    for i, ((t, _), d) in enumerate(zip(GAPS, descs)):
        body += box(56 + i * 220, 220, 200, 330, f'<div class="num" style="font-size:52px;color:#BA1A1A">{i + 1:02d}</div><div class="ttl" style="font-size:34px">{t}</div><div class="txt muted" style="font-size:20px">{d}</div>',
                    cls="sigshadow" if i == 1 else "", style="padding:16px 16px")
    out["02-five-gaps"] = figure("FIG 1 · THE GAPS", 'ENCRYPTED IS NOT <span class="s">THE SAME AS PRIVATE</span>', body,
                                 "Each gap sits outside the cipher. A strong cipher doesn't close any of them.", h=650)

    yes, no = '<span class="no">YES</span>', '<span class="yes">NO</span>'
    data = [("ICLOUD NOTES", "Standard", "Apple", yes, "Apple can help"),
            ("ICLOUD NOTES", "With ADP", "Your devices", no, "Recovery key or contact"),
            ("GOOGLE KEEP", "Default", "Google", yes, "Google account"),
            ("ATOMIC NOTES", "T2T, default", "No note key", '<span class="part">IN TRANSIT</span>', "Google sign-in"),
            ("ATOMIC NOTES", "Vault on", "Your phone", no, "Six-word phrase only"),
            ("TYPICAL E2E APP", "Default", "Your devices", no, "Recovery key, if any")]
    trs = "".join(f"<tr><th style=\"font-size:25px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in data)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>APP</th><th>SETUP</th><th>KEY HELD BY</th>'
            f'<th>PROVIDER CAN READ</th><th>RECOVERY</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-key-custody"] = figure("FIG 2 · KEY CUSTODY", 'SAME WORD, <span class="s">DIFFERENT KEY HOLDER</span>', body,
                                   "From Apple, Google, and Atomic Notes documentation, October 9, 2026. Atomic T2T: your Drive holds readable files.", h=760)

    items = ["When the note was created", "When it was last modified", "When it was last viewed", "Whether it's pinned",
             "Whether it's marked as deleted", "Whether it has a drawing or handwriting", "A checksum of imported content"]
    li = "".join(f'<div style="display:grid;grid-template-columns:46px 1fr;padding:9px 0;border-top:1.5px solid #C6C6CB">'
                 f'<span class="lbl" style="font-size:18px">{i + 1:02d}</span><span style="font-size:23px">{x}</span></div>' for i, x in enumerate(items))
    body = box(56, 196, 640, 470, f'<div class="lbl">STAYS UNDER STANDARD PROTECTION</div><div class="ttl" style="font-size:40px;margin-bottom:8px">VISIBLE TO APPLE</div>{li}', cls="warn")
    body += box(740, 196, 404, 470, '<div class="lbl">END-TO-END WITH ADP</div><div class="ttl" style="font-size:40px">HIDDEN</div>'
                '<div class="txt" style="margin-top:14px">Note titles, text, and attachments.</div>'
                '<div class="txt muted" style="margin-top:22px">Apple documents both lists. That openness is what every app should offer.</div>', cls="signal")
    out["04-metadata-stays"] = figure("FIG 3 · METADATA", 'WHAT ADVANCED DATA PROTECTION <span class="s">STILL SHOWS</span>', body,
                                      "Source: Apple's iCloud data security overview, checked October 9, 2026.", h=760)

    qs = [("WHERE?", "In transit, at rest, or on your device?"), ("WHOSE KEY?", "Yours alone, or theirs too?"), ("WHAT'S VISIBLE?", "Is there a published metadata list?"),
          ("WHAT ELSE IS SENT?", "Analytics, crash reports, ads, AI?"), ("HOW DO I RECOVER?", "If they can reset you, they can read.")]
    body = ""
    for i, (q, d) in enumerate(qs):
        x, yy = 56 + (i % 3) * 370, 196 + (i // 3) * 230
        body += box(x, yy, 340, 200, f'<div class="num" style="font-size:44px">{i + 1:02d}</div><div class="ttl" style="font-size:36px">{q}</div><div class="txt muted" style="font-size:21px">{d}</div>',
                    cls="sigshadow" if i == 1 else "", style="padding:14px 20px")
    out["05-five-questions"] = figure("FIG 4 · THE CHECK", 'FIVE QUESTIONS <span class="s">FOR ANY APP</span>', body,
                                      "Vague answers usually mean the gap is real.", h=700)

    body = phone(12, 64, 190, 260, crop=470, shadow="ink")
    facts = [("WHERE", "HTTPS always. On the phone too, with the vault"), ("WHOSE KEY", "Vault: yours, from six words"),
             ("VISIBLE", "IDs, type, flags, times, rough size"), ("ALSO SENT", "Nothing. No analytics or trackers"),
             ("RECOVERY", "Your phrase only. No reset path"), ("HONEST LIMITS", "Vault off by default. No audit yet")]
    rws = "".join(f'<div style="display:grid;grid-template-columns:210px 1fr;gap:14px;padding:11px 0;border-top:1.5px solid #C6C6CB">'
                  f'<span class="lbl" style="font-size:18px">{a}</span><span style="font-size:22px">{b}</span></div>' for a, b in facts)
    body += box(400, 190, 744, 500, f'<div class="ttl big" style="margin-top:0">ATOMIC NOTES</div><div style="margin-top:10px">{rws}</div>', cls="sigshadow")
    out["06-atomic-answers"] = figure("FIG 5 · OUR ANSWERS", 'ATOMIC NOTES, <span class="s">SAME FIVE QUESTIONS</span>', body,
                                      "It's my app, so the bar is higher. Every answer is checkable in its public code.", h=760)
    return out
