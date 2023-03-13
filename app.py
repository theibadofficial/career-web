from flask import Flask

app = Flask(__name__)


# @ --> decurater in py
@app.route("/")
def de():
  return "hello"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
