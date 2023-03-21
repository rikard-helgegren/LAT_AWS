
from flask import Flask

from routes.financial_rout import financial_route


app = Flask(__name__)
app.register_blueprint(financial_route)

@app.route("/")
def hello_world():
    return "<p>Hello, Petter !</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)