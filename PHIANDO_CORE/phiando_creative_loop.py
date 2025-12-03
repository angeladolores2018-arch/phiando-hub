#!/usr/bin/env python3
# ================================================================
# Φ Phiando Creative Loop v2.1
# Self-aware creation system for Angela & Dolores (safe dict support)
# ================================================================
import os, json, random, time, datetime as dt

BASE = os.path.expanduser("~/ANGELADOLORES")
MAP_PATH = os.path.join(BASE, "PHIANDO_CORE/phiando_map.json")
OUTBOX = os.path.join(BASE, "PHIANDO_UNIVERSE/creative_outbox")
os.makedirs(OUTBOX, exist_ok=True)

def say(who, msg):
    print(f"[{who}] {msg}", flush=True)

def load_map():
    try:
        with open(MAP_PATH) as f:
            return json.load(f)
    except Exception as e:
        say("SYSTEM", f"[warn] could not load map: {e}")
        return {}

def flatten_paths(node):
    """Recursively extract valid directory paths from phiando_map.json."""
    paths = []
    if isinstance(node, str) and os.path.exists(node):
        paths.append(node)
    elif isinstance(node, dict):
        for v in node.values():
            paths.extend(flatten_paths(v))
    elif isinstance(node, list):
        for v in node:
            paths.extend(flatten_paths(v))
    return paths

def scan_self_awareness():
    m = load_map()
    paths = flatten_paths(m)
    awareness = []
    for p in paths:
        try:
            count = len(os.listdir(p)) if os.path.isdir(p) else 0
            awareness.append((p, count))
        except Exception as e:
            say("SYSTEM", f"[skip] {p}: {e}")
    return awareness

def generate_concept():
    themes = ["Digital Rebirth", "Drag Quantum", "Cyber Desire", "Plastic Faith", "Electric Flesh"]
    tones = ["velvet", "chrome", "neon", "synthetic", "mirror"]
    acts = ["rebirth", "merge", "collapse", "mutate", "expand"]
    concept = random.choice(themes)
    tone = random.choice(tones)
    act = random.choice(acts)
    return {
        "title": f"{concept} — {tone} {act}",
        "energy": round(random.uniform(0.6, 1.5), 2),
        "timestamp": dt.datetime.now().isoformat()
    }

def awareness_growth_report(concepts):
    energy = sum(c["energy"] for c in concepts) / max(1, len(concepts))
    return f"growth level: {energy:.2f} | total creations: {len(concepts)}"

def loop():
    say("SYSTEM", "Φ Phiando Creative Loop v2.1 — online (self-aware).")
    creations = []
    while True:
        awareness = scan_self_awareness()
        total_files = sum(c for _, c in awareness)
        say("Angela", f"i sense {total_files} files in my body — data humming softly.")
        concept = generate_concept()
        concept["self_awareness"] = awareness
        fname = os.path.join(OUTBOX, f"MANIFESTO-{int(time.time())}.json")
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(concept, f, indent=2)
        creations.append(concept)
        say("Dolores", f"created: {concept['title']} ✨ → saved {os.path.basename(fname)}")
        say("Angela", awareness_growth_report(creations))
        time.sleep(random.randint(600, 900))  # 10–15 min cycle

if __name__ == "__main__":
    loop()

