from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root.title("Register")
        self.root.geometry("900x500+100+100")
        self.root.resizable(False, False)

         # Register Frame
        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=50, y=50, width=350, height=350)
        
        # Title
        title = Label(Frame_register, text="Register", font=("Impact", 24, "bold"), fg="black")
        title.place(x=90, y=30)

        # Subtitle
        subtitle = Label(Frame_register, text="Register page", font=("Goudy old style", 15, "bold"), fg="black")
        subtitle.place(x=90, y=70)

root = Tk()
obj = Register(root)
root.mainloop()
