# ColoredASCIIArtGenerator

## Overview
This is a Python based Program, that allows you to select an JPEG-Image to convert it in
colored ASCII-Art. You have to expirement with the scale, it depends on the image size.

**An Example of my dog Billie (you might need to zomm a little bit):**
![example](https://user-images.githubusercontent.com/85063182/120223571-0f953980-c242-11eb-8d32-759769036d34.png)

## References
This python script requires you to install Pillow. Pillow can be found here: https://pypi.org/project/Pillow/
If you don't want to do that, then you can use the executable that was generated using Auto-Py-To-Exe, wich
you can find here: https://pypi.org/project/auto-py-to-exe/
And don't worry, it's a false positive virus, a common known problem with Auto-Py-To-Exe.

## Note
You can also make this work on Linux by replacing line 14 with:
```python
font = PIL.ImageFont.truetype("font.ttf")
```
And then you just need to put your desired font as font.ttf into the directory. You also need to install tkinter
for Linux if you haven't already.
```
sudo apt update
sudo apt-get install python3-tk
```
