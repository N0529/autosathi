# How to contribute to AutoSathi

Thanks for wanting to help! The most valuable thing you can do is **add a route you use daily**. No coding experience needed.

---

## Adding a new route (no coding needed)

### Step 1 — Check if the route already exists
Browse the `/routes/pune/` folder. If your route isn't there, continue.

### Step 2 — Copy the template
Open `routes/TEMPLATE.json` and copy its contents.

### Step 3 — Fill in your route
You need:
- **Stop names** — the common names people actually use, not official ones
- **Landmarks** — what's near each stop (a temple, a station, a building)
- **Fares** — what you actually pay between each pair of stops
- **Coordinates** — open Google Maps, right-click any stop location, copy the lat/long

### Step 4 — Name your file
Use this format: `from-area-to-area.json`
Example: `wakad-hinjewadi.json`

### Step 5 — Submit a Pull Request
- Fork this repo
- Add your file to `/routes/pune/`
- Submit a PR with the title: `Add route: From Area → To Area`

That's it. Someone will review and merge it.

---

## How fares work

Fares are per **boarding segment**, not per kilometre. List every pair of stops that has a different fare.

Example for a 3-stop route:
```json
"fares": [
  { "from_stop": 1, "to_stop": 2, "amount_rupees": 10 },
  { "from_stop": 1, "to_stop": 3, "amount_rupees": 15 },
  { "from_stop": 2, "to_stop": 3, "amount_rupees": 10 }
]
```

---

## How to find coordinates

1. Open [Google Maps](https://maps.google.com)
2. Find the stop location
3. Right-click → "What's here?"
4. Copy the numbers shown (latitude, longitude)

---

## Verifying existing routes

If you ride a route and notice a stop name is wrong, a fare has changed, or a stop no longer exists — please open an Issue with the title `Update route: route-name` and describe what changed.

---

## Questions?

Open an Issue and we'll help you out.
