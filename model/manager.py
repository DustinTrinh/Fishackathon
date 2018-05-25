import tkinter as tk

class manager(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Admin Home", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        Connect_and_Show_Graph = tk.Button(self)
        Connect_and_Show_Graph.place(relx=0.3, rely=0.36, height=43, width=236)
        Connect_and_Show_Graph.configure(text='''Connect Device and Show Graph''')

        logout = tk.Button(self, command=lambda: controller.show_frame("login"))
        logout.place(relx=0.82, rely=0.04, height=33, width=93)
        logout.configure(text='''Log out''')

        username_label = tk.Label(self)
        username_label.place(relx=0.03, rely=0.04, height=36, width=122)
        username_label.configure(text='''Welcome admin!''')

        UpdateRegulationButton = tk.Button(self, command=lambda: controller.show_frame("updateRegulations"))
        UpdateRegulationButton.place(relx=0.3, rely=0.82, height=33, width=236)
        UpdateRegulationButton.configure(text='''Update Regulation''')
        UpdateRegulationButton.configure(width=236)

    def _add_member(self):
        pass
