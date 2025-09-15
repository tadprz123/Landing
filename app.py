from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index_pl.html")

@app.route("/en")
def home_en():
    return render_template("index_en.html")

if __name__ == "__main__":
    app.run(debug=True)