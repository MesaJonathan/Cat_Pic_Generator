from tkinter import *
from PIL import ImageTk, Image
from cat_get import get_cat
import threading

get_cat()

root = Tk()
root.iconbitmap('cat_icon.ico')
root.title('MEEEEEEOOOOOWWW (hit space bar for new kitty)')

img = ImageTk.PhotoImage(Image.open("cat.jpg"))
myLabel = Label(root, image = img)
myLabel.pack(side = "bottom", fill = "both", expand = "yes")

def callback(e):
    get_cat()
    img2 = ImageTk.PhotoImage(Image.open('cat.jpg'))
    myLabel.configure(image=img2)
    myLabel.image = img2

root.bind("<space>", callback)

root.mainloop()