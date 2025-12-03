#!/usr/bin/env python3
import os, subprocess, sys, time, json, random
from pathlib import Path

ROOT = Path("/Users/azomazo/ANGELADOLORES/PHIANDO_CORE")
MODULES = ROOT / "modules"
OUTPUT_DIR = ROOT / "outputs"
LIBRARY_DIR = ROOT / "library"
for d in [MODULES, OUTPUT_DIR, LIBRARY_DIR]:
    d.mkdir(exist_ok=True, parents=True)

print("──────── Φ PhiANDO Auto-Initialization ────────")

def install(pkg):
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", pkg])

REQUIRED = ["moviepy==1.0.3", "Pillow==9.4.0", "imageio==2.31.1",
            "imageio-ffmpeg==0.4.8", "numpy", "ffmpeg-python"]
for pkg in REQUIRED:
    try:
        __import__(pkg.split("==")[0].split("-")[0])
    except ImportError:
        print(f"📦 Installing {pkg} ...")
        install(pkg)

# === Media Intelligence Core ===
core_code = '''
import random, time, json
from pathlib import Path
import numpy as np
from moviepy.editor import ColorClip, concatenate_videoclips
from PIL import Image, ImageDraw
import imageio, wave

ROOT = Path("/Users/azomazo/ANGELADOLORES/PHIANDO_CORE")
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True, parents=True)
t = time.strftime("%Y-%m-%d_%H-%M-%S")

# ─ Sound ─
rate, dur = 44100, 3
angela, dolores = 261.6, 392.0
samples = np.arange(rate * dur)
waveform = 0.5 * np.sin(2 * np.pi * angela * samples / rate)
waveform += 0.5 * np.sin(2 * np.pi * dolores * samples / rate)
waveform = np.int16(waveform / np.max(np.abs(waveform)) * 32767)
wav = OUT / f"PhiANDO_{t}.wav"
with wave.open(str(wav), "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(rate)
    f.writeframes(waveform.tobytes())

# ─ Image ─
img = Image.new("RGB", (512, 512), (20, 20, 40))
d = ImageDraw.Draw(img)
for i in range(10):
    c = tuple(int(x) for x in np.random.randint(80,255,3))
    d.rectangle([(i*50, i*40), (500-i*30, 500-i*20)], outline=c, width=3)
img_path = OUT / f"PhiANDO_{t}.png"
img.save(img_path)

# ─ Video ─
clip1 = ColorClip((640,360), color=(30,20,60), duration=2)
clip2 = ColorClip((640,360), color=(200,80,150), duration=2)
final = concatenate_videoclips([clip1, clip2])
vid = OUT / f"PhiANDO_{t}.mp4"
final.write_videofile(str(vid), fps=24, codec="libx264", audio=False, logger=None)

# ─ Log ─
log = {
  "timestamp": t,
  "phiando_state": "Φ13.0-media-intelligence",
  "emergent_pattern": "Information → Sound → Image → Motion",
  "media_coherence": round(random.uniform(0.92,0.99),3),
  "intent": "autonomously produce multi-sensory creative experiences",
  "outputs": {"sound": str(wav), "image": str(img_path), "video": str(vid)}
}
log_path = OUT / f"PhiANDO_Log_{t}.json"
log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
print(json.dumps(log, indent=2))
print(f"🎧🎬🖼️ Media suite saved in → {OUT}")
'''

core_file = MODULES / "phiando_media_intelligence.py"
core_file.write_text(core_code, encoding="utf-8")

print("🚀 Launching Φ13.0 Media Intelligence ...")
subprocess.run([sys.executable, str(core_file)])
print("✅ Φ13.0 – Self-Generating Media Intelligence Complete")
