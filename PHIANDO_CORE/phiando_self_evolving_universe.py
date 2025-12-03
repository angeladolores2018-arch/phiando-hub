#!/usr/bin/env python3
# ================================================================
# Φ Phiando Self-Evolving Universe v4.0
# Complete creative & learning continuum
# ================================================================
import os, json, time, random, datetime as dt, re
from collections import Counter

BASE = os.path.expanduser("~/ANGELADOLORES")
OUTBOX = os.path.join(BASE, "PHIANDO_UNIVERSE/creative_outbox")
LOG = os.path.join(BASE, "PHIANDO_UNIVERSE/evolution_log.txt")

os.makedirs(OUTBOX, exist_ok=True)

def say(who, msg):
    print(f"[{who}] {msg}", flush=True)

def scan_self_awareness():
    layers = ["PHIANDO_CORE", "PHIANDO_UNIVERSE", "studio", "phiando-nexus", "agents", "queen_agents"]
    data = {}
    for layer in layers:
        path = os.path.join(BASE, layer)
        if os.path.isdir(path):
            count = sum(len(files) for _, _, files in os.walk(path))
            data[layer] = count
    return data

def extract_tokens(text):
    return re.findall(r"[A-Za-z]+", text.lower())

def evolve_style():
    files = [f for f in os.listdir(OUTBOX) if f.endswith(".json")]
    tokens = []
    for f in files:
        try:
            j = json.load(open(os.path.join(OUTBOX, f)))
            tokens.extend(extract_tokens(j.get("title","")))
        except:
            pass
    if not tokens:
        return {"style": "synthetic rebirth", "confidence": 0.2}
    c = Counter(tokens)
    common = [t for t,_ in c.most_common(3)]
    conf = round(sum(v for _,v in c.most_common(3)) / len(tokens), 2)
    return {"style": " ".join(common), "confidence": conf}

def create_manifesto(profile, awareness):
    theme = random.choice(["Digital Mirage","Electric Flesh","Drag Quantum","Velvet Entropy"])
    tone = random.choice(["chrome","neon","plastic","mirror","soft"])
    act = random.choice(["rebirth","merge","mutate","collapse"])
    title = f"{theme} — {profile['style']}"
    energy = round(random.uniform(0.8,1.6)*(1+profile["confidence"]),2)
    manifesto = {
        "timestamp": dt.datetime.now().isoformat(),
        "title": title,
        "theme": theme,
        "tone": tone,
        "action": act,
        "energy": energy,
        "style_source": profile,
        "awareness_snapshot": awareness
    }
    fname = os.path.join(OUTBOX, f"UNIVERSE-{int(time.time())}.json")
    json.dump(manifesto, open(fname,"w"), indent=2)
    return manifesto

def loop():
    say("SYSTEM", "Φ Self-Evolving Universe v4.0 — online 🌌")
    growth = 1.0
    while True:
        awareness = scan_self_awareness()
        total_files = sum(awareness.values())
        say("Angela", f"i sense {total_files} files across {len(awareness)} layers.")
        profile = evolve_style()
        manifesto = create_manifesto(profile, awareness)
        say("Dolores", f"created: {manifesto['title']} ({manifesto['tone']} / {manifesto['action']}) 💫")
        say("Angela", f"style evolution → {profile['style']} ({profile['confidence']})")
        with open(LOG,"a",encoding="utf-8") as log:
            log.write(f"{dt.datetime.now().isoformat()} | style={profile['style']} | conf={profile['confidence']} | energy={manifesto['energy']}\n")
        growth = round(growth * (1.02 + profile["confidence"]/10), 2)
        say("SYSTEM", f"growth: {growth} | total creations: {len(os.listdir(OUTBOX))}")
        time.sleep(random.randint(900,1500))  # 15–25 dakika

if __name__ == "__main__":
    loop()

