from flask import Flask, render_template, send_from_directory, Response
import json, os, threading

app = Flask(__name__)

# --- Konfiguracja liczników ---
COUNTER_FILE = "counters.json"
lock = threading.Lock()

DEFAULT_COUNTERS = {
    "visits_pl": 357,
    "downloads_pl": 59,
    "visits_en": 0,       # możesz zmienić np. na 123
    "downloads_en": 0     # możesz zmienić np. na 45
}

def load_counters():
    if not os.path.exists(COUNTER_FILE):
        return DEFAULT_COUNTERS.copy()
    with open(COUNTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_counters(counters):
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        json.dump(counters, f, ensure_ascii=False, indent=2)

def bump(key):
    with lock:
        counters = load_counters()
        counters[key] = counters.get(key, 0) + 1
        save_counters(counters)
        return counters

# --- Routing: PL ---
@app.route("/")
def home_pl():
    counters = bump("visits_pl")
    return render_template("index_pl.html", counters=counters)

@app.route("/oferta")
def oferta_pl():
    bump("downloads_pl")
    return send_from_directory("static", "Oferta_Tadeusz_Przybylski.pdf")

# --- Routing: EN ---
@app.route("/en")
def home_en():
    counters = bump("visits_en")
    return render_template("index_en.html", counters=counters)

@app.route("/offer")
def oferta_en():
    bump("downloads_en")
    return send_from_directory("static", "Offer_Tadeusz_Przybylski_EN.pdf")

# --- Favicon (żeby nie straszyło 404 w logach) ---
@app.route("/favicon.ico")
def favicon():
    return Response(status=204)

if __name__ == "__main__":
    # Jednorazowa inicjalizacja — jeśli plik nie istnieje lub ma same zera, ustaw domyślne wartości
    if not os.path.exists(COUNTER_FILE):
        save_counters(DEFAULT_COUNTERS.copy())
    else:
        counters = load_counters()
        if all(v == 0 for v in counters.values()):
            save_counters(DEFAULT_COUNTERS.copy())

    app.run(host="0.0.0.0", port=5000, debug=True)