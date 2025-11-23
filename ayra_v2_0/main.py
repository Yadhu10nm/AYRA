from AiCONTROL.control import Control
from Voice.LISTEN import Listen



class AYRA:
    def __init__(self):
        self.control = Control()
        self.mic = Listen()

    def control_flow(self):
        def voice():
            while True:
                text = self.mic.listening()
                res = self.control.Ctrl(text)
                if res is None:
                   break
        def type_inp():
            while True:
                text = int("Enter : ").lower()
                res = self.control.Ctrl(text)
                if res is None:
                   break
        ch = int(input("press \n 1 - Mic\n 2 - Typing : "))
        if ch == 1:
            voice()
        else:
            type_inp()

if __name__ == "__main__":
    ayra = AYRA()
    ayra.control_flow()
    print("Thank you !")