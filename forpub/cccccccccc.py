from flask import Flask,render_template
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route("/dd")
def hello():
    return render_template("login.html")

@app.route("/ff")
def go():
    return "jjjjjjjj"

if __name__ == "__main__":
    app.run()