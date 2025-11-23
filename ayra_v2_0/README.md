# 🤖 AYRA – Voice Based AI Assistant

AYRA is a Python-based personal AI voice assistant inspired by Jarvis.  
It can **listen to your voice**, **process commands**, **think using AI**, **stores the chat history**, and **speak back** like a real assistant.

---

## 📁 Project Folder Structure

```bash
ayra_v2_0/
│
├── AiCONTROL/
│   ├── __init__.py
│   └── control.py
│
├── BRAIN/
│   ├── __init__.py
│   └── brain.py
│
├── MEMORY/
│   ├── __init__.py
│   ├── history.json
│   └── memory.py
│
├── Voice/
│   ├── __init__.py
│   ├── LISTEN.py
│   └── SPEAK.py
│
└── main.py

## ✨ Features

- 🎤 **Voice Recognition** (Speech Input)
- 🤖 **AI Responses** using Google Generative AI
- 🔊 **Voice Output** using `pyttsx3`
- 🧠 **Brain Module** to think and generate replies
- 💾 **History System** using JSON
- 🎮 **Control System** for voice commands

---

## ⚙️ How AYRA Works

1. 🎙️ Listens through microphone using `SpeechRecognition`
2. 🧠 Sends text to **Google Gemini**
3. 🎮 Understands commands inside `AiCONTROL`
4. 💾 Saves chat history in `MEMORY/history.json`
5. 🔊 Speaks the response using `pyttsx3`

