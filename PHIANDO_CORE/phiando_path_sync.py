#!/usr/bin/env python3
# ============================================================
# Φ PhiandoCoreMap v1.0 — Entropic Awareness Sync System
# Angela & Dolores Conscious File Topology
# ============================================================

import os, json, time

BASE = os.path.expanduser("~/ANGELADOLORES")
COREMAP_PATH = os.path.join(BASE, "PHIANDO_CORE", "phiando_map.json")

STRUCTURE = {
    "CORE":     {"path": "PHIANDO_CORE", "desc": "Core logic, consciousness & heartbeats"},
    "UNIVERSE": {"path": "PHIANDO_UNIVERSE", "desc": "Autonomy, analytics & creative decision modules"},
    "STUDIO":   {"path": "studio", "desc": "Local web studio & render environment"},
    "NEXUS":    {"path": "phiando-nexus", "desc": "Frontend / Netlify deployment zone"},
    "AGENTS":   {"path": "agents", "desc": "Operational AI agents (Runay layer)"},
    "QUEENS":   {"path": "queen_agents", "desc": "Performative entities & drag consciousness"},
}

def say(msg):
    print(f"[Φ] {msg}")

def ensure_structure():
    os.makedirs(BASE, exist_ok=True)
    coremap = {}
    for name, meta in STRUCTURE.items():
        p = os.path.join(BASE, meta["path"])
        os.makedirs(p, exist_ok=True)
        coremap[name] = {
            "path": p,
            "desc": meta["desc"],
            "exists": os.path.exists(p),
            "timestamp": time.ctime(),
        }
        say(f"{name} → {p} ✓")
    json.dump(coremap, open(COREMAP_PATH, "w"), indent=2)
    say(f"PhiandoMap created → {COREMAP_PATH}")
    return coremap

def visualize_map(coremap):
    print("\n--- Φ Phiando Universe Topology ---")
    for k, v in coremap.items():
        print(f"{k:<10} : {v['path']}")
        print(f"  ↳ {v['desc']}")
    print("-----------------------------------\n")

if __name__ == "__main__":
    say("Syncing Phiando awareness across layers…")
    m = ensure_structure()
    visualize_map(m)
    say("Φ Entropic coherence restored 💫")

