import tkinter as tk

class startPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("login"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("userMenu"))
        button3 = tk.Button(self, text="Go to Page Three",
                            command=lambda: controller.show_frame("manager"))
        button1.pack()
        button2.pack()
        button3.pack()
