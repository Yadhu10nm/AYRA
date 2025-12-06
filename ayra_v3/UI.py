import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

from AiCONTROL.control import Control
from Voice.LISTEN import Listen


# ================= AYRA CLASS =================
class AYRA:
    bool_ = False

    def __init__(self):
        self.control = Control()
        self.mic = Listen()

    def control_flow(self):
        while True:
            AYRA.bool_ = False
            text = self.mic.listening()
            if text is not None:
                AYRA.bool_ = True
                res = self.control.Ctrl(text)

                if res is None:
                    break


# ========== SETTINGS ==========
video_path = r"C:\PROJECTS\AYRA_\ayra-jarvis\ayra_v3\video_2.mp4"
window_width = 600
window_height = 600
# ==============================


# ---------- CONDITION FUNCTION ----------
def my_condition():
    return AYRA.bool_

# =================== VIDEO UI ===================
class VideoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Video UI")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)

        self.label = tk.Label(root)
        self.label.pack(fill="both", expand=True)

        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            print("Video not found!")
            self.root.destroy()
            return

        self.paused = True
        self.show_first_frame()

        self.root.bind("<Escape>", self.exit_app)

        self.update_video()

    def show_first_frame(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (window_width, window_height))
            self.show_frame(frame)

    def update_video(self):
        if my_condition():
            self.paused = False
            ret, frame = self.cap.read()

            if not ret:
                # restart video from beginning
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = self.cap.read()

            if ret:
                frame = cv2.resize(frame, (window_width, window_height))
                self.show_frame(frame)

        else:
            # ✅ pause + reset when condition is False
            if not self.paused:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                self.show_first_frame()
                self.paused = True

        self.root.after(30, self.update_video)

    def show_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

    def exit_app(self, event=None):
        if self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

# =================== MAIN ===================
if __name__ == "__main__":
    # run background logic
    ayra = AYRA()
    t1 = threading.Thread(target=ayra.control_flow)
    t1.daemon = True
    t1.start()

    # start UI
    root = tk.Tk()
    app = VideoUI(root)
    root.mainloop()