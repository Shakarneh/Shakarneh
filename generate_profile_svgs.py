"""
Generates the animated SVG graphics for github.com/Shakarneh.

Why this exists: GitHub's stats services go down (503) and byte-count language
stats call a backend developer a "CSS developer". These SVGs are generated here,
committed to the repo, and served by GitHub itself - so they are always accurate
and can never break.

Run:  python generate_profile_svgs.py
Out:  assets/api_console.svg, assets/request_flow.svg, assets/skills.svg
"""

from pathlib import Path

OUT = Path(__file__).parent / "assets"

# ── Tokyo Night palette ──────────────────────────────────────────────
BG        = "#1a1b26"
BG_BAR    = "#16161e"
BORDER    = "#2f3549"
FG        = "#c0caf5"
MUTED     = "#565f89"
BLUE      = "#7aa2f7"
CYAN      = "#7dcfff"
GREEN     = "#9ece6a"
ORANGE    = "#ff9e64"
PURPLE    = "#bb9af7"
RED       = "#f7768e"
YELLOW    = "#e0af68"

FONT = "ui-monospace, 'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"


def esc(text: str) -> str:
    """Escape the five XML-significant characters."""
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                .replace('"', "&quot;").replace("'", "&apos;"))


# ══════════════════════════════════════════════════════════════════════
# 1. API CONSOLE - a terminal that types out a GET request and its JSON
# ══════════════════════════════════════════════════════════════════════

def build_api_console() -> str:
    prompt = "curl -s https://api.shakarneh.dev/v1/developer"

    # (indent level, [(text, colour), ...])
    body = [
        (0, [("{", MUTED)]),
        (1, [('"status"', CYAN), (": ", MUTED), ("200 OK", GREEN), (",", MUTED)]),
        (1, [('"name"', CYAN), (": ", MUTED), ('"Mohammed Shakarneh"', GREEN), (",", MUTED)]),
        (1, [('"role"', CYAN), (": ", MUTED), ('"Software Development Engineer"', GREEN), (",", MUTED)]),
        (1, [('"focus"', CYAN), (": [", MUTED), ('"back-end"', GREEN), (", ", MUTED),
             ('"REST APIs"', GREEN), (", ", MUTED), ('"clean architecture"', GREEN), ("],", MUTED)]),
        (1, [('"stack"', CYAN), (": [", MUTED), ('"Python"', GREEN), (", ", MUTED),
             ('"FastAPI"', GREEN), (", ", MUTED), ('"SQLAlchemy"', GREEN), (", ", MUTED),
             ('"PostgreSQL"', GREEN), ("],", MUTED)]),
        (1, [('"experience"', CYAN), (": {", MUTED)]),
        (2, [('"company"', CYAN), (": ", MUTED), ('"Expert Choice CIS"', GREEN), (",", MUTED)]),
        (2, [('"built"', CYAN), (": ", MUTED),
             ('"admin API - JWT, RBAC, conflict detection"', GREEN)]),
        (1, [("},", MUTED)]),
        (1, [('"in_production"', CYAN), (": ", MUTED),
             ('"https://lolocosmetics.shop"', ORANGE), (",", MUTED)]),
        (1, [('"languages"', CYAN), (": [", MUTED), ('"Arabic"', GREEN), (", ", MUTED),
             ('"English"', GREEN), (", ", MUTED), ('"Russian"', GREEN), ("],", MUTED)]),
        (1, [('"learning"', CYAN), (": [", MUTED), ('"OOP mastery"', GREEN), (", ", MUTED),
             ('"clean code"', GREEN), (", ", MUTED), ('"DS & algorithms"', GREEN), ("],", MUTED)]),
        (1, [('"open_to_work"', CYAN), (": ", MUTED), ("true", ORANGE)]),
        (0, [("}", MUTED)]),
    ]

    W, LH = 860, 21
    top = 78                                  # first body line baseline
    H = top + LH * len(body) + 30

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="API response describing Mohammed Shakarneh">',
        "<style>",
        f".m{{font-family:{FONT};font-size:13.5px}}",
        "@keyframes fade{to{opacity:1}}",
        "@keyframes blink{50%{opacity:0}}",
        "@keyframes type{to{width:640px}}",
        ".ln{opacity:0;animation:fade .35s ease forwards}",
        ".cur{animation:blink 1.05s step-end infinite}",
        "</style>",
        # window
        f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{BG}" stroke="{BORDER}"/>',
        f'<path d="M1 13a12 12 0 0 1 12-12h{W-26}a12 12 0 0 1 12 12v25H1z" fill="{BG_BAR}"/>',
        f'<line x1="1" y1="38" x2="{W-1}" y2="38" stroke="{BORDER}"/>',
        f'<circle cx="22" cy="20" r="5.5" fill="{RED}"/>',
        f'<circle cx="42" cy="20" r="5.5" fill="{YELLOW}"/>',
        f'<circle cx="62" cy="20" r="5.5" fill="{GREEN}"/>',
        f'<text class="m" x="{W//2}" y="25" fill="{MUTED}" text-anchor="middle">'
        f'shakarneh — developer profile</text>',
        # typed prompt, revealed by an expanding clip rect
        '<defs><clipPath id="tw"><rect x="0" y="0" height="100%" width="0">'
        '<animate attributeName="width" from="0" to="640" dur="1.4s" fill="freeze"/>'
        "</rect></clipPath></defs>",
        f'<g clip-path="url(#tw)">'
        f'<text class="m" x="20" y="62"><tspan fill="{PURPLE}">$ </tspan>'
        f'<tspan fill="{FG}">{esc(prompt)}</tspan></text></g>',
    ]

    for i, (indent, tokens) in enumerate(body):
        y = top + i * LH
        delay = 1.6 + i * 0.085
        spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in tokens)
        parts.append(
            f'<text class="m ln" x="{20 + indent * 22}" y="{y}" '
            f'style="animation-delay:{delay:.2f}s">{spans}</text>'
        )

    # blinking cursor after the last line
    cy = top + LH * (len(body) - 1) + 4
    parts.append(
        f'<rect class="ln cur" x="34" y="{cy}" width="8" height="15" fill="{BLUE}" '
        f'style="animation-delay:{1.6 + len(body) * 0.085:.2f}s,0s"/>'
    )
    parts.append("</svg>")
    return "\n".join(parts)


# ══════════════════════════════════════════════════════════════════════
# 2. REQUEST FLOW - a packet travelling through the layers of a backend
# ══════════════════════════════════════════════════════════════════════

def build_request_flow() -> str:
    stages = [
        ("Client",     "HTTP + Bearer",     BLUE),
        ("Auth",       "JWT · role check",  PURPLE),
        ("Validation", "Pydantic schema",   CYAN),
        ("Logic",      "business rules",    GREEN),
        ("Database",   "transaction",       ORANGE),
    ]

    W, H = 880, 250
    bw, bh = 142, 76
    gap = (W - 40 - bw * len(stages)) / (len(stages) - 1)
    y = 74
    cycle = 7.0                                   # seconds per full round trip

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="A request flowing from client through auth, validation, logic and database">',
        "<style>",
        f".t{{font-family:{SANS}}}",
        f".mono{{font-family:{FONT}}}",
        "@keyframes pulse{0%,100%{opacity:.35}12%{opacity:1}}",
        "@keyframes glow{0%,100%{stroke-opacity:.25}12%{stroke-opacity:1}}",
        "@keyframes dash{to{stroke-dashoffset:-24}}",
        f".flow{{stroke-dasharray:5 7;animation:dash 1.1s linear infinite}}",
        "</style>",
        f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{BG}" stroke="{BORDER}"/>',
        f'<text class="t" x="24" y="32" font-size="14" font-weight="600" fill="{FG}">'
        f'Request lifecycle</text>',
        f'<text class="t" x="24" y="51" font-size="11.5" fill="{MUTED}">'
        f'the path I can follow end to end — and where it breaks</text>',
    ]

    xs = [20 + i * (bw + gap) for i in range(len(stages))]

    # connectors
    for i in range(len(stages) - 1):
        x1, x2 = xs[i] + bw, xs[i + 1]
        parts.append(
            f'<line class="flow" x1="{x1}" y1="{y + bh/2}" x2="{x2}" y2="{y + bh/2}" '
            f'stroke="{BORDER}" stroke-width="2"/>'
        )

    # stage boxes
    for i, (title, sub, colour) in enumerate(stages):
        x = xs[i]
        d = i * (cycle / (len(stages) * 2.4))
        parts += [
            f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="9" fill="{BG_BAR}" '
            f'stroke="{colour}" stroke-width="1.6" style="animation:glow {cycle}s '
            f'ease-in-out {d:.2f}s infinite"/>',
            f'<text class="t" x="{x + bw/2}" y="{y + 31}" font-size="13.5" font-weight="600" '
            f'fill="{colour}" text-anchor="middle">{esc(title)}</text>',
            f'<text class="mono" x="{x + bw/2}" y="{y + 51}" font-size="10.5" fill="{MUTED}" '
            f'text-anchor="middle">{esc(sub)}</text>',
        ]

    # the travelling packet
    path = f"M {xs[0] + bw/2} {y + bh/2} L {xs[-1] + bw/2} {y + bh/2}"
    parts += [
        f'<path id="rail" d="{path}" fill="none"/>',
        f'<circle r="6" fill="{YELLOW}">'
        f'<animateMotion dur="{cycle}s" repeatCount="indefinite" keyPoints="0;1;1;0;0" '
        f'keyTimes="0;0.42;0.5;0.92;1" calcMode="linear">'
        f'<mpath href="#rail"/></animateMotion></circle>',
        f'<circle r="13" fill="{YELLOW}" opacity=".16">'
        f'<animateMotion dur="{cycle}s" repeatCount="indefinite" keyPoints="0;1;1;0;0" '
        f'keyTimes="0;0.42;0.5;0.92;1" calcMode="linear">'
        f'<mpath href="#rail"/></animateMotion></circle>',
    ]

    # failure / success codes
    codes = [
        (xs[1] + bw / 2, "401 / 403", RED),
        (xs[2] + bw / 2, "422", RED),
        (xs[4] + bw / 2, "200 OK", GREEN),
    ]
    for cx, label, colour in codes:
        parts.append(
            f'<text class="mono" x="{cx}" y="{y + bh + 30}" font-size="11.5" fill="{colour}" '
            f'text-anchor="middle" opacity=".85">{esc(label)}</text>'
        )

    parts.append(
        f'<text class="t" x="{W//2}" y="{H-16}" font-size="10.5" fill="{MUTED}" '
        f'text-anchor="middle">rejected early, or answered — never a crash</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts)


# ══════════════════════════════════════════════════════════════════════
# 3. SKILLS - an honest chart, because byte counts lie
# ══════════════════════════════════════════════════════════════════════

def build_skills() -> str:
    # Where the work actually goes. Edit these freely - they are yours to state.
    skills = [
        ("Python",              92, BLUE),
        ("FastAPI · REST APIs", 88, GREEN),
        ("SQL · data modelling", 82, ORANGE),
        ("JavaScript · React",  75, YELLOW),
        ("PHP · Java",          58, PURPLE),
        ("DevOps · deployment", 52, CYAN),
    ]

    W = 880
    row_h, top = 40, 92
    H = top + row_h * len(skills) + 26
    bar_x, bar_w = 250, 560

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="Skill focus chart">',
        "<style>",
        f".t{{font-family:{SANS}}}",
        f".mono{{font-family:{FONT}}}",
        "@keyframes grow{from{width:0}}",
        "@keyframes fade{to{opacity:1}}",
        ".pct{opacity:0;animation:fade .4s ease forwards}",
        "</style>",
        f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{BG}" stroke="{BORDER}"/>',
        f'<text class="t" x="24" y="36" font-size="14" font-weight="600" fill="{FG}">'
        f'Where the work actually goes</text>',
        f'<text class="t" x="24" y="56" font-size="11.5" fill="{MUTED}">'
        f'GitHub measures bytes, so it thinks I write CSS. This is the real split.</text>',
        f'<line x1="24" y1="70" x2="{W-24}" y2="70" stroke="{BORDER}"/>',
    ]

    for i, (label, pct, colour) in enumerate(skills):
        y = top + i * row_h
        w = int(bar_w * pct / 100)
        delay = i * 0.16
        parts += [
            f'<text class="t" x="24" y="{y + 15}" font-size="12.5" fill="{FG}">{esc(label)}</text>',
            f'<rect x="{bar_x}" y="{y + 3}" width="{bar_w}" height="14" rx="7" fill="{BG_BAR}"/>',
            f'<rect x="{bar_x}" y="{y + 3}" width="{w}" height="14" rx="7" fill="{colour}" '
            f'style="animation:grow 1.1s cubic-bezier(.2,.8,.2,1) {delay:.2f}s backwards"/>',
            f'<text class="mono pct" x="{bar_x + bar_w + 14}" y="{y + 15}" font-size="11.5" '
            f'fill="{MUTED}" style="animation-delay:{delay + .8:.2f}s">{pct}</text>',
        ]

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, svg in (
        ("api_console.svg", build_api_console()),
        ("request_flow.svg", build_request_flow()),
        ("skills.svg", build_skills()),
    ):
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"wrote assets/{name}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
