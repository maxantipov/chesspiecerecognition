from PIL import Image, ImageDraw, ImageOps, ImageChops
from chess_recognition import Board

def find_border(im):
    w,h = im.size
    a,b,c,d = -1,-1,-1,-1

    #convierto en blanco lo que sea gris
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            if (r != 0 and r != 255):
                im.putpixel((i,j),(255,255,255))

    for i in range(w):
        r,g,b = im.getpixel((w/2,i))
        if r != 255:
            a = i
            break

    for i in range(h):
        r,g,b = im.getpixel((i,h/2))
        if r != 255:
            b = i
            break

    for i in range(w-1,0,-1):
        r,g,b = im.getpixel((i,w/2))
        print i,r
        if r != 255:
            c = i
            break

    for i in range(h-1,0,-1):
        r,g,b = im.getpixel((h/2,i))
        if r != 255:
            d = i
            break

    print(a,b,c,d)
    img = im.crop((a,b,c,d))
    img.show()


im = Image.open("pieces/board_w_pieces.png","r")
im.convert("RGB").convert("1")
w,h = im.size
for i in range(1,8):
    fila = w*i/8
    columna = w*i/8
    drawF = ImageDraw.Draw(im)
    drawF.line((0,fila,w,fila),fill="#0000FF")
    drawC = ImageDraw.Draw(im)
    drawC.line((columna,0,columna,h),fill="#0000FF")

find_border(im)


#inverts the colors of an image white <-> black ;-)
#might be useful to check for pieces on black squares
# im2 = ImageOps.invert(im)
# im.show()
# im2.show()


