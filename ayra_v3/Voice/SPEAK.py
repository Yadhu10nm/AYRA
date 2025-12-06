import pyttsx3
import time

class Speak:
    def __init__(self):
        print("Initializing TTS engine...")
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[2].id)
        self.engine.setProperty('rate', 130)

        time.sleep(1)

    def speak(self, text):
        print("Ayra says:", text)
        self.engine.say(text)
        self.engine.runAndWait()

# import asyncio
# import edge_tts
# import pygame
# import os
# import uuid
# import time
#
# class Speak:
#     def __init__(self):
#         self.voice = "en-IN-NeerjaNeural"
#         pygame.mixer.init()
#
#     async def speak_(self, text):
#         # make unique file every time
#         filename = f"voice_{uuid.uuid4().hex}.mp3"
#         file_path = os.path.join(os.path.dirname(__file__), filename)
#
#         communicate = edge_tts.Communicate(text, self.voice)
#         await communicate.save(file_path)
#
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)
#
#         pygame.mixer.music.stop()
#         pygame.mixer.music.unload()
#
#         # Don't delete immediately, let Windows relax 😄
#         time.sleep(1)
#
#         # safe delete
#         try:
#             os.remove(file_path)
#         except:
#             pass
#
#     def speak(self, text):
#         asyncio.run(self.speak_(text))
#
#
