import tkinter as tk
from tkinter import *
import requests
import cv2
import numpy as np
import imutils

w = 1200
h = 650

class mainform:
    def __init__(self, master):
        self.master = master
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar)
        self.products.add_command(label="Add")
        self.products.add_command(label="Edit")
        self.products.add_command(label="Remove")

        self.menubar.add_cascade(menu=self.products, label="Product")

        self.categories = Menu(self.menubar)
        self.categories.add_command(label="Add")
        self.categories.add_command(label="Edit")
        self.categories.add_command(label="Remove")

        self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------ #
        def ipwebcam():
            url = "http://10.1.41.26:8080/shot.jpg"
            while True:
                img_resp = requests.get(url)
                img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
                #print(img_arr)
                img = cv2.imdecode(img_arr, -1)
                # print(img)
                img = imutils.resize(img, width=1000, height=1800)

                cv2.imshow("Android_cam", img)
                # Press Esc key to exits
                if cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()

        def printinput():
            inp=self.inputtxt.get(1.0,"end-1c")
            
            if(inp=="2240"):
                self.lblf.config(text = "Provided Input: "+inp)
                ipwebcam()
            else:
                self.lblf.config(text = "Provided Input is invalid!!: "+inp)
                

           

        self.master.config(menu=self.menubar, bg="#ecf0f1")
        #self.lbl = tk.Label(self.master, text='Main Form', font=('verdana',50, 'bold'), fg='#2A2C2B',bg="#ecf0f1")
        #self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)
        self.inputtxt=tk.Text(self.master,height=5,width=20)
        self.inputtxt.pack()
        self.done=tk.Button(self.master,text="DONE",command=printinput)
        self.done.pack()
        self.lblf = tk.Label(self.master, text = "")
        self.lblf.pack()


