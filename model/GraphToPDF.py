import os
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

logo = ImageReader("graph.png") 
canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
now = datetime.datetime.now()
#left value is HORIZONTALLY
canvas.setFont('Helvetica', 40)
canvas.drawString(120,750,'Fish Capture Report')
canvas.setFont('Helvetica', 15)
canvas.drawString(20,700,'Ship Name')
canvas.drawString(20,680, 'Longtitude')
canvas.drawString(20,660,'Latitude')
canvas.drawString(20,640,now.strftime("%Y-%m-%d %H:%M:%S"))
canvas.drawImage(logo,110, 300, width=450, height=300) #first one is to move left right, second is up and down.
canvas.drawString(160,250,'Logistics : ')
canvas.drawString(230,250,'Logistics Info ')
canvas.drawString(160,230,'Logistics : ')
canvas.drawString(230,230,'Logistics Info ')
canvas.drawString(160,210,'Logistics : ')
canvas.drawString(230,210,'Logistics Info ')


canvas.setFont('Helvetica', 30)
canvas.drawString(110,100,'Final Decision: ')
#connect the decision here and display in the box below
canvas.drawString(340,100,'Yes / No ')
canvas.save()
os.startfile('form.pdf')