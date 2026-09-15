# Snack Route

A phone-only, offline-first PWA for building a twice-weekly DSD snack order
across seven stores and combining it into one master list for keying into OTS.

- `index.html` — the whole app (HTML, CSS, JS)
- `sw.js` — cache-first service worker (bump `CACHE` on every change)
- `manifest.webmanifest`, `icon-192.png`, `icon-512.png`
- `tools/make-icons.py` — regenerates the icons (stdlib only)

## Run locally

```bash
python3 -m http.server 8787
```

Open http://localhost:8787 in Chrome. To install on an Android phone, serve it
over https (or use `chrome://inspect` port forwarding to `localhost`) and use
Chrome's "Install app" / "Add to Home screen".

## Data

Everything is in `localStorage` under `snackroute.v1`. Setup → Backup exports
and imports a JSON file. There is no server and no sync.
