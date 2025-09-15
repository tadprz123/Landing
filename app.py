# app.py
from flask import Flask, render_template
import json, pathlib

app = Flask(__name__)

# ---- counters: zawsze dostępne w Jinja, bez zapisu pliku ----
def load_counters():
    p = pathlib.Path("counters.json")
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            pass
    return {"pl": 0, "en": 0, "total": 0}

@app.context_processor
def inject_counters():
    return dict(counters=load_counters())

# ---- routes ----
@app.route("/")
def home():
    return render_template("index_pl.html")

@app.route("/en")
def home_en():
    return render_template("index_en.html")

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(debug=True)