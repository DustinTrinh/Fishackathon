import tkinter as tk

class userMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Home", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        Connect_and_Show_Graph = tk.Button(self)
        Connect_and_Show_Graph.place(relx=0.32, rely=0.38, height=43, width=236)
        Connect_and_Show_Graph.configure(text='''Connect Device and Show Graph''', command=self._show_graph)

        logout = tk.Button(self, command=lambda: controller.show_frame("login"))
        logout.place(relx=0.82, rely=0.04, height=33, width=93)
        logout.configure(text='''Log out''')

        username = tk.Label(self)
        username.place(relx=0.03, rely=0.04, height=36, width=122)

    def _show_graph(self):
        self.controller.show_frame("graphData")
