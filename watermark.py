import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from PIL import ImageFont
from PIL import ImageDraw

# create the root window
root = tk.Tk()
root.title('Watermark Adder')
root.resizable(False, False)
root.geometry('300x150')
def show_canvas(photo):
    root.geometry('500x500')
    canv = tk.Canvas(root, width=280, height=280, bg='white')
    canv.place(relx=0.5, rely=0.6, anchor="center")
    

    img = ImageTk.PhotoImage(photo)  
    canv.create_image(20, 20,anchor="nw", image=img)
    root.mainloop()
    

def watermark(photo):
    draw = ImageDraw.Draw(photo)
    w, h = photo.size
    x, y = int(w / 1.5), int(h / 1.1)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
   
    font = ImageFont.truetype("arial.ttf", int(font_size/6))
    draw.text((x, y), "MD Photo", fill=(255, 255, 255), font=font, anchor='ms')
    
def select_file():
    global filename
    filetypes = [("JPEG files", "*.jpg"), ("PNG files", "*.png")]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    if filename:
        root.geometry('500x500')
        canv = tk.Canvas(root, width=280, height=280, bg='white')
        canv.place(relx=0.5, rely=0.6, anchor="center")
        open_button.place(relx=0.5, rely=0.05, anchor="center")
        addmark_button.place(relx=0.5, rely=0.1, anchor="center")
        img = ImageTk.PhotoImage((Image.open(filename)).resize((250,250), Image.LANCZOS))  
        canv.create_image(20, 20,anchor="nw", image=img)
        root.mainloop()
    
def add_watermark():
    global watermark_image
    image = Image.open(filename)
    image=image.resize((250,250),Image.LANCZOS)
    watermark_image = image.copy()
    save_button.place(relx=0.5, rely=0.15, anchor="center")
    watermark(watermark_image)
    
    show_canvas(watermark_image)

def save_button():
    errorlabel= tk.Label(text="You have to add watermark")
    if watermark_image:
        image = Image.open(filename)
        watermark(image)
        f = fd.asksaveasfile(initialfile = 'Untitled.jpg',
        defaultextension=".jpg",filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if f is None:
            return
        image.save(f)
        
    else:
        errorlabel.place(relx=0.5, rely=0.2, anchor="center")
    
    

# buttons
open_button = ttk.Button(
    root,
    text='Open a photo',
    command=select_file
)
addmark_button = ttk.Button(
    root,
    text='Add watermark to a file',
    command=add_watermark
)
save_button = ttk.Button(
    root,
    text='Save file',
    command=save_button
)



open_button.place(relx=0.5, rely=0.2, anchor="center")

# run the application
root.mainloop()