import tkinter as tk
from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox

class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # tk.Frame.__init__(self, parent, bg="blue", height=250, width=300)
        # filename = PhotoImage(file = "bg.jpg")
        # background_label = tk.Label(self, image=filename)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="User Login", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        

        cleartextbutton = tk.Button(self)
        cleartextbutton.place(relx=0.34, rely=0.53, height=33, width=86)
        cleartextbutton.configure(pady="0")
        cleartextbutton.configure(text='''Clear''', command=self._clear_fields)

        UsernameLabel = ttk.Label(self)
        UsernameLabel.place(relx=0.22, rely=0.35, height=34, width=85)
        UsernameLabel.configure(text='''Username:''')

        PasswordLabel = ttk.Label(self)
        PasswordLabel.place(relx=0.22, rely=0.42, height=34, width=79)
        PasswordLabel.configure(text='''Password:''')

        self.UsernameEntry = Entry(self)
        self.UsernameEntry.place(relx=0.34, rely=0.37, relheight=0.04, relwidth=0.28)

        self.PasswordEntry = Entry(self, show="*")
        self.PasswordEntry.place(relx=0.34, rely=0.44, relheight=0.04, relwidth=0.28)

        self.loginbutton = tk.Button(self, text="Log in", command=self._authentication)
        self.loginbutton.place(relx=0.51, rely=0.53, height=33, width=76)
        self.loginbutton.configure(pady="0")

    def _authentication(self):
        # if self.UsernameEntry.get() == "user" and self.PasswordEntry.get() == "pass":
        #     self.controller.show_frame("userMenu")
        # elif self.UsernameEntry.get() == "admin" and self.PasswordEntry.get() == "pass":
        #     self.controller.show_frame("manager")

        try:
            conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
        except:
            print ("I am unable to connect to the database.")
            
        cur = conn.cursor()
        try:
            username = "'" + self.UsernameEntry.get() + "'"
            password = self.PasswordEntry.get()
            getUser = "SELECT * FROM USERS WHERE usernames LIKE " + username + ";"
            cur.execute(getUser)
            saveuser = cur.fetchall()
            print (saveuser[0][3])
            if(saveuser != []):
                if(password == saveuser[0][2] ):
                    if(saveuser[0][3] == True):
                        self.controller.show_frame("manager")
                    else:
                        
                        self.controller.show_frame("userMenu")
                else:
                    print("Failed Inner")
                    messagebox.showerror("Login Fail", "Username or Password incorrect")
            else:
                messagebox.showerror("Login Fail", "Username or Password incorrect")
                print("Failed Outer")   
            
        except:
            print ("I can't drop our test database!")

    def _clear_fields(self):
        self.UsernameEntry.delete(0, 'end')
        self.PasswordEntry.delete(0, 'end')
