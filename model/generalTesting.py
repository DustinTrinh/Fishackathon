import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from PIL import ImageTk,Image
from graphData import graphData
from login import login
from manager import manager
from startPage import startPage
from userMenu import userMenu
from updateRegulations import updateRegulations


class SampleApp(tk.Tk):

    def __init__(self, model=None, *args, **kwargs):

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["startPage"] = startPage(container, self)
        self.frames["startPage"].grid(row=0, column=0, sticky="nsew")

        self.frames["login"] = login(container, self)
        self.frames["login"].grid(row=0, column=0, sticky="nsew")

        self.frames["userMenu"] = userMenu(container, self)
        self.frames["userMenu"].grid(row=0, column=0, sticky="nsew")

        self.frames["manager"] = manager(container, self)
        self.frames["manager"].grid(row=0, column=0, sticky="nsew")

        self.frames["graphData"] = graphData(container, self)
        self.frames["graphData"].grid(row=0, column=0, sticky="nsew")

        self.frames["updateRegulations"] = updateRegulations(container, self)
        self.frames["updateRegulations"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    root = Tk()
    root.geometry("727x684+500+100")
    SampleApp()
    mainloop()
