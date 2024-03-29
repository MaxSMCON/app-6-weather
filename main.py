# import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/vi/<station>/<date>")
def about(station, date):
    # df = pd.read_csv("")
    temperature = 23 #df.station(date)
    return {"station": station,
            "date": date,
            "temperature": temperature}
if __name__ == "__main__":
    app.run(debug=True, port=5001)
