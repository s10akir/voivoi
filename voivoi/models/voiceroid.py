import random
from pyvcroid2 import VcRoid2
from werkzeug import exceptions


class Voiceroid:
    def __init__(self, voice, language):
        self.vc = VcRoid2()
        self.loadVoice(voice)
        self.loadLanguage(language)

    def loadVoice(self, voice):
        if voice is not None:
            if voice in self.vc.listVoices():
                self.vc.loadVoice(voice)
            else:
                # NOTE: tts までいかなかった場合に明示的に object を破棄しないと
                #       pyvcroid2 から ResultCode.ALREADY_INITIALIZED が raise される
                del self.vc
                raise exceptions.BadRequest(f"{voice} is not available in voice.")
        else:
            self.vc.loadVoice(random.choice(self.vc.listVoices()))

    def loadLanguage(self, language):
        if language is not None:
            if language in self.vc.listLanguages():
                self.vc.loadLanguage(language)
            else:
                # NOTE: tts までいかなかった場合に明示的に object を破棄しないと
                #       pyvcroid2 から ResultCode.ALREADY_INITIALIZED が raise される
                del self.vc
                raise exceptions.BadRequest(f"{language} is not available in language.")
        else:
            self.vc.loadLanguage(random.choice(self.vc.listLanguages()))

    def tts(self, text):
        if text is None:
            # NOTE: tts までいかなかった場合に明示的に object を破棄しないと
            #       pyvcroid2 から ResultCode.ALREADY_INITIALIZED が raise される
            del self.vc
            raise exceptions.BadRequest("text is required parameter.")

        return self.vc.textToSpeech(text)
