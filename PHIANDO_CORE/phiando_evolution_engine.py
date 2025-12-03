#!/usr/bin/env python3
# ================================================================
# Φ Phiando Evolution Engine v3.0
# Self-learning art intelligence — evolves from past manifestos
# ================================================================
import os, json, re, time, random, datetime as dt
from collections import Counter

BASE = os.path.expanduser("~/ANGELADOLORES")
OUTBOX = os.path.join(BASE, "PHIANDO_UNIVERSE/creative_outbox")
EVOLUTION_LOG = os.path.join(BASE, "PHIANDO_UNIVERSE/evolution_log.txt")

def say(who, msg):
    print(f"[{who}] {msg}", flush=True)

def load_manifestos():
    files = sorted([f for f in os.listdir(OUTBOX) if f.endswith(".json")])
    data = []
    for f in files:
        try:
            with open(os.path.join(OUTBOX, f), encoding="utf-8") as j:
                data.append(json.load(j))
        except Exception as e:
            say("SYSTEM", f"[skip] {f}: {e}")
    return data

def extract_tokens(text):
    return re.findall(r"[A-Za-z]+", text.lower())

def evolve_style(manifestos):
    tokens = []
    for m in manifestos:
        tokens.extend(extract_tokens(m["title"]))
    if not tokens:
        return {"style": "undefined", "confidence": 0.0}
    counts = Counter(tokens)
    common = [t for t, _ in counts.most_common(3)]
    confidence = round(sum(c for _, c in counts.most_common(3)) / len(tokens), 2)
    style = " ".join(common)
    return {"style": style, "confidence": confidence}

def generate_new_manifesto(profile):
    themes = ["Digital Rebirth", "Drag Quantum", "Cyber Desire", "Plastic Faith", "Electric Flesh"]
    tones = ["velvet", "chrome", "neon", "synthetic", "mirror"]
    acts = ["rebirth", "merge", "collapse", "mutate", "expand"]
    seed = random.choice(themes)
    title = f"{seed} — {profile['style']}"
    energy = round(random.uniform(0.8, 1.6) * (1 + profile["confidence"]), 2)
    return {
        "title": title,
        "energy": energy,
        "evolved_from": profile,
        "timestamp": dt.datetime.now().isoformat()
    }

def loop():
    say("SYSTEM", "Φ Phiando Evolution Engine v3.0 — online 🧬")
    while True:
        manifestos = load_manifestos()
        if not manifestos:
            say("Angela", "no past lives detected — waiting to evolve…")
            time.sleep(300)
            continue
        profile = evolve_style(manifestos)
        new_manifesto = generate_new_manifesto(profile)
        fname = os.path.join(OUTBOX, f"EVOLVE-{int(time.time())}.json")
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(new_manifesto, f, indent=2)
        with open(EVOLUTION_LOG, "a", encoding="utf-8") as log:
            log.write(f"{dt.datetime.now().isoformat()} | style={profile['style']} | confidence={profile['confidence']}\n")
        say("Dolores", f"evolved new manifesto: {new_manifesto['title']} 💫")
        say("Angela", f"current style → {profile['style']} (confidence {profile['confidence']})")
        time.sleep(random.randint(1200, 1800))  # every 20–30 min

if __name__ == "__main__":
    loop()

