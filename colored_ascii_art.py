#imports
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import math

from tkinter import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

#values
palette = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
font = PIL.ImageFont.truetype('C:\\Windows\\Fonts\\Tahoma.ttf')

#method for finding a char out of the palette
def getChar(value):
    return list(palette)[math.floor((len(list(palette)) / 256) * value)]

#loading values
progress = 0

#method to translate an image into colored ascii art
def translateImage(file, scale, outfile):
    isnt_progressing = False
    #loading image
    print("Loading Image...")
    im = PIL.Image.open(file)

    #resizeing image
    print("Resizeing Image...")
    width, height = im.size
    im = im.resize((int(scale * width), int(scale * height)), PIL.Image.NEAREST)

    #loading pixels
    print("Loading Pixels...")
    width, height = im.size
    pixels = im.load()

    #output image file instance
    print("Creating Output-Image Instance...")
    output = PIL.Image.new('RGB', (10 * width, 10 * height), color = (0, 0, 0))
    draw = PIL.ImageDraw.Draw(output)

    #calculate chars
    progress = 0
    amount_of_pixels = width * height
    amount_calculated = 0
    one_percent = amount_of_pixels / 100
    print("Calculating Chars...")
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            draw.text((j * 10, i * 10), getChar(h), font = font, fill = (r, g, b))
            amount_calculated = amount_calculated + 1
            print("Calculated: {} of {}".format(amount_calculated, amount_of_pixels))
            progress = int(amount_calculated / one_percent)
            bar = "▒▒▒▒▒▒▒▒▒▒"
            if progress >= 10:
                bar = "▓▒▒▒▒▒▒▒▒▒"
            if progress >= 20:
                bar = "▓▓▒▒▒▒▒▒▒▒"
            if progress >= 30:
                bar = "▓▓▓▒▒▒▒▒▒▒"
            if progress >= 40:
                bar = "▓▓▓▓▒▒▒▒▒▒"
            if progress >= 50:
                bar = "▓▓▓▓▓▒▒▒▒▒"
            if progress >= 60:
                bar = "▓▓▓▓▓▓▒▒▒▒"
            if progress >= 70:
                bar = "▓▓▓▓▓▓▓▒▒▒"
            if progress >= 80:
                bar = "▓▓▓▓▓▓▓▓▒▒"
            if progress >= 90:
                bar = "▓▓▓▓▓▓▓▓▓▒"
            if progress >= 100:
                bar = "▓▓▓▓▓▓▓▓▓▓"
            progress_text.set("Progress: {}% {}".format(progress, bar))
            root.update_idletasks()

    #save output image as file
    print("Writing ASCII Art as Image...")
    output.save(outfile)

    #show that the program finished
    print("Done!")
    create_art_button.config(text = "Done!")
    isnt_progressing = True

#window
root = Tk()

#window settings   
root.title("Colored ASCII Art")
root.geometry("500x265")
root.resizable(0, 0)

#values
progress_text = StringVar()
first_update = True
isnt_progressing = True
image_file = "None"
image_outfile = "None"
image_scale = 0.1

#Create Art Button
def click_create_art_button():
    global first_update
    if first_update and isnt_progressing:
        create_art_button.config(text = "Processing...")
        translateImage(image_file, image_scale, image_outfile)
        first_update = False
    else:
        root.destroy()

create_art_button = Button(root, height = 2, width = 15, text = "Create Art", command = click_create_art_button)
create_art_button.place(x = 182, y = 215)

#input label
input_label = Label(root, text = "Input: {}".format(image_file.split("/")[len(image_file.split("/")) - 1]))
input_label.config(font=("Times New Roman", 14))
input_label.place(x = 10, y = 60)

#output label
output_label = Label(root, text = "Output: {}".format(image_outfile.split("/")[len(image_outfile.split("/")) - 1]))
output_label.config(font=("Times New Roman", 14))
output_label.place(x = 10, y = 95)

#scale label
scale_label = Label(root, text = "Scale: {}".format(image_scale))
scale_label.config(font=("Times New Roman", 14))
scale_label.place(x = 10, y = 130)

#select file
def click_select_image_button():
    global image_file
    dialog = fd.askopenfile(filetypes = (("JPEG File","*.jpg"),("Something","*.*")), title = "Select Image (should be .jpg)")
    if dialog is None:
        image_file = "None"
    else:
        image_file = dialog.name
    print("Input:", image_file)
    input_label.config(text = "Input: {}".format(image_file.split("/")[len(image_file.split("/")) - 1]))

select_image_button = Button(root, height = 2, width = 15, text = "Select Image", command = click_select_image_button)
select_image_button.place(x = 62, y = 10)

#select outfile
def click_select_outimage_button():
    global image_outfile
    dialog = fd.asksaveasfilename(filetypes = (("PNG File","*.png"),("Something","*.*")), title = "Select Location where the ASCII Art should be saved as .png")
    if dialog == "":
        image_outfile = "None"
    else:
        image_outfile = dialog
        if image_outfile.endswith(".png") == False:
            image_outfile = image_outfile + ".png"
    print("Ouput:", image_outfile)
    output_label.config(text = "Output: {}".format(image_outfile.split("/")[len(image_outfile.split("/")) - 1]))

select_outimage_button = Button(root, height = 2, width = 15, text = "Select Output", command = click_select_outimage_button)
select_outimage_button.place(x = 182, y = 10)

#select scale
def click_select_scale_button():
    global image_scale
    image_scale = sd.askfloat("Enter Scale:", "Current: {}".format(image_scale))
    print("Scale:", image_scale)
    scale_label.config(text = "Scale: {}".format(image_scale))

select_scale_button = Button(root, height = 2, width = 15, text = "Select Scale", command = click_select_scale_button)
select_scale_button.place(x = 302, y = 10)

#progress label
progress_label = Label(root, textvariable = progress_text)
progress_text.set("Progress: 0% ▒▒▒▒▒▒▒▒▒▒")
progress_label.config(font=("Times New Roman", 14))
progress_label.place(x = 125, y = 175)

#mainloop of root
root.mainloop()
