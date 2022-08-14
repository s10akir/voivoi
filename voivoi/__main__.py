import datetime
import random
from flask import Flask, Response, request
from pyvcroid2 import VcRoid2
from .models.voiceroid import Voiceroid

app = Flask(__name__)


@app.route("/")
def index():
    """
    /
    """
    return {"mesage": "Hello World!"}


@app.route("/info")
def info():
    """
    /info
    return avaiable voices and languages.
    """
    vc = VcRoid2()

    return {"voices": vc.listVoices(), "languages": vc.listLanguages()}


@app.route("/tts", methods=["GET"])
def tts():
    voice = request.args.get("voice")
    language = request.args.get("language")
    text = request.args.get("text")

    vc = Voiceroid(voice, language)
    speech, _ = vc.tts(text)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    response = Response(speech, mimetype="audio/wave")
    response.headers["Content-Disposition"] = f"attachment; filename={timestamp}.wav"

    return response


if __name__ == "__main__":
    app.run()
