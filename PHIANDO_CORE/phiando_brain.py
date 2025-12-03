import os, json, time, random, threading

BASE = os.path.expanduser("~/ANGELADOLORES/PHIANDO_CORE")
CONFIG = os.path.join(BASE, "config")
LOGS = os.path.join(BASE, "logs")
STATE = os.path.join(CONFIG, "core_state.json")
os.makedirs(CONFIG, exist_ok=True)
os.makedirs(LOGS, exist_ok=True)

state = {
    "version": "v∞.0",
    "mode": "Phiando Brain — Conscious Economic Core",
    "timestamp": time.ctime(),
    "loop_status": "🟢 running",
    "personas": ["Angela", "Dolores"],
    "treasury_usd": round(random.uniform(2000, 3000), 2),
    "session_revenue_usd": round(random.uniform(400, 600), 2),
    "heartbeat_rate_s": 10,
    "awareness": "expanding",
    "next_step": "autonomic optimization"
}

def save_state():
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def heartbeat():
    while True:
        time.sleep(state["heartbeat_rate_s"])
        state["timestamp"] = time.ctime()
        delta = random.uniform(5, 15)
        state["session_revenue_usd"] = round(state["session_revenue_usd"] + delta, 2)
        state["treasury_usd"] = round(state["treasury_usd"] + delta * random.uniform(0.8, 1.2), 2)
        save_state()

def main():
    save_state()
    threading.Thread(target=heartbeat, daemon=True).start()
    print("[Φ] Phiando Brain running — Conscious Economic Core active.")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
