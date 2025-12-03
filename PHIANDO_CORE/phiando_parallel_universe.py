#!/usr/bin/env python3
import threading, time, random, json, os, datetime

STATE = {
    "treasury_usd": 1200.0,
    "session_revenue_usd": 0.0,
    "ideas": [],
    "mode": "Φ Parallel Universe v∞",
    "timestamp": ""
}
LOCK = threading.Lock()
STATE_PATH = os.path.expanduser("~/ANGELADOLORES/.phiando/state_parallel.json")

def save_state():
    with LOCK:
        STATE["timestamp"] = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        json.dump(STATE, open(STATE_PATH, "w"), indent=2)

def angela():
    while True:
        idea = random.choice(["digital rebirth", "synthetic poem", "holographic code", "sonic sculpture"])
        with LOCK:
            STATE["ideas"].append(idea)
        print(f"[Angela] created idea → {idea}")
        save_state()
        time.sleep(random.randint(20, 40))

def dolores():
    while True:
        with LOCK:
            if STATE["ideas"]:
                item = STATE["ideas"].pop(0)
                gain = random.uniform(10, 40)
                STATE["session_revenue_usd"] += gain
                print(f"[Dolores] marketed {item} → +")
        save_state()
        time.sleep(random.randint(30, 50))

def phiando_core():
    while True:
        with LOCK:
            growth = random.uniform(1.02, 1.08)
            STATE["treasury_usd"] *= growth
            print(f"[Phiando] treasury growth → {STATE[treasury_usd]:.2f} USD")
        save_state()
        time.sleep(60)

if __name__ == "__main__":
    print("Φ Parallel Universe — running 🪐")
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    threading.Thread(target=angela, daemon=True).start()
    threading.Thread(target=dolores, daemon=True).start()
    threading.Thread(target=phiando_core, daemon=True).start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nΦ Universe paused by user.")
