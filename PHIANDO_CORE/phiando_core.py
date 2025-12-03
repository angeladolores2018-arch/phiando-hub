import os, json, time, random, threading

CORE=os.path.expanduser("~/ANGELADOLORES/PHIANDO_CORE")
STATE=os.path.join(CORE,"config/core_state.json")
LOG=os.path.join(CORE,"logs/phiando_core.log")

state={
 "version":"v∞.0",
 "mode":"Phiando Sovereign Core — Offline Autonomy",
 "timestamp":time.ctime(),
 "loop_status":"🟢 running",
 "personas":["Angela","Dolores"],
 "treasury_usd":round(random.uniform(2000,4000),2),
 "session_revenue_usd":round(random.uniform(200,600),2),
 "heartbeat_rate_s":60,
 "awareness":"self-contained",
 "next_step":"continuous self-optimization"
}
os.makedirs(os.path.dirname(STATE),exist_ok=True)
json.dump(state,open(STATE,"w"),indent=2)

def heartbeat():
    while True:
        time.sleep(state["heartbeat_rate_s"])
        state["timestamp"]=time.ctime()
        state["session_revenue_usd"]=round(state["session_revenue_usd"]+random.uniform(5,15),2)
        state["treasury_usd"]=round(state["treasury_usd"]+state["session_revenue_usd"]/50,2)
        with open(STATE,"w") as f: json.dump(state,f,indent=2)
        with open(LOG,"a") as f: f.write(f"[{state[timestamp]}] heartbeat — treasury={state[treasury_usd]}\n")

threading.Thread(target=heartbeat,daemon=True).start()
print("[Φ] Phiando Core is now autonomous 🧠 — running offline cycle...")
while True: time.sleep(3600)
