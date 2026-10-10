"""U01 · L1-S1 · Local Storage vs Cloud Storage for Notes (Medium)."""
from atomic_viz import figure, banner, box, phone, arrow
from social_viz import carousel, pin

LABEL = "LOCAL FIRST · STORAGE"


def _place(x, y, w, h, tag, title, rows, cls=""):
    li = "".join(f'<div style="padding:9px 0;border-top:1.5px solid {"rgba(255,255,255,.35)" if cls in ("signal", "ink") else "#C6C6CB"};font-size:21px">{r}</div>' for r in rows)
    return box(x, y, w, h, f'<div class="lbl">{tag}</div><div class="ttl" style="font-size:40px;margin-bottom:8px">{title}</div>{li}', cls=cls)


def build():
    out = {}
    art = (_place(740, 96, 400, 140, "1 · DEVICE ONLY", "YOUR PHONE", [], "surface flat")
           + _place(740, 256, 400, 140, "2 · COMPANY CLOUD", "THEIR SERVERS", [], "")
           + _place(740, 416, 400, 140, "3 · YOUR OWN CLOUD", "YOUR DRIVE", [], "signal"))
    out["01-banner"] = banner("LOCAL FIRST · STORAGE", 'LOCAL STORAGE <span class="s">VS CLOUD STORAGE</span>',
                              "Three places your notes can live, and what each one means on a bad day.", art, title_size=92, text_width=640)

    body = (_place(56, 196, 340, 300, "1 · DEVICE ONLY", "ON YOUR PHONE", ["Works with no network", "Nobody else can reach it", "Gone if the phone is"], "")
            + _place(430, 196, 340, 300, "2 · COMPANY CLOUD", "THEIR SERVERS", ["Syncs everywhere", "Survives a lost phone", "Their keys, their rules"], "ink")
            + _place(804, 196, 340, 300, "3 · YOUR OWN CLOUD", "YOUR STORAGE", ["Google Drive, iCloud Drive, Nextcloud", "Syncs and backs up", "Your account is the weak point"], "signal"))
    out["02-three-places"] = figure("FIG 1 · THREE PLACES", 'WHERE YOUR NOTES <span class="s">CAN LIVE</span>', body,
                                    "Most apps use one of these, or a mix of two.", h=580)

    ok, no, part = '<span class="yes">SAFE</span>', '<span class="no">AT RISK</span>', '<span class="part">DEPENDS</span>'
    rows = [("LOST PHONE", no, ok, ok), ("ACCOUNT LOCKED", ok, no, part), ("SERVICE SHUTS DOWN", ok, no, ok),
            ("SERVER BREACH", ok, no, part), ("NO SIGNAL", ok, ok, ok)]
    trs = "".join(f"<tr><th style=\"font-size:26px\">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
    body = (f'<table class="d" style="left:56px;top:190px;width:1088px"><thead><tr><th>BAD DAY</th><th>DEVICE ONLY</th>'
            f'<th>COMPANY CLOUD</th><th class="hl">YOUR OWN CLOUD</th></tr></thead><tbody>{trs}</tbody></table>')
    out["03-bad-days"] = figure("FIG 2 · THE BAD DAYS", 'HOW EACH ONE <span class="s">HANDLES TROUBLE</span>', body,
                                "Depends: on your storage account's security and whether the app encrypts before upload.", h=620)

    body = phone(3, 64, 196, 230, crop=400, shadow="ink")
    body += box(370, 230, 300, 170, '<div class="lbl">THE REAL COPY</div><div class="ttl" style="font-size:38px">YOUR PHONE</div><div class="txt" style="font-size:20px">Saved as you type, offline.</div>', cls="signal")
    body += box(840, 230, 300, 170, '<div class="lbl">THE SYNCED COPY</div><div class="ttl" style="font-size:38px">YOUR DRIVE</div><div class="txt" style="font-size:20px">One file per note, your account.</div>')
    body += box(600, 480, 330, 150, '<div class="lbl">THE SERVER</div><div class="ttl" style="font-size:34px">METADATA ONLY</div><div class="txt muted" style="font-size:19px">Orders sync. Never stores note text.</div>', cls="surface flat")
    lines = arrow(674, 315, 832, 315, color="sig") + arrow(765, 404, 765, 472, color="ink", dash=True)
    out["04-hybrid"] = figure("FIG 3 · THE MIX I CHOSE", 'LOCAL FIRST, <span class="s">SYNCED TO YOUR OWN CLOUD</span>', body,
                              "Atomic Notes by DevBehindYou. With the vault off, your Drive holds readable files.", lines=lines, h=720)
    return out


def social():
    out = {}
    slides = [("01", "DEVICE ONLY", "Your notes never leave the phone. Private and offline, but one lost phone takes them with it."),
              ("02", "COMPANY CLOUD", "Synced and convenient. The company holds the keys and sets the rules on your account."),
              ("03", "YOUR OWN CLOUD", "The app syncs into storage you control, like Google Drive. Your account becomes the weak point."),
              ("04", "THE BAD DAYS", "Lost phone, locked account, service shutdown, breach, no signal. Each model fails a different one."),
              ("05", "THE BEST MIX", "Real copy on your device. Second copy in storage you control. That's local first.")]
    for k, v in carousel(LABEL, 'LOCAL VS <span class="s">CLOUD STORAGE</span>', "Where do your notes actually live? Three answers, compared.",
                         slides, 'ONE COPY YOU HOLD. <span class="s">ONE COPY ELSEWHERE.</span>', "That rule survives more bad days than either model alone.").items():
        out[f"03 Instagram/{k}"] = v
    out["07 Pinterest/pin"] = pin("NOTES · STORAGE", 'LOCAL STORAGE <span class="s">VS CLOUD STORAGE</span>',
                                  ["Device only: private, offline, but fragile", "Company cloud: synced, their keys and rules",
                                   "Your own cloud: synced, your account", "Check how each handles 5 bad days",
                                   "Best mix: one copy you hold, one elsewhere"])
    return out
