from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyBYmDPYjNdfWKjtn9mRpahHYiFIWxMt6ls")

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    ai_response = ""
    if request.method == "POST":
        user_input = request.form.get("text_input")
        if user_input == "what is your name" or "your name" in user_input:
            ai_response = "My name is Ayra . I'm an AI model developed by Yadhu on 20-06-2025."
        else:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(user_input)
                ai_response = response.text

    return render_template("index.html", user_input=user_input, ai_response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)

