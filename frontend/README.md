# Property Manager — Frontend

React + Vite + Tailwind PWA. Works in any modern browser (Windows desktop,
Android phone, iPhone) and can be installed to the home screen.

Designed to later be wrapped with **Capacitor** for Google Play and Apple
App Store distribution without rewriting the UI.

## Run locally

In one terminal — Django API:

```bash
# from repo root
python manage.py runserver 0.0.0.0:8000
```

In another terminal — frontend dev server:

```bash
cd frontend
npm install
npm run dev -- --host
```

Vite proxies `/api` and `/media` to Django, so the frontend uses
`/api/v1/...` paths and Vite forwards them. No CORS issues in dev.

- On the laptop: open `http://localhost:5173`
- On your phone (same Wi-Fi): Vite prints a `Network:` URL like
  `http://192.168.1.42:5173` — open that on your phone

## Install as PWA

In Chrome (Android) or Edge/Chrome (Windows), open the site, then
**three-dot menu → Install app**. It shows up as an icon like a native app.

## Build for production

```bash
npm run build         # outputs dist/
npm run preview -- --host    # serves dist/ on a port for testing
```

You can serve `dist/` from any static host (Netlify, Vercel, S3, nginx).
For a single-server setup, you can also have Django serve `dist/` via
`whitenoise` — not wired up here yet.

## Path to Google Play / Apple App Store (later)

When you're ready to ship a real app:

```bash
cd frontend
npm install -D @capacitor/cli @capacitor/core @capacitor/android @capacitor/ios
npx cap init "Property Manager" "com.yourname.property" --web-dir dist
npm run build
npx cap add android
npx cap add ios
npx cap sync
npx cap open android   # opens Android Studio → build APK / AAB → Play Store
npx cap open ios       # opens Xcode → archive → App Store Connect
```

Capacitor wraps the existing PWA in a native shell, gives you access to
camera/storage APIs, and produces installable bundles for both stores.
**You don't rewrite any UI code** — the React app inside the wrapper is
the same one that runs in the browser.

For native camera in Capacitor builds, swap the file `<input>` for
`@capacitor/camera`'s `Camera.getPhoto()`. That's the only file-system
API the current code uses.

## API base URL

In dev, Vite proxies to Django at `127.0.0.1:8000`. In production builds
(including Capacitor mobile bundles), set `VITE_API_BASE` to your hosted
API URL:

```bash
VITE_API_BASE=https://api.yourdomain.com/api/v1 npm run build
```

## What's wired up

Working: Dashboard (stats + tax-year card), Properties (list + create + detail
with photo upload), Tenants (list + create + detail), Leases (list), Rent
invoices (list), Expenses (list), Taxes (year-picker summary).

Read-only stubs (use admin to add data): leases creation, rent payment
logging, expense creation, document uploads on tenants. Adding these is a
straight repeat of the Properties create-form pattern.
