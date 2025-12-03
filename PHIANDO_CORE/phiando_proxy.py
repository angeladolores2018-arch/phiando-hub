import openai, os, json, time
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/api/message")
def message():
    data = request.get_json(force=True)
    role = data.get("role","Angela")
    msg = data.get("text","")
    if not msg:
        return jsonify(error="no text"), 400

    prompt = f"[{role}] {msg}"
    resp = openai.ChatCompletion.create(
        model="gpt-5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=150
    )
    out = resp.choices[0].message["content"]
    print(f"[{role}] {out}")
    return jsonify(reply=out)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9090)

