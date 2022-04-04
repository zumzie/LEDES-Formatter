from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import csv

root = Tk()
root.title('Merus - LEDES Formatter')
root.geometry("500x450")





class Elder:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
        self.myButton = Button(master, text="Open", command=self.open_text)
        self.myButton.pack(pady=20)
        self.myButton = Button(master, text="Reformat", command=self.reformat_text)
        self.myButton.pack(pady=20)
        self.my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
        self.my_text.pack(pady=20)
        self.rows = []
        self.text_data = []

    def open_text(self):
        self.text_path = filedialog.askopenfilename(initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
        self.text_file = open(self.text_path, 'r')
        if self.text_file is not None:
           with open(self.text_path) as fi:
                self.text_data = list(tuple(fi))



        

        self.stuff = self.text_file.read()
        self.my_text.insert(END, self.stuff)
        self.text_file.close()

    def reformat_text(self):
        self.data = [("csv file(*.csv)","*.csv"),('All types(*.*)', '*.*')]
        self.file = filedialog.asksaveasfilename(filetypes = self.data, defaultextension = self.data)
        # file will have file name provided by user.
        # Now we can use this file name to save file.
        with open(self.file, mode='w', newline='') as csv_file:
            report_writer = csv.writer(csv_file, dialect='excel')
            for row in list(self.text_data):
                row = row.split("|") 
                lst_row = list(row)
                print(row)
                row = tuple(lst_row)
                self.rows.append(row)
                report_writer.writerow(row)



e = Elder(root)
root.mainloop()
