# this code is what makes raw images into templates, which is then
# put into the template.png file using GIMP with the help of guides
# to make positioning accurate
#
# thank you to Aurora Aquir for uploading this code to Discord during
# r/place '22
# if there's another source i will update these comments
#
# Indie Alliance ftw

from PIL import Image

path = "pre-overlay.png"
new_path = "overlay.png"

im = Image.open("pre-overlay.png")
width, height = im.size
pixels = im.load()
new_img = Image.new("RGBA", (width*3,height*3), color = (0,0,0,0))


for x in range(width):
    for y in range(height):
        new_img.putpixel((1+3*x,1+3*y), pixels[x,y])
        
new_img.save(new_path)