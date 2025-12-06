# 🌙 Ayra — Voice Interactive AI Assistant (v3.0)

Ayra 3.0 is a **real-time conversational AI assistant** built using **Gemini**, with memory support, speech-based interaction, and a live UI that plays an animated character while speaking.  
Designed to feel alive — Ayra listens, thinks, speaks and responds like a companion.

---

## 🚀 Features

| Feature | Status |
|--------|--------|
| 🔊 Voice Recognition (Speech → Text) | ✔ |
| 🤖 Gemini-based Chatbot | ✔ |
| 🧠 Chat Memory using JSON | ✔ |
| 🎬 Live UI + Continuous Video Playback | ✔ |
| 🧵 Multithreading for smooth performance | ✔ |
| 🔈 Text-to-Speech Output (TTS) | ✔ |

---

## 🏗 Tech Stack

| Technology | Usage |
|-----------|--------|
| **Python** | Core logic |
| **Google Generative AI (Gemini)** | Text generation / chatbot |
| **SpeechRecognition** | Capturing microphone input |
| **pyttsx3** | TTS output |
| **Tkinter** | UI + video rendering |
| **JSON** | Local chat memory storage |

---

## 🔥 How Ayra Works

1. **Ayra listens** using the `speech_recognition` library.  
2. The captured voice is processed into text.  
3. Parsed text is sent to **Gemini API**, where Ayra generates the response.  
4. Response is spoken aloud using **pyttsx3 TTS engine**.  
5. Meanwhile, **Tkinter UI plays a looping character animation/video** during speech.  
6. All tasks run using **threading**, ensuring no UI freeze during conversation.  

Ayra behaves like an AI companion — replies instantly, speaks naturally and feels interactive.

---



