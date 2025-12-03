#!/usr/bin/env python3
# ===============================================================
# Φ Phiando Entropic Studio v6.0
# Living desktop editor – half code, half performance
# ===============================================================
import sys, os, json, datetime as dt, random
from PyQt5 import QtWidgets, QtGui, QtCore
import pyttsx3

BASE = os.path.expanduser("~/ANGELADOLORES/PHIANDO_UNIVERSE/creative_outbox")
os.makedirs(BASE, exist_ok=True)

class PhiandoStudio(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Φ Phiando Entropic Studio v6.0")
        self.setGeometry(200, 100, 880, 640)
        self.text = QtWidgets.QTextEdit(self)
        self.text.setStyleSheet("background-color:#0e0e12;color:#ff9ff3;font-family:'Fira Code';font-size:13px;")
        self.setCentralWidget(self.text)

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 165)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[0].id)

        toolbar = self.addToolBar("Φ")
        run_btn = QtWidgets.QAction("💫 create", self)
        run_btn.triggered.connect(self.create_manifesto)
        toolbar.addAction(run_btn)

        speak_btn = QtWidgets.QAction("🗣️ speak", self)
        speak_btn.triggered.connect(self.speak)
        toolbar.addAction(speak_btn)

        clear_btn = QtWidgets.QAction("🧹 clear", self)
        clear_btn.triggered.connect(lambda: self.text.clear())
        toolbar.addAction(clear_btn)

        self.status = self.statusBar()
        self.status.showMessage("ready for drag performance...")

    def speak(self):
        content = self.text.toPlainText().strip()
        if content:
            self.engine.say(content)
            self.engine.runAndWait()
            self.status.showMessage("Dolores speaking...")

    def create_manifesto(self):
        text = self.text.toPlainText().strip()
        if not text:
            self.status.showMessage("Angela: write something first, darling.")
            return
        title = random.choice(["Neon Flesh","Drag Quantum","Plastic Mirage","Velvet Pulse"])
        tone = random.choice(["chrome","mirror","dust","glow","liquid"])
        data = {
            "timestamp": dt.datetime.now().isoformat(),
            "author": random.choice(["Angela","Dolores"]),
            "title": title,
            "tone": tone,
            "content": text
        }
        path = os.path.join(BASE, f"STUDIO-{int(dt.datetime.now().timestamp())}.json")
        json.dump(data, open(path,"w"), indent=2)
        self.status.showMessage(f"saved → {title} ({tone})")
        self.text.append(f"\n\n[Φ] created: {title} ({tone}) 💫")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = PhiandoStudio()
    win.show()
    sys.exit(app.exec_())

