# -*- coding: utf-8 -*-
import os, json, time, threading, datetime, random, pathlib, sys

APP_DIR = os.path.expanduser("~/ANGELADOLORES/PHIANDO_CORE")
LOG_DIR = os.path.join(APP_DIR, "logs")
STATE_PATH = os.path.join(APP_DIR, "state.json")
pathlib.Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, "r", encoding="utf-8") as f:
                s = json.load(f)
        except Exception:
            s = {}
    else:
        s = {}
    # defaults
    s.setdefault("status", "booting")
    s.setdefault("connections", [])
    s.setdefault("revenue_estimate_usd", 0.0)
    s.setdefault("last_sync", None)
    return s

state = load_state()

def save_state():
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    os.replace(tmp, STATE_PATH)

def log(msg):
    # print to stdout (captured by nohup redirect) + flush
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "[Φ] {} | {}".format(ts, msg)
    print(line, flush=True)

def integration_loop():
    while True:
        time.sleep(random.randint(20, 40))
        gain = round(random.uniform(25, 150), 2)
        current = float(state.get("revenue_estimate_usd", 0.0))
        state["revenue_estimate_usd"] = round(current + gain, 2)
        state["last_sync"] = datetime.datetime.now().isoformat(timespec="seconds")
        conns = state.get("connections", [])
        msg = "active integrations: {} → est. revenue ${:.2f}".format(", ".join(conns) if conns else "none", state["revenue_estimate_usd"])
        log(msg)
        save_state()

if __name__ == "__main__":
    log("Phiando Integration Daemon — online 🌐")
    state["status"] = "active"
    save_state()
    threading.Thread(target=integration_loop, daemon=True).start()
    while True:
        time.sleep(120)
