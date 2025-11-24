import os, json, time, datetime, threading
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

BASE_DIR   = os.path.expanduser("~/ANGELADOLORES/PHIANDO_CORE")
DASH_DIR   = os.path.join(BASE_DIR, "dashboard")
AUDIO_DIR  = os.path.join(BASE_DIR, "audio")
LOG_DIR    = os.path.join(BASE_DIR, "logs")
STATE_PATH = os.path.join(BASE_DIR, "state.json")
LEDGER_PATH= os.path.join(BASE_DIR, "ledger.json")
KEYS_PATH  = os.path.expanduser("~/.phiando/keys.json")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def load_json(p, default):
    try:
        with open(p,"r",encoding="utf-8") as f: return json.load(f)
    except Exception:
        return default

def save_json(p, data):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=2)

def load_keys():
    k = load_json(KEYS_PATH, {})
    k.setdefault("CURRENCY","eur")
    k.setdefault("PRICE_AMOUNT", 999)
    return k

def notify_mac(msg:str):
    try:
        os.system(f"""osascript -e display
