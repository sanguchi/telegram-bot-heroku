import flask
from bot import token, bot
from telebot.types import Update
from os import environ

app = flask.Flask(__name__)


@app.route('/')
def index():
    if("GITHUB_URL" in environ):
        repo = environ["GITHUB_URL"]
    else:
        repo = None
    return flask.render_template("index.html", repo=repo)


@app.route("/{}".format(token), methods=["POST"])
def handle_update():
    if(flask.request.headers.get("content-type") == "application/json"):
        json_string = flask.request.get_data().decode("utf-8")
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


if(__name__ == "__main__"):
    app.run()
