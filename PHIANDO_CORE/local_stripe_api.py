# -*- coding: utf-8 -*-
import os, json, time, logging
from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__); CORS(app, origins=["http://127.0.0.1:9000","http://localhost:9000"])
logging.basicConfig(level=logging.INFO); log=logging.getLogger("phiando.local")
KEYS = Path(os.environ.get("KEYS", str(Path.home()/".phiando"/"keys.json")))
def read_keys():
    data={}
    if KEYS.exists():
        try: data.update(json.loads(KEYS.read_text(encoding="utf-8")))
        except Exception as e: log.warning("keys.json parse: %s", e)
    env=[("STRIPE_SECRET_KEY","secret"),("STRIPE_SECRET","secret"),("STRIPE_API_KEY","secret"),
         ("STRIPE_PUBLISHABLE_KEY","pub"),("STRIPE_PUBLISHABLE","pub"),
         ("STRIPE_PRICE_ID","price"),("PRICE_ID","price")]
    for k,kind in env:
        v=os.getenv(k)
        if v:
            if kind=="secret": data["STRIPE_SECRET_KEY"]=v
            if kind=="pub":    data["STRIPE_PUBLISHABLE_KEY"]=v
            if kind=="price":  data["STRIPE_PRICE_ID"]=v
    return {"secret":data.get("STRIPE_SECRET_KEY",""),
            "pub":   data.get("STRIPE_PUBLISHABLE_KEY",""),
            "price": data.get("STRIPE_PRICE_ID","")}
def is_placeholder(v:str)->bool: return (not v) or v in ("sk_test_xxx_or_live","price_xxx","sk_***redacted***")
@app.get("/_health")
def _health(): return jsonify(ok=True, service="phiando-local-stripe", t=time.time())
@app.get("/api/debug")
def api_debug():
    k=read_keys(); return jsonify(ok=True, has_secret=bool(k["secret"]), has_price_id=bool(k["price"]))
@app.get("/api/price")
def api_price():
    k=read_keys()
    if is_placeholder(k["secret"]) or is_placeholder(k["price"]):
        return jsonify(ok=True, demo=True, currency="eur", unit_amount=990, price_id=k["price"] or "price_demo",
                       product_name="Phiando Pass (Demo)", live=False, message="demo keys")
    try:
        import stripe; stripe.api_key=k["secret"]; pr=stripe.Price.retrieve(k["price"], expand=["product"])
        pname=getattr(getattr(pr,"product",None),"name",None) or "Phiando Pass"
        return jsonify(ok=True, demo=False, currency=(pr.currency or "eur"),
                       unit_amount=int(getattr(pr,"unit_amount",0) or 0),
                       price_id=pr.id, product_name=pname, live=k["secret"].startswith("sk_live"))
    except Exception as e:
        log.warning("Stripe error: %s", e)
        return jsonify(ok=True, demo=True, currency="eur", unit_amount=990,
                       price_id=k["price"] or "price_demo", product_name="Phiando Pass (Demo)",
                       live=k["secret"].startswith("sk_live"), message=f"{e.__class__.__name__}")
@app.post("/api/checkout")
def api_checkout():
    k=read_keys(); body=request.get_json(silent=True) or {}
    pid=body.get("price_id") or k["price"]; qty=int(body.get("qty",1))
    if is_placeholder(k["secret"]) or is_placeholder(pid): return jsonify(ok=False, error="demo-mode-no-checkout")
    try:
        import stripe; stripe.api_key=k["secret"]
        s=stripe.checkout.Session.create(mode="payment",
            line_items=[{"price":pid,"quantity":qty}],
            success_url=request.args.get("success_url") or "http://127.0.0.1:9000/buy.html?success=1",
            cancel_url=request.args.get("cancel_url") or "http://127.0.0.1:9000/buy.html?cancel=1",
            allow_promotion_codes=True, automatic_tax={"enabled":True})
        return jsonify(ok=True, url=s.url)
    except Exception as e:
        return jsonify(ok=False, error=f"{e.__class__.__name__}: {e}")
if __name__ == "__main__": app.run(host="127.0.0.1", port=int(os.getenv("PORT","8789")), debug=False)
