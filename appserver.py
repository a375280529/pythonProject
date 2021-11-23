from flask import Flask
import config
from flask import session
from bluetu import lantu
app = Flask(__name__,template_folder='templates')
app.register_blueprint(lantu,url_prefix='/lantu')
app.config.from_object(config)

@app.route("/")
def index():
    return "ok"


if __name__ == '__main__':
    app.run()