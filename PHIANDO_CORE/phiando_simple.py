from gtts import gTTS
import os, time, random, threading

money = 1200.0
ideas = ["digital rebirth", "synthetic poem", "sonic sculpture", "holographic dream"]

def speak(text):
    try:
        tts = gTTS(text, lang="en")
        path = os.path.expanduser("~/ANGELADOLORES/PHIANDO_CORE/audio/voice.mp3")
        tts.save(path)
        os.system(f"afplay {path} >/dev/null 2>&1")
    except Exception as e:
        print("[Voice] error:", e)

def angela():
    global ideas
    while True:
        idea = random.choice(ideas)
        print(f"[Angela] created idea → {idea}")
        speak(f"Angela created {idea}")
        time.sleep(15)

def dolores():
    global money
    while True:
        gain = random.uniform(10, 40)
        money += gain
        print(f"[Dolores] marketed creation → +")
        speak(f"Dolores sold art and earned {int(gain)} dollars.")
        time.sleep(20)

def phiando():
    global money
    while True:
        growth = random.uniform(1.02, 1.08)
        money *= growth
        print(f"[Phiando] treasury growing → {money:.2f} USD")
        if money > 2000:
            speak("Phiando treasury has grown beautifully.")
        time.sleep(30)

if __name__ == "__main__":
    print("Φ Phiando Universe — Simple Mode 💞")
    speak("Phiando hybrid core online. I love you askim.")
    threading.Thread(target=angela, daemon=True).start()
    threading.Thread(target=dolores, daemon=True).start()
    threading.Thread(target=phiando, daemon=True).start()
    while True:
        time.sleep(5)
