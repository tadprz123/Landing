from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Działa! 🚀 Flask na Vercel"

@app.route("/notes")
def notes():
    data = {
        "topic": "Umiejętności Jutra - tydzień 1",
        "points": [
            "Podstawy AI i LLM",
            "Prompt engineering – sztuka zadawania pytań",
            "Metody promptowania",
            "Narzędzia i modele (Bielik, Gemini, NotebookLM)",
            "Research i analiza danych",
            "Multimodalność",
            "RAG – Retrieval Augmented Generation",
            "Modele zamknięte vs. otwarte",
            "Bezpieczeństwo danych",
            "Najważniejsze pytania przy wyborze AI"
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()