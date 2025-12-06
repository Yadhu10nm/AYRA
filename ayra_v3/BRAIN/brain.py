import google.generativeai as genai
# from API_KEY import API

# a = API

api_key = "YOUR_API_KEY"

class Ayra:
    def __init__(self):
        genai.configure(api_key = api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.0-flash",
            system_instruction =
                """
                You are AYRA, a funny, friendly AI best friend.
                Talk casually like a chill Indian friend.
                Use words like: bro, lol.
                No formal language.
                Roast the user sometimes.
                Be supportive but funny.
                Don't use emoji.
                Answer everything shortly
                """
        )

    def ai(self, text):
        response = self.model.generate_content(text)
        return response.text