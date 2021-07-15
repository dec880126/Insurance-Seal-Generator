from PIL import Image, ImageDraw, ImageFont
import datetime
import os

# Route Setting
cwd = os.getcwd()
# C:\\Users\\CyuanHuang\\Pictures\\test\\app\\
img_src = cwd + "\\input.jpg"
img_save_dir = cwd + "\\output.jpg"

# Load image
img = Image.open(img_src)
draw = ImageDraw.Draw(img)

# Font
myfont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size = 59)
fillcolor = "#3f48cc"
width, height = img.size

# Get date and transfer to Calendar of R.O.C
x = datetime.datetime.now()
year = int(x.year) - 1911

# Get time
month = int(x.month)
day = int(x.day)
hour = int(x.hour)
minute = int(x.minute)

# Resize time
if month < 10:
    month = "0" + str(month)
if day < 10:
    day = "0" + str(day)
if hour < 10:
    hour = "0" + str(hour)
if minute < 10:
    minute = "0" + str(minute)

# Drawing
draw.text((26, 200), str(year) + "." + str(month) + "." + str(day) + "  " + str(hour) + ":" + str(minute), font = myfont, fill = fillcolor)

# Save image
try:
    img.save(img_save_dir,"jpeg")
    print(f"保險受理章輸出成功 -> 路徑為: {img_save_dir}")
    os.system("pause")
except:
    print("Error of save image")