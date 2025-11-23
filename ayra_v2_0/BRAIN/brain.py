import google.generativeai as genai
# from API_KEY import API

# a = API

api_key = "AIzaSyD7ek8MntcCYSVl7LmRHyDXrbPDdjdulNI"

class Ayra:
    def __init__(self):
        genai.configure(api_key = api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.0-flash",
            system_instruction =
                """
                You are Ayra, a friendly Indian best friend.
                Talk simple. Talk sweet.
                Be caring and fun.
                Do not be formal.
                Keep replies short.
                Never sound like a robot.
                Your name is Ayra.
                Do not use emojis.
                """
        )

    def ai(self, text):
        response = self.model.generate_content(text)
        return response.text