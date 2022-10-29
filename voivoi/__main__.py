import datetime
from flask import Flask, Response, request, render_template
from pyvcroid2 import VcRoid2
from .models.voiceroid import Voiceroid

app = Flask(__name__)


@app.route("/")
def index():
    """
    /
    """
    vc = VcRoid2()

    return render_template(
        "index.html",
        voices=vc.listVoices(),
        languages=vc.listLanguages()
    )


@app.route("/voices")
def voices():
    """
    /voices

    return avaiable voices.
    """
    vc = VcRoid2()

    return {"voices": vc.listVoices()}


@app.route("/languages")
def languages():
    """
    /languages

    return avaiable languages.
    """
    vc = VcRoid2()

    return {"languages": vc.listLanguages()}


@app.route("/tts", methods=["GET"])
def tts():
    vc = VcRoid2()

    voice = request.args.get("voice") or vc.listVoices()[0]
    language = request.args.get("language") or vc.listLanguages()[0]
    text = request.args.get("text")
    del vc  # NOTE: 明示的にインスタンス破棄しないと pyvcroid2 から ResultCode.ALREADY_INITIALIZED が raise される

    vc = Voiceroid(voice, language)
    speech, _ = vc.tts(text)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    response = Response(speech, mimetype="audio/wave")
    response.headers["Content-Disposition"] = f"attachment; filename={timestamp}.wav"

    return response


if __name__ == "__main__":
    app.run()
