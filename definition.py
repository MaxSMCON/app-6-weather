from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/vi/<word>")
def dictionary(word):
    # word = input()
    return {"word": word,
            "definition": word.upper()}

if __name__ == "__main__":
    app.run(debug=True, port=5002)