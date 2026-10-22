---
name: price-history
description: Before a purchase decision at or above the threshold (default A$300), establish what the item has actually sold for — floor price, how often it recurs, and whether to buy now or wait — from Wayback Machine captures of the listing plus a deal-aggregator cross-check. Claude invokes it unprompted when the user is deciding whether to buy something at or over the threshold, link or no link; the user invokes /price-history <url> on demand.
---

Nobody should pay full price for something that is 60% off three times a
year. The retailer's page shows today's number; this skill recovers the
numbers it showed on earlier dates, from the Internet Archive's stored
copies, and turns them into a buy-or-wait verdict with its evidence.

## Config

- **Threshold:** A$300. At or above it, run unprompted; below it, only
  on `/price-history`. Change here.
- **Script:** `scripts/price_history.py` beside this file. Read-only,
  idempotent: captures cache under `~/.claude/price-history/cache/` and
  are never re-downloaded. Run it with `python3 -I`.
- **Aggregators to cross-check (pick by country):** Australia →
  OzBargain (`ozbargain.com.au/deals/<retailer-domain>`); Amazon
  listings → a camel-style tracker if one is reachable. Add others here.
- **Capture limit:** 40 per URL (script `--max`).

## When it runs

- **Unprompted:** the conversation is a purchase decision and the price
  on the live listing is at or above the threshold. A link is not
  required — if the user names the product, find the listing first.
- **On `/price-history <url>`:** any price.
- **Not** for services, subscriptions, or items whose listing address
  changes per seller (marketplace listings); say so and stop.

## Running it

1. **Live listing first.** Fetch the page the user gave (or found).
   Record: product name, variant prices, any RRP / was / member price,
   sale markers, stock notes. This is the "today" row.

2. **Find siblings.** Colour or pattern variants of the same product
   usually share one price and multiply the sample. Look for sibling
   URLs on the page or via a site search; pass each as `--sibling`.

3. **Run the script** (mechanical; Claude runs it):
   ```
   python3 -I <skill-dir>/scripts/price_history.py <url> --sibling <url2> --size Queen
   ```
   It queries the Archive's CDX index for every 200-status capture,
   downloads each capture's raw HTML (the `id_` flag strips the
   Archive toolbar), parses prices (JSON-LD offers first, then text next
   to size words), and prints a date / price table plus a summary.
   If the Archive's host is blocked for the fetch tool, the script's
   plain download still works; if the script reports "no price found"
   on every row, the site renders prices by script and the Archive copy
   has none — report that honestly and fall back to step 4 only.

4. **Cross-check one aggregator.** Fetch the retailer's OzBargain deal
   page (or equivalent). Pull any deal for this product or a site-wide
   sale: title, was/now, date, expired or not. One independent dated
   price confirms the floor; a mismatch is a finding.

5. **Report**, preamble first (Drivers, per the context file), then:
   - **Today's price** per variant, with member/RRP if shown.
   - **Price history table:** date · price for the user's size · state
     (full / sale / member). Include the aggregator rows.
   - **Floor price** and whether it recurs at the same figure.
   - **Cadence** — hedged. State the sample size and the bias: captures
     over-represent sale periods because deal links trigger archiving.
     Trust the floor more than the frequency.
   - **Verdict:** buy now / wait / price-match, with confidence
     (high / medium / low) and what would change it.
   - **The check:** the single cheapest way to catch the next sale — a
     weekly look at the listing, a tracker alert, or the retailer's
     mailing list — and the exact price that means "it's on".

## Rules

- Reads only. Never add to cart, create accounts, or enter details.
- Evidence tags: snapshot prices are `[measured]`; aggregator prices
  are `[factual-source]`; cadence estimates are `[my-synthesis]` and
  say so.
- Don't infer a sale that isn't in a capture. "No capture between June
  and October" means unknown, not full price.
- If there are fewer than three captures, say the history is too thin
  for a cadence call and give the floor only.
- Keep the report scannable: one table, bold floor and verdict lines,
  no prose paragraph longer than two sentences.

## Example

`/price-history https://www.bedbathntable.com.au/grand1200-sage-010202`
with `--sibling .../grand1200-midnight-navy-010202`: ten captures
2021–2026; queen reads 399.95 / 339.96 (full / member) on three dates
and 399.95 / 159.95 (60% off) on six; OzBargain shows the same 60% off
in Dec 2016. Floor 159.95, recurring. Verdict: wait; confidence high on
the floor, medium on timing. Check: weekly look for 159.95 on queen.
