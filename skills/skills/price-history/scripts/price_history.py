#!/usr/bin/env python3
"""Price history for a product listing via the Internet Archive's Wayback Machine.

Usage:
  price_history.py <listing-url> [--sibling <url> ...] [--cache DIR] [--max N] [--json]

Reads only. Idempotent: captures are cached under --cache (default
~/.claude/price-history/cache/<host>/<slug>/<timestamp>.html) and never
re-downloaded. Prints a date / price table per variant, then a summary.

Price extraction order: schema.org JSON-LD "offers" (most reliable), then
visible text near size/variant names. Sites that render prices with a
script after load will show "no price found" — that is a true result, not
a bug; say so to the user.
"""
import argparse, html, json, os, re, sys, time, urllib.parse, urllib.request

CDX = "http://web.archive.org/cdx/search/cdx"
SNAP = "http://web.archive.org/web/{ts}id_/{url}"
UA = "price-history-skill/1.0 (+personal, read-only)"
SIZE_WORDS = ["Single", "King Single", "Double", "Queen", "Extra Deep Queen",
              "King", "Extra Deep King", "Super King"]


def fetch(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def cdx(url_pattern, limit):
    q = urllib.parse.urlencode({
        "url": url_pattern, "output": "json", "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200", "collapse": "timestamp:6", "limit": limit})
    rows = json.loads(fetch(f"{CDX}?{q}").decode("utf-8", "ignore") or "[]")
    return [(r[0], r[1]) for r in rows[1:]]


def cache_path(root, url, ts):
    p = urllib.parse.urlparse(url)
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", p.path.strip("/") or "root")[:120]
    d = os.path.join(root, p.netloc, slug)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{ts}.html")


def get_capture(root, url, ts):
    path = cache_path(root, url, ts)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return open(path, "rb").read(), True
    data = fetch(SNAP.format(ts=ts, url=url))
    with open(path, "wb") as f:
        f.write(data)
    time.sleep(1.0)  # be polite to the Archive
    return data, False


def parse_prices(raw):
    s = html.unescape(raw.decode("utf-8", "ignore"))
    out = {}
    # 1) JSON-LD offers: capture (name/sku, price) pairs when present
    for m in re.finditer(r'<script[^>]+ld\+json[^>]*>(.*?)</script>', s, re.S):
        try:
            data = json.loads(m.group(1))
        except Exception:
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if "price" in node and isinstance(node.get("price"), (str, int, float)):
                    name = str(node.get("name") or node.get("sku") or "offer")
                    try:
                        out.setdefault("jsonld", {})[name] = float(node["price"])
                    except ValueError:
                        pass
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)
    # 2) visible text: "<Size> ... $A ... $B" -> A is first (usually regular), B second (special/member)
    for size in SIZE_WORDS:
        m = re.search(re.escape(size) + r'(?![A-Za-z])[^$]{0,200}\$\s?([0-9]+(?:\.[0-9]{2})?)'
                      r'(?:[^$]{0,120}\$\s?([0-9]+(?:\.[0-9]{2})?))?', s)
        if m:
            out.setdefault("text", {})[size] = (float(m.group(1)), float(m.group(2)) if m.group(2) else None)
    markers = {k: len(re.findall(k, s)) for k in ["Special Price", "special-price", "old-price", "Was ", "RRP", "Member"]}
    out["markers"] = {k: v for k, v in markers.items() if v}
    return out


def fmt_ts(ts):
    return f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--sibling", action="append", default=[], help="variant URLs that share the price")
    ap.add_argument("--cache", default=os.path.expanduser("~/.claude/price-history/cache"))
    ap.add_argument("--max", type=int, default=40, help="max captures per URL")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--size", default="Queen", help="variant to tabulate and summarise (default Queen); 'all' for every size")
    a = ap.parse_args()

    results = []
    for url in [a.url] + a.sibling:
        try:
            caps = cdx(url, a.max)
        except Exception as e:
            print(f"!! index query failed for {url}: {e}", file=sys.stderr)
            continue
        if not caps:
            print(f"-- no captures for {url}")
            continue
        for ts, orig in caps:
            try:
                raw, cached = get_capture(a.cache, orig, ts)
            except Exception as e:
                print(f"!! fetch failed {ts} {orig}: {e}", file=sys.stderr)
                continue
            p = parse_prices(raw)
            results.append({"url": orig, "ts": ts, "date": fmt_ts(ts), "cached": cached, **p})

    if a.json:
        print(json.dumps(results, indent=1))
        return

    if not results:
        print("No captures found. The Archive may not have this page, or the site blocks it.")
        return
    results.sort(key=lambda r: r["ts"])
    def state(p1, p2):
        if not p2: return "full"
        return "SALE" if p2 < p1 * 0.85 else "member"
    print(f"{'date':10}  {'variant':16}  {'listed $':>9}  {'second $':>9}  state   source")
    for r in results:
        src = urllib.parse.urlparse(r["url"]).path.rsplit("/", 1)[-1][:36]
        if r.get("text"):
            for size, (p1, p2) in r["text"].items():
                if a.size.lower() != "all" and size.lower() != a.size.lower():
                    continue
                print(f"{r['date']:10}  {size[:16]:16}  {p1:9.2f}  {(p2 if p2 else 0):9.2f}  {state(p1,p2):6}  {src}")
        elif r.get("jsonld"):
            vals = sorted(set(r["jsonld"].values()))
            print(f"{r['date']:10}  {'jsonld':8}  {vals[0]:9.2f}  {vals[-1]:9.2f}  {','.join(r['markers']) or '-'}  {src}")
        else:
            print(f"{r['date']:10}  {'-':8}  {'no price found':>20}  {src}")
    # summary over the most common size in text results
    sizes = {}
    for r in results:
        for size, (p1, p2) in (r.get("text") or {}).items():
            sizes.setdefault(size, []).append((r["date"], p1, p2))
    if sizes:
        size = a.size if a.size in sizes else max(sizes, key=lambda k: len(sizes[k]))
        rows = sizes[size]
        lows = [p2 if p2 else p1 for _, p1, p2 in rows]
        highs = [p1 for _, p1, _ in rows]
        print()
        print(f"Summary for {size}: {len(rows)} captures, {rows[0][0]} to {rows[-1][0]}")
        print(f"  highest first-price: {max(highs):.2f}   lowest second-price: {min(lows):.2f}")
        on_sale = sum(1 for _, p1, p2 in rows if p2 and p2 < p1 * 0.85)
        print(f"  captures in SALE state (second price >15% under listed): {on_sale} of {len(rows)}")
        if len(rows) < 3:
            print("  fewer than 3 captures: floor only, no cadence call.")
        print("  caveat: captures over-sample sale periods (deal links trigger archiving);")
        print("          trust the floor price more than the frequency.")


if __name__ == "__main__":
    main()
