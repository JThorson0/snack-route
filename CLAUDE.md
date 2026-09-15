# Snack Route — project rules

Phone-only PWA for a DSD snack delivery route. Vanilla HTML/CSS/JS in a single
`index.html` + `sw.js` + `manifest.webmanifest` + icons. No framework, no build
step, no bundler, no CDN, no webfonts. All data in `localStorage` under
`snackroute.v1`. Nothing leaves the phone.

## Hard rules (do not break)

1. The app never submits an order. It prepares numbers; the user keys them into
   OTS by hand. Never automate or suggest automating OTS.
2. Rollover (current → previous, current reset) is manual and two-tap
   (button + confirm). Never on a timer, never at cutoff, never as a side effect.
   Must be undoable.
3. Item numbers are strings. `080060` ≠ `80060`. Never `parseInt`/`Number` them,
   never sort numerically, never strip leading zeros — display, copy, or storage.
4. Never merge line items by item number. Two products share `29680`. Group by
   product `id` only, including master totals.
5. Never hide the previous order. Both quantities live on the same row, always.
   Never require browsing to add an item.
6. **Bold / accent = the latest (current) order.** Dim = the order already
   placed. Any doc that says otherwise is wrong.

## Visual direction (user's call, 2026-09-15)

Bold & colorful on black, Cash-App style: flat saturated blocks, huge numerals,
900-weight type, pill buttons. **Each store has its own color** (`store.color`,
picked in Setup) that floods that store's header, chip, "this order" capsule, the
composer send button, and its pill in the master list. Neutral white = primary
action, green `--go` = "cases"/go, amber `--warn` = next cutoff. This supersedes the
original "one accent color" line in the spec — the user asked for it.

## UX invariants

- The quick-add `<input>` is never re-created or re-rendered — only the list
  repaints. Re-rendering the input closes the Android keyboard.
- Buttons `preventDefault` on pointerdown/mousedown so tapping them never steals
  focus from the quick-add input (which would close the keyboard).
- Sheet swipe = horizontal drag on the pane (touch-action: pan-y, pointer
  events, axis lock). Swipe **left on a row that's on the order** clears that row
  (undoable); swipe right anywhere, or left on the header/empty space/off-order
  rows, switches store. Master rows swipe left to drop a product from every
  store. Header trash buttons clear a store / the whole order — always confirm
  sheet + Undo toast, and never touch the previous order.
- Suggestion strip above the input has a fixed height so the list never shifts.
- Respect `prefers-reduced-motion`.

## Catalog

Seeded from "Order Pick Sheets (Updated 1/1/25)" (Snyders-Lance, Orlando) — 174
products, 20 categories, in `SEED_PRODUCTS` as `[name, item, aliases, category,
desc]`. `CATALOG_VERSION` in index.html: bumping it makes every phone reset to a
fresh seed on next load (stores, catalog, **both orders** wiped) — only do that
when the user asks for a full reset. Item `29680` is intentionally on two
products. User's own shorthand names (Lance Ccc, Pbh, Tc Cheddar, 100 camp 20, …)
are kept as product names; the pick-sheet text lives in `desc` and is searchable.

## Cutoffs

Tue 07:30 America/New_York → Thursday pickup. Sat 07:30 → Tuesday pickup.
Offsets are probed with `Intl.DateTimeFormat`, never hardcoded.

## Service worker

Cache-first, app shell precached. **Bump `CACHE` in `sw.js` whenever any file
changes.**

## Hosting

GitHub Pages from `main` at https://jthorson0.github.io/snack-route/ (repo
JThorson0/snack-route). `git push origin main` deploys.

## Testing

Serve with `python3 -m http.server 8787` (see `.claude/launch.json`) and test at
380px wide.
