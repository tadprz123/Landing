from flask import Flask, render_template, send_from_directory
import os
import json, pathlib

app = Flask(__name__)

# -------------------------------
# ROUTES
# -------------------------------

@app.route("/")
def home():
    return render_template("index_pl.html")

@app.route("/en")
def home_en():
    return render_template("index_en.html")

# serwowanie plików statycznych (np. PDF, DOCX)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, "static"), filename)

def load_counters():
    p = pathlib.Path("counters.json")
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            pass
    # domyślne wartości, gdy pliku nie ma / jest uszkodzony
    return {"pl": 0, "en": 0, "total": 0}

@app.context_processor
def inject_counters():
    # dzięki temu w każdym szablonie jest dostępne {{ counters }}
    return dict(counters=load_counters())
# -------------------------------
# ENTRYPOINT
# -------------------------------
if __name__ == "__main__":
    # lokalnie odpala serwer na porcie 8000
    app.run(debug=True, host="0.0.0.0", port=8000)