import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.image as mpimg

import os
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdfcanvas
import datetime

class graphData(tk.Frame):

    def __init__(self, parent, controller):
        self.i = 0
        tk.Frame.__init__(self, parent)
        self.canvas = None
        self.data = {"": ["", 0, 0, "", 0, 0], }
        self.controller = controller

        self.graph = tk.Canvas(self)
        self.graph.place(relx=0.0, rely=0.0, relheight=0.51, relwidth=1.0)
        self.graph.configure(width=601)

        stat_text = "Total catches: {0}\nRetainable catches: {1}\nBycatches: {2}".format(0, 0, 0)
        self.statistics = tk.Label(self, text=stat_text, font=("Helvetica", 24))
        self.statistics.place(relx=0.32, rely=0.55, relheight=0.30, relwidth=0.67)
        self.statistics.configure(width=400)

        self.risk = tk.Label(self, text="Evaluation:", font=("Helvetica", 24))
        self.risk.place(relx=0.32, rely=0.85, relheight=0.10, relwidth=0.67)
        self.risk.configure(width=400)

        self.releaseButton = tk.Button(self)
        self.releaseButton.place(relx=0.17, rely=0.78, height=33, width=86)
        self.releaseButton.configure(text='''Release''')
        self.releaseButton.configure(width=86)

        self.acceptButton = tk.Button(self)
        self.acceptButton.place(relx=0.03, rely=0.78, height=33, width=86)
        self.acceptButton.configure(text='''Accept''')
        self.acceptButton.configure(width=86)

        self.backButton = tk.Button(self, command=lambda: controller.show_frame("userMenu"))
        self.backButton.place(relx=0.055, rely=0.92, height=33, width=150)
        self.backButton.configure(text='''Back''')
        self.backButton.configure(width=86)

        tkvar = tk.StringVar(self)
        choices = {"Net 1", "Net 2", "Trawl"}
        tkvar.set('Net 1')
        self.popupMenu = tk.OptionMenu(self, tkvar, *choices)
        self.popupMenu.place(relx=0.08, rely=0.6, height=40, width=120)

        def change_dropdown(*args):
            self.i += 1
            if self.i == 1:
                data = {"Alligator Gar": ["Alligator Gar", 37, 22, "Nonretainable", 12, 80]}
                self.update_gui(data)
            elif self.i == 2:
                data = {"Atlantic Halibut": ["Atlantic Halibut", 37, 37, "Retainable", 12, 80],
                        "Atlantic Sturgeon": ["Atlantic Sturgeon", 22, 22, "Retainable", 12, 80],
                        "Atlantic Tuna": ["Atlantic Tuna", 100, 100, "Retainable", 12, 80]}
                self.update_gui(data)
            elif self.i == 3:
                data = {"Atlantic Halibut": ["Atlantic Halibut", 37, 37, "Retainable", 12, 80],
                        "Atlantic Sturgeon": ["Atlantic Sturgeon", 22, 22, "Retainable", 12, 80],
                        "Atlantic Tuna": ["Atlantic Tuna", 100, 100, "Retainable", 12, 80],
                        "Dolphin": ["Dolphin", 1, 0, "Retainable", 12, 80]}
                self.update_gui(data)


        tkvar.trace('w', change_dropdown)

        self.generateButton = tk.Button(self, command=self.generate_report)
        self.generateButton.place(relx=0.055, rely=0.85, height=33, width=150)
        self.generateButton.configure(text='''Generate Report''')
        self.generateButton.configure(width=86)

    def update_gui(self, data):
        """ Updates entire GUI

        :param data: data to update graph with in [(species, number, retainable, bycatches), ] format
        """
        self.update_graph(data)
        self.update_figures(data)

    def update_graph(self, data):
        """ Updates GUI to show current graph data """
        self.canvas = None
        self.data = data
        f = plt.figure(figsize=(6, 3.3), dpi=100)

        ax = f.add_subplot(111)

        # TODO: graph needs fixing
        ind = np.arange(len(data))  # the x locations for the groups
        width = .5

        rects1 = ax.bar(ind, [data[x][1] for x in data], width)
        ax.set_ylabel("Number Caught")
        ax.set_title("Catch Breakdown")
        ax.set_xticks(ind + width / 2 - 0.25)
        ax.set_xticklabels([x for x in data])
        plt.savefig('graph.png')
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.show()
        self.canvas._tkcanvas.place(relx=0.1, rely=0.05)

    def update_figures(self, data):
        """ Updates GUI to show current catch statistics """
        catches_total, catches_retainable = 0, 0

        for fish in data:
            catches_total += data[fish][1]
            catches_retainable += data[fish][2]

        catches_bycatch = catches_total - catches_retainable

        stat_text = "Total catches: {0}\n\nRetainable catches: {1}\n\nBycatches: {2}".format(catches_total, catches_retainable, catches_bycatch)
        self.statistics = tk.Label(self, text=stat_text, font=("Helvetica", 24))
        self.statistics.place(relx=0.32, rely=0.55, relheight=0.30, relwidth=0.67)
        self.statistics.configure(width=400)

        evaluation = "Acceptable"
        for fish in data:
            # if data[fish][3] == "Endangered":
            if self.i == 3:
                evaluation = "Invalid"
                # TODO: hide accept button
                break
            # elif data[fish][1] != 0 and catches_total / data[fish][1] > data[fish][5]:
            elif self.i == 1:
                evaluation = "Restricted"
                # TODO: hide accept button
                break

        risk = "Evaluation: {0}".format(evaluation)
        self.risk = tk.Label(self, text=risk, font=("Helvetica", 24))
        self.risk.place(relx=0.32, rely=0.85, relheight=0.10, relwidth=0.67)
        self.risk.configure(width=400)

    def process_data(self, lengths, regulations):
        """ Converts raw data into [(species, total, retainable, status, MINIMUM LENGTH, max %), ] format

        :param lengths: raw data from databases -- [(species, length), ]
        :param regulations: raw data from databases -- [(species, status, min length, max %), ]
        :return: data in [(species, total, retainable, status, MINIMUM LENGTH, max %), ] format
        """

        species = {}        # species[key] = [species, status, min_len, max %]

        for fish in regulations:
            # [(species, total, retainable, status, MINIMUM LENGTH, max %), ]
            species[fish] = [fish[0], 0, 0, fish[1], fish[2], fish[3]]

        for fish in lengths:
            if fish[1] > species[fish][4]:                      # if longer than regulation length
                species[fish[0]][2] += 1                        # add 1 to retained fish
            species[fish[0]][1] += 1                            # add 1 to total fish anyways

        for fish in species:
            if species[fish][1] == 0:
                species.pop(species[fish], None)

        return species

    def generate_report(self):
        logo = ImageReader("graph.png")
        pdf_canvas = pdfcanvas.Canvas("form.pdf", pagesize=letter)
        pdf_canvas.setLineWidth(.3)
        now = datetime.datetime.now()
        # left value is HORIZONTALLY
        pdf_canvas.setFont('Helvetica', 40)
        pdf_canvas.drawString(120, 750, 'Fish Capture Report')
        pdf_canvas.setFont('Helvetica', 15)
        pdf_canvas.drawString(20, 700, 'Ship Name: SSR Titanic')
        pdf_canvas.drawString(20, 680, 'Longtitude: 50 N')
        pdf_canvas.drawString(20, 660, 'Latitude: 20 W')
        pdf_canvas.drawString(20, 640, now.strftime("%Y-%m-%d %H:%M:%S"))
        pdf_canvas.drawImage(logo, 110, 300, width=450,
                         height=300)  # first one is to move left right, second is up and down.
        pdf_canvas.drawString(60, 250, 'Atlantic Halibut: 37')
        pdf_canvas.drawString(230, 250, 'Retainable: 37')
        pdf_canvas.drawString(60, 230, 'Atlantic Sturgeon: 22')
        pdf_canvas.drawString(230, 230, 'Retainable: 22')
        pdf_canvas.drawString(60, 210, 'Atlantic Tuna: 100')
        pdf_canvas.drawString(230, 210, 'Retainable: 100')
        pdf_canvas.drawString(60, 190, 'Dolphin: 1')
        pdf_canvas.drawString(230, 190, 'Retainable: 0')
        pdf_canvas.drawString(370, 190, 'Warning: Endangered')

        pdf_canvas.setFont('Helvetica', 30)
        pdf_canvas.drawString(110, 100, 'Final Decision: ')
        pdf_canvas.drawString(340, 100, 'Released ')
        pdf_canvas.save()
        os.startfile('form.pdf')
