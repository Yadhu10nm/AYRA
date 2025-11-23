import speech_recognition as sr

class Listen:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        # ✅ Better mic handling
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.6
        self.recognizer.phrase_threshold = 0.3

    def listening(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
            print("Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)

        try:
            text = self.recognizer.recognize_google(audio, language="en-IN").lower()
            return text
        except sr.UnknownValueError:
            print("Did not catch that, try again bro...")

        except sr.RequestError:
            print("Network issue macha...")
