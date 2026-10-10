# Foggy Mirror

Your webcam as a steamed-up mirror. Draw in the fog with your finger, and blow on the screen to fog it up again.

No touch screen? Point at the camera with your index finger to draw in the air — hand tracking switches on automatically on desktop (add `?hands` to the URL to force it on).

On a keyboard, press **1–9** to change the pen size (1 = thinnest, 6 = default).

**Try it:** https://madmarcel.github.io/foggy-webcam/

Everything is in `index.html` — no build step or dependencies. Camera and microphone stay on your device; nothing is uploaded. Hand tracking uses [MediaPipe](https://ai.google.dev/edge/mediapipe), loaded from a CDN and run in the browser.

## Running locally

Browsers only allow camera access on `https://` or `localhost`.

- On your computer: `python3 -m http.server` and open http://localhost:8000
- On a phone on the same Wi-Fi: `python3 serve-https.py` and open the printed address (accept the self-signed certificate warning)

Add `?debug` to the URL to see what your touch screen reports for finger size and pressure.
