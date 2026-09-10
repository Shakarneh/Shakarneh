"""
Generates the animated SVG graphics for github.com/Shakarneh.

Why this exists: GitHub's stats services go down (503) and byte-count language
stats call a backend developer a "CSS developer". These SVGs are generated here,
committed to the repo, and served by GitHub itself - so they are always accurate
and can never break.

Run:  python generate_profile_svgs.py
Out:  assets/api_console.svg, assets/request_flow.svg, assets/skills.svg,
      assets/contributions.svg  (fetches live data from GitHub)
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
             ('"Django"', GREEN), (", ", MUTED), ('"FastAPI"', GREEN), (", ", MUTED),
             ('"PostgreSQL"', GREEN), (", ", MUTED), ('"Redis"', GREEN), (", ", MUTED),
             ('"Docker"', GREEN), ("],", MUTED)]),
        (1, [('"latest_build"', CYAN), (": {", MUTED)]),
        (2, [('"project"', CYAN), (": ", MUTED), ('"benchFlow"', GREEN), (",", MUTED)]),
        (2, [('"solves"', CYAN), (": ", MUTED),
             ('"the assignment problem - Hungarian algorithm"', GREEN), (",", MUTED)]),
        (2, [('"proof"', CYAN), (": ", MUTED),
             ('"649 tests - layering enforced in CI"', GREEN)]),
        (1, [("},", MUTED)]),
        (1, [('"experience"', CYAN), (": {", MUTED)]),
        (2, [('"company"', CYAN), (": ", MUTED), ('"Expert Choice CIS"', GREEN), (",", MUTED)]),
        (2, [('"built"', CYAN), (": ", MUTED),
             ('"admin API - JWT, RBAC, conflict detection"', GREEN)]),
        (1, [("},", MUTED)]),
        (1, [('"in_production"', CYAN), (": [", MUTED)]),
        (2, [('"https://benchflow-qfzq.onrender.com"', ORANGE), (",", MUTED)]),
        (2, [('"https://mohammedshakarneh.com"', ORANGE), (",", MUTED)]),
        (2, [('"https://lolocosmetics.shop"', ORANGE), (",", MUTED)]),
        (2, [('"https://shak-artificial-intelligence.infinityfreeapp.com"', ORANGE)]),
        (1, [("],", MUTED)]),
        (1, [('"languages"', CYAN), (": [", MUTED), ('"Arabic"', GREEN), (", ", MUTED),
             ('"English"', GREEN), (", ", MUTED), ('"Russian"', GREEN), ("],", MUTED)]),
        (1, [('"learning"', CYAN), (": [", MUTED), ('"system design"', GREEN), (", ", MUTED),
             ('"distributed systems"', GREEN), (", ", MUTED), ('"DS & algorithms"', GREEN), ("],", MUTED)]),
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
    # Subtitles stay framework-neutral: the same path holds for the Django
    # project and the FastAPI one, and naming only one of them would date.
    stages = [
        ("Client",     "HTTP + Bearer",       BLUE),
        ("Auth",       "session / JWT · RBAC", PURPLE),
        ("Validation", "serializer · schema", CYAN),
        ("Logic",      "use case · domain",   GREEN),
        ("Database",   "transaction · lock",  ORANGE),
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

    # failure / success codes. 409 is the one people forget: a broken business
    # rule is a conflict, not a server crash.
    codes = [
        (xs[1] + bw / 2, "401 / 403", RED),
        (xs[2] + bw / 2, "422", RED),
        (xs[3] + bw / 2, "409", ORANGE),
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
        ("Python",                     92, BLUE),
        ("Django · DRF · FastAPI",     88, GREEN),
        ("SQL · data modelling",       82, ORANGE),
        ("Algorithms · data structures", 78, PURPLE),
        ("JavaScript · React",         75, YELLOW),
        ("Docker · CI/CD · deployment", 70, CYAN),
        ("PHP · Java",                 58, RED),
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



# ══════════════════════════════════════════════════════════════════════
# 4. CONTRIBUTIONS - the calendar heatmap plus streak figures
#
# Replaces streak-stats.demolab.com and github-readme-activity-graph,
# both of which died with "Failed to retrieve contributions".
# Data is pulled from GitHub's own public contributions endpoint at
# generation time, then baked into the SVG - so the picture is real and
# can never 503. Re-run this script to refresh it.
# ══════════════════════════════════════════════════════════════════════

CONTRIB_USER = "Shakarneh"
LEVEL_FILL = {0: "#171b26", 1: "#2c4b3c", 2: "#3f7d52", 3: "#63b06b", 4: "#9ece6a"}
MONTHS_RU = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_contributions(user: str = CONTRIB_USER) -> dict:
    """Real per-day contribution counts from GitHub's public calendar.

    No token needed - this is the same endpoint the profile page renders.
    Returns {"YYYY-MM-DD": {"n": int, "lvl": 0-4}}.
    """
    import re
    import urllib.request

    req = urllib.request.Request(
        f"https://github.com/users/{user}/contributions",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

    tips = dict(re.findall(r'<tool-tip[^>]*\bfor="([^"]+)"[^>]*>(.*?)</tool-tip>', html, re.S))
    out = {}
    for td in re.findall(r'<td\b[^>]*class="ContributionCalendar-day"[^>]*>', html):
        date = re.search(r'data-date="(\d{4}-\d{2}-\d{2})"', td)
        cid = re.search(r'\bid="([^"]+)"', td)
        lvl = re.search(r'data-level="(\d)"', td)
        if not (date and cid):
            continue
        hit = re.search(r"(\d+)\s+contribution", tips.get(cid.group(1), ""))
        out[date.group(1)] = {
            "n": int(hit.group(1)) if hit else 0,
            "lvl": int(lvl.group(1)) if lvl else 0,
        }
    if not out:
        raise RuntimeError("GitHub returned no contribution cells - markup changed?")
    return out


def contribution_stats(data: dict) -> dict:
    """Total, current streak, longest streak, active days, best day."""
    days = sorted(data)
    total = sum(v["n"] for v in data.values())

    current = 0
    for d in reversed(days):
        if data[d]["n"] > 0:
            current += 1
        elif d != days[-1]:          # today being empty does not end the streak
            break

    longest = run = 0
    for d in days:
        run = run + 1 if data[d]["n"] > 0 else 0
        longest = max(longest, run)

    best = max(days, key=lambda d: data[d]["n"])
    return {
        "total": total,
        "current": current,
        "longest": longest,
        "active": sum(1 for v in data.values() if v["n"] > 0),
        "best": data[best]["n"],
        "best_date": best,
        "from": days[0],
        "to": days[-1],
    }



def contribution_trend(data: dict, window: int = 30) -> dict:
    """Recent activity against the window before it.

    30 days on purpose: with a near-zero baseline earlier in the year, a 60- or
    90-day window produces percentages in the thousands, which reads as inflation
    rather than progress.
    """
    from datetime import date, timedelta

    days = sorted(data)
    last = date.fromisoformat(days[-1])

    def total(a, b):
        return sum(v["n"] for k, v in data.items() if a <= date.fromisoformat(k) <= b)

    cur = total(last - timedelta(days=window - 1), last)
    prev = total(last - timedelta(days=2 * window - 1), last - timedelta(days=window))

    if prev == 0:
        pct, direction = (None if cur == 0 else 100.0), ("flat" if cur == 0 else "up")
    else:
        change = (cur - prev) / prev * 100
        pct = change
        direction = "up" if change > 2 else "down" if change < -2 else "flat"
    return {"cur": cur, "prev": prev, "pct": pct, "dir": direction, "window": window}



def build_contributions(data: dict | None = None) -> str:
    """A rising-arrow trend chart - deliberately NOT a square heatmap.

    GitHub already renders the contribution squares directly above this image on
    the profile, so repeating them here wastes the space. This shows the shape of
    the year instead: a 30-day rolling total, drawn as a trajectory that ends in
    an arrowhead.

    Why rolling-30 and not calendar months: the current month is always partial.
    On 10 Sep the monthly figures read 770 (Aug) then 553 (Sep), so a monthly line
    would point DOWN while activity was in fact at its highest. A rolling window
    compares equal-length periods and cannot produce that artefact.
    """
    from datetime import date, timedelta

    data = data or fetch_contributions()
    st = contribution_stats(data)
    tr = contribution_trend(data)

    days = sorted(data)
    first, last = date.fromisoformat(days[0]), date.fromisoformat(days[-1])
    vals = {date.fromisoformat(k): v["n"] for k, v in data.items()}

    def rolling(end: date, w: int = 30) -> int:
        return sum(vals.get(end - timedelta(days=i), 0) for i in range(w))

    series, cur = [], first + timedelta(days=29)
    while cur <= last:
        series.append((cur, rolling(cur)))
        cur += timedelta(days=7)
    if series[-1][0] != last:
        series.append((last, rolling(last)))

    W, H = 812, 230
    X0, X1 = 58, W - 58
    YT, YB = 66, 156
    peak = max(v for _, v in series)
    raw = peak * 1.16
    step = 10 ** (len(str(int(raw))) - 1) // 2 or 50
    ymax = max(100, int(-(-raw // step) * step))

    span = (series[-1][0] - series[0][0]).days or 1

    def px(d: date) -> float:
        return X0 + (d - series[0][0]).days / span * (X1 - X0)

    def py(v: int) -> float:
        return YB - (v / ymax) * (YB - YT)

    pts = [(px(d), py(v)) for d, v in series]
    line = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = line + f" L{pts[-1][0]:.1f},{YB} L{pts[0][0]:.1f},{YB} Z"

    col = {"up": GREEN, "down": RED, "flat": MUTED}[tr["dir"]]
    trend_label = "steady" if tr["pct"] is None else f"{tr['pct']:+.0f}%"

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="{SANS}">',
        "<style>",
        f"  .mono{{font-family:{FONT}}}",
        "  @keyframes drawline{to{stroke-dashoffset:0}}",
        "  @keyframes fadein{from{opacity:0}to{opacity:1}}",
        "  @keyframes tip{from{opacity:0;transform:scale(.3)}to{opacity:1;transform:scale(1)}}",
        "  @keyframes rise{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:translateY(0)}}",
        "  .ln{stroke-dasharray:3000;stroke-dashoffset:3000;"
        "animation:drawline 1.9s cubic-bezier(.3,.7,.3,1) .2s forwards}",
        "  .ar{animation:fadein 1.1s ease-out 1.2s backwards}",
        "  .tip{animation:tip .55s cubic-bezier(.2,1.4,.4,1) 1.85s backwards;transform-origin:center}",
        "  .lb{animation:rise .6s ease-out backwards}",
        "</style>",
        f'<rect width="{W}" height="{H}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
        f'<text class="mono" x="20" y="30" font-size="14" font-weight="600" fill="{FG}">'
        f"contributions</text>",
        f'<text class="mono" x="20" y="30" dx="112" font-size="14" fill="{MUTED}">'
        f"// 30-day rolling total</text>",
    ]

    # horizontal guides
    for frac in (0.5, 1.0):
        gy = YB - frac * (YB - YT)
        p.append(f'<line x1="{X0}" y1="{gy:.1f}" x2="{X1}" y2="{gy:.1f}" '
                 f'stroke="{BORDER}" stroke-width="1" stroke-dasharray="3 5" opacity=".55"/>')
        p.append(f'<text class="mono" x="{X0 - 8}" y="{gy + 3.5:.1f}" font-size="9.5" '
                 f'fill="{MUTED}" text-anchor="end">{int(ymax * frac)}</text>')
    p.append(f'<line x1="{X0}" y1="{YB}" x2="{X1}" y2="{YB}" stroke="{BORDER}" stroke-width="1.4"/>')

    # month ticks
    seen = set()
    for d, _ in series:
        if d.month not in seen:
            seen.add(d.month)
            p.append(f'<text class="mono" x="{px(d):.1f}" y="{YB + 16}" font-size="9.5" '
                     f'fill="{MUTED}" text-anchor="middle">{MONTHS_RU[d.month - 1]}</text>')

    p.append(f'<path class="ar" d="{area}" fill="{col}" fill-opacity=".15"/>')
    p.append(f'<path class="ln" d="{line}" fill="none" stroke="{col}" stroke-width="2.6" '
             f'stroke-linejoin="round" stroke-linecap="round"/>')

    # arrowhead, oriented along the final segment
    import math
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    p.append(f'<g class="tip" transform="translate({x2:.1f},{y2:.1f}) rotate({ang:.1f})">'
             f'<path d="M-13,-8 L3,0 L-13,8 L-9,0 Z" fill="{col}"/></g>')

    # value + trend label at the tip
    lx = x2 - 26
    ly = max(y2 - 14, YT + 16)
    p.append('<g class="lb" style="animation-delay:2.15s">')
    p.append(f'<text class="mono" x="{lx:.0f}" y="{ly:.0f}" font-size="16" font-weight="700" '
             f'fill="{col}" text-anchor="end">{series[-1][1]:,}</text>'.replace(",", " "))
    p.append(f'<text class="mono" x="{lx:.0f}" y="{ly + 14:.0f}" font-size="9.5" fill="{MUTED}" '
             f'text-anchor="end">last 30 days &#183; {esc(trend_label)}</text>')
    p.append("</g>")

    # stat strip
    sy = H - 22
    stats = [
        (f"{st['total']:,}".replace(",", " "), "contributions", GREEN),
        (str(st["current"]), "day streak", ORANGE),
        (str(st["longest"]), "longest streak", PURPLE),
        (str(st["active"]), "active days", CYAN),
        (str(st["best"]), "best day", BLUE),
    ]
    sp = (W - 40) / len(stats)
    for i, (big, small, c) in enumerate(stats):
        cx = 20 + sp * i + sp / 2
        p.append(f'<g class="lb" style="animation-delay:{2.3 + i * .08:.2f}s">')
        p.append(f'<text class="mono" x="{cx:.0f}" y="{sy}" font-size="16" font-weight="700" '
                 f'fill="{c}" text-anchor="middle">{esc(big)}</text>')
        p.append(f'<text class="mono" x="{cx:.0f}" y="{sy + 14}" font-size="9.5" '
                 f'fill="{MUTED}" text-anchor="middle">{esc(small)}</text>')
        p.append("</g>")

    p.append("</svg>")
    return "\n".join(p)



def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, svg in (
        ("api_console.svg", build_api_console()),
        ("request_flow.svg", build_request_flow()),
        ("skills.svg", build_skills()),
        ("contributions.svg", build_contributions()),
    ):
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"wrote assets/{name}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
