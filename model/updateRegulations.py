from tkinter import ttk
import tkinter as tk
import psycopg2


class updateRegulations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Edit Regulations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.SpeciesEntryLabel = tk.Label(self)
        self.SpeciesEntryLabel.place(relx=0.2, rely=0.22, height=26, width=100)
        self.SpeciesEntryLabel.configure(text='''Species''')

        self.max = tk.Label(self)
        self.max.place(relx=0.4, rely=0.22, height=26, width=100)
        self.max.configure(text='''Maximum %''')

        self.maxEntry = tk.Entry(self)
        self.maxEntry.place(relx=0.4, rely=0.3, height=26, width=100)

        self.min_len = tk.Label(self)
        self.min_len.place(relx=0.6, rely=0.22, height=26, width=100)
        self.min_len.configure(text='''Minimum Length''')

        self.minEntry = tk.Entry(self)
        self.minEntry.place(relx=0.6, rely=0.3, height=26, width=100)

        self.CurrentRegValue = tk.Label(self)
        self.CurrentRegValue.place(relx=0.57, rely=0.58, height=26, width=10)

        # comboBOXXXXXXXX
        try:
            conn = psycopg2.connect(host="localhost", database="hackathontest", user="postgres",
                                    password="thuytrang080599")
        except:
            print("I am unable to connect to the database.")

        
        cur = conn.cursor()

        try:
            getSpecies = "SELECT DISTINCT species_name FROM fishspecies;"
            cur.execute(getSpecies)
            listOfSpecies = cur.fetchall()
            self.combobox = ttk.Combobox(self, textvariable=listOfSpecies[0], )
            self.combobox.place(relx=0.15, rely=0.3)
            self.combobox.config(values=(listOfSpecies))
        except:
            pass

        self.backButton = tk.Button(self, command=lambda: controller.show_frame("manager"))
        self.backButton.place(relx=0.055, rely=0.92, height=33, width=150)
        self.backButton.configure(text='''Back''')
        self.backButton.configure(width=86)
