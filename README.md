[README.md](https://github.com/user-attachments/files/26871040/README.md)
# autosathi
Community map of shared auto routes, stops &amp; fares in Pune — built by daily riders, for daily riders 🛺
# AutoSathi 🛺

**A community-built guide to shared autos in Pune.**

Shared autos are the cheapest way to get around Pune — but if you're new to an area, you have no idea which routes exist, where to board, or what the fare is. AutoSathi fixes that.

No drivers involved. No booking. Just **routes, fares, and wait times** — contributed by daily riders, for daily riders.

---

## What it does

- 🗺️ Shows shared auto routes on a map
- 💰 Tells you the fare between any two stops on a route
- ⏱️ Shows how long the auto typically takes to fill up at a stop (by time of day)
- 📍 Works for middle stops too — know if autos tend to pass full at your stop

---

## Routes available

| City | Routes |
|------|--------|
| Pune | 1 (growing) |

See `/routes/pune/` for all route files.

---

## Contributing

The best way to help is to **add a route you know**.

👉 Read [CONTRIBUTING.md](./CONTRIBUTING.md) — no coding needed, just local knowledge.

---

## Running locally

```bash
# Clone the repo
git clone https://github.com/yourusername/autosathi.git
cd autosathi

# Install Python dependencies
pip install fastapi uvicorn

# Start the backend
python scripts/server.py

# Open index.html in your browser
```

---

## Tech stack

- **Frontend** — HTML, CSS, Vanilla JS, Leaflet.js (OpenStreetMap)
- **Backend** — Python + FastAPI
- **Data** — Plain JSON files (one per route, human-readable)
- **Database** — Supabase (PostgreSQL)

---

## License

MIT — free to use, fork, and build on.

---

## Why this exists

> "I moved to a new area in Pune and had no idea which autos to catch or what they cost. Ola and Uber were too expensive as a student. I asked around and found that locals just know these routes — but that knowledge lives nowhere online."

If you've felt this, this app is for you. And if you know your local routes, please add them.
