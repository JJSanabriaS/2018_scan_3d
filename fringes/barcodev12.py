import barcode
from barcode.writer import ImageWriter
import PIL
from PIL import Image
import tkinter as tk
# https://raspberrypi.stackexchange.com/questions/14518/sending-live-data-readings-from-raspberry-pi-to-laptop
# https://stackoverflow.com/questions/46726757/capture-and-send-jpeg-images-from-raspberry-pi-to-pc-socket-python
# https://stackoverflow.com/questions/56056422/how-to-continuously-send-images-from-raspberry-to-pc-without-delay

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bar_class = barcode.get_barcode_class('code128')
                                      #code128')

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
