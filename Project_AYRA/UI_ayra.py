import streamlit as st
import AYRA.Ayra as ayra
import pyttsx3 as TTS


def speak():
    tts = TTS.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[1].id)
    tts.say("I am Ayra, how can I help you")
    tts.runAndWait()

def ui():
    st.title("Ayra here !")
    speak()
    st.write("______________________________________________")
    prompt = st.text_area(label="Type here ")
    if st.button("click"):
            respose = ayra.ayra(prompt)
            st.markdown(f"<p style='font-size:30px;'>{respose}</p>", unsafe_allow_html=True)


ui()
