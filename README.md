# 🌌 Celestial Clock

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![API](https://img.shields.io/badge/API-NASA%20NeoWs-lightgrey.svg)]()

> A minimal CLI tool that uses real asteroid data to decide how seriously you should take your day.
>
>A Dashboard type interface minimal and aesthetic.
---

##  Overview

**Celestial Clock** pulls live Near-Earth Object (NEO) data from NASA and converts it into a simple daily signal:

* 🟢 *Everything is fine — go work*
* 🟡 *Space is active — take it easy*
* 🔴 *Potentially hazardous — abandon responsibility*

It’s fast, lightweight, and intentionally simple.

---
---

## 🤖 Parts Made with Ai
- UI
- Minor Improvements to the core
---
## 🚀 Features

* Real-time asteroid data via NASA NeoWs
* Urgency levels based on:

  * distance (Lunar Distance)
  * size (meters)
  * hazard classification
* Color-coded terminal output
* ASCII urgency meter
* Daily caching (no unnecessary API calls)
* Dynamic message generation (non-repetitive)
* `--refresh` flag for manual override

---

## 📦 Installation

```bash
git clone https://github.com/your-username/celestial-clock.git
cd celestial-clock
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the root directory:

```env
NASA_API_KEY=your_api_key_here
```

Get a free API key from: https://api.nasa.gov

If omitted, the app falls back to `DEMO_KEY` (rate-limited).

---

## ▶️ Usage

### Default (uses cache if available)

```bash
python main.py
```

### Force fresh API data

```bash
python main.py --refresh
```

---

## 🖥️ Example Output

```
=== CELESTIAL CLOCK ===
----------------------------------------
Asteroids Today  : 18
Closest Distance : 6.12 LD
Largest Size     : 520.44 m
Hazardous        : No

URGENCY
[■■■■■■□□□□] Level 2

VERDICT
The universe is busy. You don’t have to be.
----------------------------------------
```

---

## 🧠 Logic

| Level | Condition                              |
| ----- | -------------------------------------- |
| 🔴 3  | Potentially hazardous asteroid present |
| 🟡 2  | Distance < 10 LD OR Diameter > 500m    |
| 🟢 1  | Otherwise calm                         |

Messages are randomly selected within each level to avoid repetition.

---

## 📁 Project Structure

```
celestial_clock/
│
├── main.py      # CLI interface
├── core.py      # data + logic
├── config.py    # environment setup
│
├── cache/       # daily cached responses
├── .env         # API key (ignored)
└── requirements.txt
```

---

## ⚙️ Behavior Notes

* Cache is stored per day (`cache/YYYY-MM-DD.json`)
* App works offline if cached data exists
* No background processes — runs on demand
* Designed to be fast (<1s with cache)

---

## 🔮 FOR CONTRIBUTERS(U CAN ADD)

* `--quiet` mode (minimal output)
* JSON output for scripting
* historical trend tracking
* simple web dashboard

---

## 📜 License

MIT

---

## ☄️ Philosophy

> If space is calm, you have no excuse.
>
> If space is chaotic, neither do you — but at least it feels justified.
