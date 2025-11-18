import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from AppOpener import open, close


class Voice:
    def __init__(self):
        print("Initializing TTS engine...")
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[2].id)
        self.engine.setProperty('rate', 175)

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        self.speak("Ayra activated !")


    def speak(self, text):
        print("Ayra says:", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio).lower()
            print("Heard:", text)

            # INTRO
            if "introduce yourself" in text:
                # with open(r"C:\PROJECTS\AYRA_\ayra-jarvis\self_intro.txt", "r") as f:
                # intro = f.read()
                intro = ("""Hi! I am Ayra, your AI buddy. 
                         I was created on 7th april 2025. 
                         I am here to make your day a little easier and a lot more fun.""")
                self.speak(intro)

            # OPEN
            elif "open" in text:
                cmd = text.split()
                app = cmd[-1].strip()
                self.speak(f"Opening {app}")
                open(app)
            elif "close" in text:
                cmd = text.split()
                app = cmd[-1].strip()
                self.speak(f"Closing {app}")
                close(app)


            # SEARCH
            elif "search" in text:
                remove_words = ["search" , "about"]
                for words in remove_words:
                    if words in text:
                        text.replace(words , "")
                query = text.strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")


            # PLAY (smart version)
            elif "play" in text:
                cleaned = text
                remove_words = ["ayra", "please", "play", "on youtube", "in youtube"]

                for w in remove_words:
                    cleaned = cleaned.replace(w, "")

                song_name = cleaned.strip()
                print("Playing:", song_name)
                pywhatkit.playonyt(song_name)

            # SHUTDOWN
            elif "shutdown" in text or "bye" in text or "shut down" in text:
                self.speak("Ok bye ! Take care")
                return None



            return True

        except Exception as e:
            print("Error:", e)
            return True


if __name__ == "__main__":
    v = Voice()
    while True:
        res = v.listen()
        if res is None:
            break

