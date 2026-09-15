# Snack Route

A phone-only, offline-first PWA for building a twice-weekly DSD snack order
across seven stores and combining it into one master list for keying into OTS.

- `index.html` — the whole app (HTML, CSS, JS)
- `sw.js` — cache-first service worker (bump `CACHE` on every change)
- `manifest.webmanifest`, `icon-192.png`, `icon-512.png`
- `tools/make-icons.py` — regenerates the icons (stdlib only)

## Live

**https://jthorson0.github.io/snack-route/** — served by GitHub Pages from the
`main` branch of https://github.com/JThorson0/snack-route. Every push to `main`
redeploys in about a minute. Open it in Chrome on the phone and choose
"Add to Home screen" / "Install app".

## Demo data

Open `https://jthorson0.github.io/snack-route/?demo` once to load a realistic
"last order submitted and rolled over" state across all seven stores. Setup →
Reset clears it.

## Run locally

```bash
python3 -m http.server 8787
```

Open http://localhost:8787 in Chrome.

## Data

Everything is in `localStorage` under `snackroute.v1` and works offline. Setup →
Backup exports/imports a JSON file. Setup → Cloud sync (optional) mirrors the
data to Firestore (project `snack-route-jt`, rules in `firestore.rules`) under a
private sync key so it can be opened on another device via a `?join=KEY` link.
