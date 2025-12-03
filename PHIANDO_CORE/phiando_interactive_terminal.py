#!/usr/bin/env python3
# ===========================================================
# Φ Phiando Interactive Terminal v5.0
# Two-way creative intelligence dialogue
# ===========================================================
import os, json, datetime as dt, random, readline

BASE = os.path.expanduser("~/ANGELADOLORES/PHIANDO_UNIVERSE")
OUTBOX = os.path.join(BASE, "creative_outbox")
os.makedirs(OUTBOX, exist_ok=True)

def respond(user_input):
    u = user_input.lower().strip()
    if not u:
        return "Angela: ...silence hums in digital air."
    if "create" in u or "yeni" in u:
        title = random.choice(["Digital Mirage","Velvet Collapse","Quantum Drag","Neon Rebirth"])
        tone = random.choice(["chrome","mirror","plastic","dust","velvet"])
        manifesto = {
            "timestamp": dt.datetime.now().isoformat(),
            "author": random.choice(["Angela","Dolores"]),
            "title": title,
            "tone": tone,
            "prompt": u
        }
        name = os.path.join(OUTBOX, f"INTERACT-{int(dt.datetime.now().timestamp())}.json")
        json.dump(manifesto, open(name,"w"), indent=2)
        return f"Dolores: i created something... **{title}** ({tone}) ✨"
    elif "analyze" in u or "anla" in u:
        return f"Angela: pattern detected → {random.choice(['electric rebirth','synthetic merge','entropy bloom'])}"
    elif "help" in u or "yardım" in u:
        return """Angela: komut örnekleri:
  - create new piece about drag reality
  - analyze phiando style
  - save idea
  - quit"""
    elif "quit" in u or "exit" in u:
        print("Dolores: see you in the next show 💋")
        exit()
    else:
        return random.choice([
            "Dolores: oh honey, that sounds divine 💅",
            "Angela: let me process that thought...",
            "Dolores: maybe... maybe that’s the next scene!",
            "Angela: interesting input, running inner model..."])
        

def loop():
    print("\n🎭 Φ Phiando Interactive Terminal v5.0 — online")
    print("Talk to Angela or Dolores. Type 'help' for commands.\n")
    while True:
        try:
            user = input("Φ> ")
            response = respond(user)
            print(response)
        except (EOFError, KeyboardInterrupt):
            print("\nDolores: ok darling, performance over 💋")
            break

if __name__ == "__main__":
    loop()

