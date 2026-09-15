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

## UX invariants

- The quick-add `<input>` is never re-created or re-rendered — only the list
  repaints. Re-rendering the input closes the Android keyboard.
- Buttons `preventDefault` on pointerdown/mousedown so tapping them never steals
  focus from the quick-add input (which would close the keyboard).
- Sheet swipe = horizontal drag on the pane (touch-action: pan-y, pointer
  events, axis lock). Row-clear swipe = horizontal drag that *starts on the
  −/qty/+ cluster* of a row that's on the order. This is how the two horizontal
  gestures coexist.
- Suggestion strip above the input has a fixed height so the list never shifts.
- Respect `prefers-reduced-motion`.

## Cutoffs

Tue 07:30 America/New_York → Thursday pickup. Sat 07:30 → Tuesday pickup.
Offsets are probed with `Intl.DateTimeFormat`, never hardcoded.

## Service worker

Cache-first, app shell precached. **Bump `CACHE` in `sw.js` whenever any file
changes.**

## Testing

Serve with `python3 -m http.server 8787` (see `.claude/launch.json`) and test at
380px wide.
