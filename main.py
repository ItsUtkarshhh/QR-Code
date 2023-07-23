# Importing Modules!
import qrcode
from PIL import Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Changing the Current working directory!


# Defining QR Generating function :
def generateQR(*args) :
    data = text.get()
    if data :
        img = qrcode.make(data) # Qr Code
        resize_image = img.resize((280,250))
        tkimage = ImageTk.PhotoImage(resize_image)
        qrcanvas.delete("all")
        qrcanvas.create_image(0,0,anchor=tk.NW, image=tkimage)
        qrcanvas.image = tkimage
    else :
        messagebox.showwarning("Error", "Enter some data first!")

# Defining QR Saving function :
def saveQR(*args) :
    data = text.get()
    if data :
        img = qrcode.make(data)
        resize_image = img.resize((280,250))
        path =filedialog.asksaveasfilename(defaultextension=".png")
        if path :
            resize_image.save(path)
            messagebox.showinfo("Success", "QR Generated")
    else :
        messagebox.showwarning("Error", "Enter some data first!")

# Creating the main dialogue box and setting its height, width and bg color :
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("320x390")
root.config(bg="white")
root.resizable(0,0) # Due to this, the dialogue box will have a fixed dimensions

# Adding 2 frames, frame1 for the main QR Cover and Image, and another frame2 for user input
frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=10, width=300,height=270)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=290, width=300,height=75)

# Adding specifications to the frame1 content :
cover_img = tk.PhotoImage(file="QR Code Generator.png")
qrcanvas = tk.Canvas(frame1)
qrcanvas.create_image(0,0,anchor=tk.NW, image=cover_img)
qrcanvas.image = cover_img
qrcanvas.bind("<Double-1>", saveQR)
qrcanvas.pack(fill=tk.BOTH)

# Adding specifications to frame2 content :
text = ttk.Entry(frame2,width=23, font="Georgia", justify=tk.CENTER)
text.bind("<Return>", generateQR)
text.place(x=5,y=5)

# Adding buttons :
# Adding Create button :
btn1 = ttk.Button(frame2, text="Create",width=10, command=generateQR)
btn1.place(x=15, y=40)

# Adding Save button :
btn2 = ttk.Button(frame2, text="Save",width=10, command=saveQR)
btn2.place(x=110, y=40)

# Adding Exit button :
btn3 = ttk.Button(frame2, text="Exit",width=10, command=root.quit)
btn3.place(x=205, y=40)

# Executing the program :
root.mainloop()