import pyttsx3
import time

class Speak:
    def __init__(self):
        print("Initializing TTS engine...")
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[2].id)
        self.engine.setProperty('rate', 175)

        time.sleep(1)

    def speak(self, text):
        print("Ayra says:", text)
        self.engine.say(text)
        self.engine.runAndWait()
