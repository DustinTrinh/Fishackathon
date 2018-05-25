# #============================================================================
# # Login Part
# # import psycopg2
# # from tkinter import messagebox
# # # # Try to connect

# # try:
# #     conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
# # except:
# #     print ("I am unable to connect to the database.")
    
# # cur = conn.cursor()
# # try:
# #     username = "'admin'"
# #     password = "pass"
# #     getUser = "SELECT * FROM USERS WHERE usernames LIKE " + username + ";"
# #     cur.execute(getUser)
# #     saveuser = cur.fetchall()
# #     print (saveuser[0][3])
# #     if(saveuser != []):
# #         if(password == saveuser[0][2] ):
# #             if(saveuser[0][3] == True):
# #                 print ("okayla")
# #                 print (saveuser)
# #             else:
# #                 print ("Nowayla")
# #                 print (saveuser)
# #         else:
# #             print("Failed Inner")
# #             messagebox.showerror("Login Fail", "Username or Password incorrect")
# #     else:
# #         messagebox.showerror("Login Fail", "Username or Password incorrect")
# #         print("Failed Outer")   
    
# # except:
# #     print ("I can't drop our test database!")

# #=============================================================================================
# #Grab the 2 arrays

# # import psycopg2
# # from tkinter import messagebox
# # # Try to connect

# # try:
# #     conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
# # except:
# #     print ("I am unable to connect to the database.")
    
# # cur = conn.cursor()

# # try:

# #     getCatchData = "SELECT species_id, lenghth FROM catchdetails;"
# #     getFishData = "SELECT species_id, min_len FROM fishspecies;"
# #     cur.execute(getCatchData)
# #     saveCatch = cur.fetchall()
# #     cur.execute(getFishData)
# #     saveFish = cur.fetchall()
# #     print("This is save catch")
# #     print (saveCatch)
# #     print ("This is save fish")
# #     print(saveFish)
# # #saveCAtch and saveFish are the 2 arrays u want
# # except:
# #     print ("I can't drop our test database!")

# #================================================================================
# #For edit Regulation page
# #After the Edit button is clicked 
# #Grab the Entry and search for the species through name or ID

# # import psycopg2
# # from tkinter import messagebox
# # # Try to connect

# # try:
# #     conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
# # except:
# #     print ("I am unable to connect to the database.")
    
# # cur = conn.cursor()

# # try:

# #     # getCatchData = "SELECT species_id, lenghth FROM catchdetails;"
# #     # getFishData = "SELECT species_id, min_len FROM fishspecies;"
# #     # cur.execute(getCatchData)
# #     # saveCatch = cur.fetchall()
# #     # cur.execute(getFishData)
# #     # saveFish = cur.fetchall()
# #     checkWhich = 0
# #     saveFish = []
# #     saveSpecies = []
# #     findFishName = "110"  # "'" + entry.get "'"
# #     findFishID = "110" #entry.get()
# #     searchFish = "SELECT min_len FROM fishspecies WHERE species_name LIKE INITCAP(" + "'%" + findFishName + "%');"
# #     cur.execute(searchFish)
# #     saveSpecies = cur.fetchall()
# #     if(saveSpecies == []):
# #         checkWhich = 0

# #     elif (saveSpecies != []):
# #         checkWhich = 1

# #     else:
# #         searchFishID = "SELECT min_len FROM fishspecies WHERE species_id " + "=" + findFishID + ";"
# #         cur.execute(searchFishID)
# #         saveFish = cur.fetchall()
# #         if(saveFish == []):
# #             checkWhich = 0
# #         else:
# #             checkWhich = 2
    
# #     if(checkWhich == 0):
# #         messagebox.showerror("Cannot Find Species", "Input Error")
# #     else: 
# #         pass
# #         #We gonna create LABEL say CURRENT REGULATION and show the current regulation
# #         #We gonna create LABEL say NEW REGULATION and show ENTRY for new regulation
# #         #THEN PUSH IT TO DATABASE

# #         #newRegulation = newRegulationEntry.get()

# #         # if(checkWhich == 1):
# #         #     updateRegulation = "UPDATE TABLE fishspecies SET min_len" + "=" + newRegulation + "WHERE " +  findFishName + " LIKE INITCAP(" + "'%" + findFishName + "%');"
# #         # else:
# #         #     updateRegulation = "UPDATE TABLE fishspecies SET min_len" + "=" + newRegulation + "WHERE " +  findFishID + "=" + findFishID + ";"
# # except:
# #     print ("I can't drop our test database!")

# #Grab the 2 arrays

# import psycopg2
# from tkinter import messagebox
# # Try to connect

# try:
#     conn = psycopg2.connect(host="localhost",database="hackathontest", user="postgres", password="thuytrang080599")
# except:
#     print ("I am unable to connect to the database.")
    
# cur = conn.cursor()

# try:

#     getLength = "SELECT species_name, lenghth FROM catchdetails WHERE CATCH_ID" + "=1;"
#     getRegulation = "SELECT species_name, category, min_len, max_percentage FROM fishspecies;"
#     cur.execute(getLength)
#     saveLength = cur.fetchall()
#     cur.execute(getRegulation)
#     saveRegulation = cur.fetchall()
#     print("This is save catch")
#     print (saveLength[0][0])
#     print ("This is save fish")
#     print(saveRegulation)
# #saveCAtch and saveFish are the 2 arrays u want
# except:
#     print ("I can't drop our test database!")
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

app = Tk()
app.title("Welcome")
image2 =Image.open('./graph.png')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))
#app.configure(background='C:\\Usfront.png')
#app.configure(background = image1)


label1 = Label(app, image=image1,
               font=("Times New Roman", 24),
               justify=CENTER, height=500, width=660, fg="blue")
label1.pack()

app.mainloop()