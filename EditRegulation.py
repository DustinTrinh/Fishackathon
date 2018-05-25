from tkinter import *
from tkinter import ttk
import tkinter as tk
import psycopg2
class EditRegulation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.37, rely=0.07, height=33, width=155)
        self.Label1.configure(text='''Edit Regulation''')

        self.SpeciesEntryLabel = tk.Label(self)
        self.SpeciesEntryLabel.place(relx=0.27, rely=0.22, height=26, width=63)
        self.SpeciesEntryLabel.configure(text='''Species :''')

        self.EditSpeciesButton = tk.Button(self)
        self.EditSpeciesButton.place(relx=0.43, rely=0.4, height=33, width=114)
        self.EditSpeciesButton.configure(text='''Edit Regulation''')

        self.CurrentRegValue = tk.Label(self)
        self.CurrentRegValue.place(relx=0.57, rely=0.58, height=26, width=10)

        #comboBOXXXXXXXX
        try:
            conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
        except:
            print ("I am unable to connect to the database.")
            
        cur = conn.cursor()

        try:
            getSpecies = "SELECT DISTINCT species_name FROM fishspecies;"
            cur.execute(getSpecies)
            listOfSpecies = cur.fetchall()
            self.combobox = ttk.Combobox(self, textvariable = listOfSpecies[0], )
            self.combobox.place_configure(relx=0.57, rely=0.58)
            self.combobox.pack()
            self.combobox.config(values = (listOfSpecies))
            
        except:
            pass
        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.15, rely=0.53, relheight=0.41, relwidth=0.74)
        self.Frame1.place_forget()

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.16, rely=0.16, height=26, width=133)
        self.Label2.configure(text='''Current Regulation:''')

        self.currentRegLabel = tk.Label(self.Frame1)
        self.currentRegLabel.place(relx=0.52, rely=0.16, height=26, width=10)


        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.2, rely=0.43, height=26, width=115)
        self.Label4.configure(text='''New Regulation:''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.49, rely=0.43, relheight=0.13, relwidth=0.14)
        #regulationentry

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.43, rely=0.76, height=33, width=61)
        self.Button1.configure(text='''Update''')

