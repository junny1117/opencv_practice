import tkinter as tk
from tkinter import Button, Frame, Label, Tk, filedialog
from PIL import Image, ImageTk, ImageFilter
import os


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select image file", filetypes=(("PNG file", "*.png"),
                                                                                ("JPG file", "*.jpg"),
                                                                                ("JPEG file", "*.jpeg"),
                                                                                ("ALL file", "*.txt")))
    importedimage = Image.open(filename)
    importedimage = importedimage.resize((380, 320), Image.LANCZOS)  # Resize the image to fit the frame
    importedimage = ImageTk.PhotoImage(importedimage)
    lbl.configure(image=importedimage)
    lbl.image = importedimage  # Keep a reference to avoid garbage collection

def blurimage():
    image1 = Image.open(filename)
    bluredimage = image1.filter(ImageFilter.BLUR)
    bluredimage = ImageTk.PhotoImage(bluredimage)
    lbl.configure(image=bluredimage, width=380, height=320)
    lbl.image = bluredimage

def contourimage():
    image2 = Image.open(filename)
    contouredimage = image2.filter(ImageFilter.CONTOUR)
    contouredimage = ImageTk.PhotoImage(contouredimage)
    lbl.configure(image=contouredimage, width=380, height=320)
    lbl.image = contouredimage

def embossimage():
    image3 = Image.open(filename)
    embossedimage = image3.filter(ImageFilter.EMBOSS)
    embossedimage = ImageTk.PhotoImage(embossedimage)
    lbl.configure(image=embossedimage, width=380, height=320)
    lbl.image = embossedimage

def restartimage():
    lbl.configure(image=importedimage, width=380, height=320)
    lbl.image = importedimage
    

window = Tk()
window.title("OpenCV")
window.geometry("900x500+100+100")
window.configure(bg="#e2f9b8")


img = Image.open("test.png")
img = img.resize((70, 100), Image.LANCZOS)
photo_img = ImageTk.PhotoImage(img)


window.iconphoto(False, photo_img)


Label(window, image=photo_img, bg="#fff").place(x=10, y=10)


Label(window, text="OPENCV", font="arial 30 bold", fg="yellow", bg="#e2f9b8").place(x=90, y=50)


selectimage = Frame(window, width=400, height=400, bg="#d6dee5")
selectimage.place(x=10, y=120)


f = Frame(selectimage, bg="black", width=380, height=320)
f.place(x=10, y=10)


lbl = Label(f, bg="black")
lbl.place(x=0, y=0)


Button(selectimage, text="Select image", width=12, height=2, font="arial 14 bold", command=showimage).place(x=10, y=340)
transformationsection = Frame(width=440, height=510, bg="#939f5c")
transformationsection.place(x=450, y=10)

Label(transformationsection, text="Filters:", font="arial 20 bold", fg="#fff", bg="#939f5c").place(x=10, y=10)

Button(transformationsection, text="BLUR", width=12, height=2, font="arial 14 bold", command=blurimage).place(x=10,
                                                                                                              y=50)
Button(transformationsection, text="CONTOUR", width=12, height=2, font="arial 14 bold", command=contourimage).place(x=155, y=50)
Button(transformationsection, text="EMBOSS", width=12, height=2, font="arial 14 bold", command=embossimage).place(x=300, y=50)
Button(selectimage, text="Restart", width=12, height=2, font="arial 14 bold", command=restartimage).place(x=260, y=340)

# Start the main loop
window.mainloop()
