# -*- coding: utf-8 -*-

from PIL import Image, ImageChops, ImageDraw

def main():
    img = Image.open("inputs/hello.png")
    img = img.resize((d * 2 for d in img.size))
    if img.width > 108:
        img = img.crop((0, 0, 108, img.height))
    origsize = img.size
    scale = 16
    img = img.resize((d * scale for d in img.size))
    img.putpalette([0xaa] * 3 + [0xff] * 3)
    img = img.convert("RGB")
    grid = Image.new(img.mode, img.size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    color = (112//2, 0xdd, 0xee)
    for ox in range(origsize[0]):
        x = ox * scale
        draw.line((x, 0, x, img.height),
                  fill=color,
                  width=1 + (ox % 5 == 0))
    for oy in range(origsize[1]):
        y = oy * scale
        draw.line((0, y, img.width, y),
                  fill=color,
                  width=1 + (oy % 5 == 0))
    img = ImageChops.multiply(img, grid)
    img.save("hello.png")

if __name__ == "__main__":
    main()
