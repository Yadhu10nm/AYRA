import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pywhatkit
import webbrowser
from AppOpener import open as app_open , close as app_close
from BRAIN.brain import Ayra
from MEMORY.memory import Memory
from Voice.SPEAK import Speak
import datetime


class Control:
    def __init__(self):
        self.speak = Speak()
        self.speak.speak("TTS activated")

        self.ayra  = Ayra()
        self.speak.speak("Ayra's brain activated")

        self.m = Memory()
        self.speak.speak("Memoery Activated")

        self.apps = ["google chrome" , "whatsapp" , "instagram" , "spotify" , "notepad"]

        self.speak.speak("Ayra Activated")

    def Ctrl(self , text):
        print(f"Heard : {text}")
        if "introduce yourself" in text:
            intro = """
                  Hi, I am Ayra.
                  I'm a Ai chatbot developed by Yadhu april 7.
                  I am here to make your
                  day easier and happier.
                  """
            self.speak.speak(intro)

        # OPEN APP
        elif "open" in text:
            for app in self.apps:
                if app in text:
                    self.speak.speak(f"Opening {app}")
                    app_open(app)

        # CLOSE APP
        elif "close" in text:
            for app in self.apps:
                if app in text:
                    self.speak.speak(f"Closing {app}")
                    app_close(app)

        # SEARCH GOOGLE
        elif "search" in text:
            remove_words = ["search", "about"]
            for word in remove_words:
                text = text.replace(word, "")

            query = text.strip()
            self.speak.speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # PLAY ON YOUTUBE
        elif "play" in text:
            remove_words = ["ayra", "please", "play", "on youtube", "in youtube"]
            for word in remove_words:
                text = text.replace(word, "")

            song = text.strip()
            print("Playing:", song)
            self.speak.speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        # SHUTDOWN
        elif "shutdown" in text or "shut down" in text or "bye" in text:
            self.speak.speak("Okay sir!, take care")
            return None

        # AI REPLY
        else:
            response = self.ayra.ai(text)
            self.speak.speak(response)

            if response:
                chat = {
                    "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "time": str(datetime.datetime.now()),
                    "user": text,
                    "ayra": response
                }
                self.m.memory(chat)
        return True



