from PIL import Image, ImageDraw
import random

maxi = 150

def iterations(c):
    z = 0
    n = 0
    while abs(z) < 2 and n < maxi:
        z = z**2 + c
        n += 1
    return n

width = 800
height = 600

rstart = -2.25
rend = 1.25
istart = -1.25
iend = 1.25

im = Image.new('HSV', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(width):
    for y in range(height):
        c = complex(rstart + (x / width) * (rend - rstart), istart + (y / height) * (iend - istart))
        fr = iterations(c)
        h = int(255 * fr / maxi)
        if fr < maxi:
            v = 255
        else:
            v = 0

        draw.point([x, y], (h, 255, v))

im.convert('RGB').save('mandelbrot.png', 'PNG')
