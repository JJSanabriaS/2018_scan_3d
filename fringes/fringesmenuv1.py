
import barcode
from barcode.writer import ImageWriter
import PIL
from PIL import Image
import tkinter as tk
#from tkinter import tk, Button, Canvas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys
import webbrowser
import numpy as np
from LightPipes import *
import math
import warnings


#if sys.version_info[0] < 3:
#    from Tkinter import *
#    import Tkinter as Tk
#    import tkMessageBox,tk, Button, Canvas
#else:
#    from tkinter import *
#    import tkinter as tk
#    from tkinter import messagebox,Button, Canvas



# https://raspberrypi.stackexchange.com/questions/14518/sending-live-data-readings-from-raspberry-pi-to-laptop
# https://stackoverflow.com/questions/46726757/capture-and-send-jpeg-images-from-raspberry-pi-to-pc-socket-python
# https://stackoverflow.com/questions/56056422/how-to-continuously-send-images-from-raspberry-to-pc-without-delay


warnings.filterwarnings("ignore")
tipo=input("    tipo fringe (1 barcode fixed/2 polar circle/3 turtle circle/ simple circles )   ")
if (tipo=="1"):
             root = tk.Tk()
             screen_width = root.winfo_screenwidth()
             screen_height = root.winfo_screenheight()
             bar_class = barcode.get_barcode_class('code128')                                      #code128')
             barcode = '1234567890'
             writer=ImageWriter()
             code128 = bar_class(barcode, writer)
             code128.save('filename', options={"write_text": False}) # save the originally generated image
             to_be_resized = Image.open('filename.png') # open in a PIL Image object
             newSize = (screen_width, screen_height) # new size will be 500 by 300 pixels, for example
             resized = to_be_resized.resize(newSize, resample=PIL.Image.NEAREST) # you can choose other :resample: values to get different quality/speed results
             resized.save('filename_resized.png') # save the resized image
             im = Image.open("filename_resized.png")
             #show image
             im.show()
elif (tipo=="2"):
             cm = 1/2.54  # centimeters in inches
             fig=plt.figure(figsize=(12.8*cm, 9.6*cm))
             #fig=plt.figure(figsize=cm2inch(12.8, 9.6))
             ax = fig.add_subplot(111, polar=True)
             #ax.plot([1.0,1.5], [5,5], color='r', linestyle='-')
             for i in range(1,20):
                ax.plot(np.linspace(0, 2*np.pi, 100), np.ones(100)*0.0001*i, color='black', linestyle='-', linewidth=1)
                
             plt.show()
elif (tipo=="3"):
             import turtle
             turtle.setup(800,600)
             board = turtle.Turtle()
             radio =15
             for i in range(1,20):
                #print("...Running code ...",i)
                #print(i)
                board.circle(i*radio)
                #board.sety(-i*radio) # en esta posicion crea una linea visible de descenso
                board.penup()
                board.sety(-i*radio)
                board.pendown()
                board.pensize(1) # pensize default =1 

             turtle.done()
elif (tipo=="4"):
    #circle1 = plt.Circle((0.5, 0.5), 0.2, color='black', fill=False, linewidth=18)
    #circle2 = plt.Circle((0.5, 0.5), 0.3, color='black', fill=False)
    #circle3 = plt.Circle((0.5, 0.5), 0.4, color='black', clip_on=False, fill=False)
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax = plt.gca()
    # change default range so that new disks will work
    ax.axis("equal")
    ax.set_xlim((-15, 15))
    ax.set_ylim((-15, 15))
    # (or if you have an existing figure)
    # fig = plt.gcf()
    # ax = fig.gca()
    for i in range(0,10,1):
        circle = plt.Circle((0.5, 0.5), 1*i, color='black', fill=False, linewidth=5)
        ax.add_patch(circle)


    #ax.add_patch(circle2)
    #ax.add_patch(circle3)
    fig.show()
    #fig.savefig('plotcircles.png')
    

            

             
           
