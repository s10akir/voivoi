from flask import Flask
from pyvcroid2 import VcRoid2

app = Flask(__name__)


@app.route('/')
def index():
    """
    /
    """
    return {"mesage": "Hello World!"}


@app.route('/info')
def info():
    """
    /info
    return avaiable voices and languages.
    """
    vc = VcRoid2()

    return {"voices": vc.listVoices(), "languages": vc.listLanguages()}


if __name__ == '__main__':
    app.run()
