from tkinter import *
from PIL import ImageTk, Image
from cat_get import get_cat

root = Tk()
root.iconbitmap('cat_icon.ico')
root.title('MEEEEEEOOOOOWWW')

img = ImageTk.PhotoImage(Image.open("cat.png"))
myLabel = Label(root, image = img)
myLabel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()