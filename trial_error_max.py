from PIL import Image, ImageDraw, ImageOps, ImageChops
from chess_recognition import Board


def convert_to_bw(im):
    im.convert("RGB")
    im.convert("1")
    w,h = im.size
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            if brightness < 20:
                im.putpixel((i,j),(0,0,0))
            else:
                im.putpixel((i,j),(255,255,255))


#input: image
#returns image cropped to board size
def find_border (im):
    w,h = im.size
    a1,a2,b1,b2 = -1,-1,-1,-1

    #convert to b/w
    convert_to_bw(im)

    im.show()

    #convert grey pixels to white
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            if (r != 0 and r != 255):
                im.putpixel((i,j),(255,255,255))

    im.show()

    for i in range(w):
        r,g,b = im.getpixel((w/2,i))
        if r != 255:
            a1 = i
            break

    for i in range(h):
        r,g,b = im.getpixel((i,h/2))
        if r != 255:
            a2 = i
            break

    for i in range(w-1,0,-1):
        r,g,b = im.getpixel((i,w/2))
        if r != 255:
            b1 = i
            break

    for i in range(h-1,0,-1):
        r,g,b = im.getpixel((h/2,i))
        if r != 255:
            b2 = i
            break

    print(a1,a2,b1,b2)
    img = im.crop((a1+1,a2+1,b1,b2))
    return img


def load_board_from_image(file_path):
    im = Image.open(file_path,"r")
    im = find_border(im)
    w,h = im.size

    #draws lines on squares limits (calculated from image h/w)
    for i in range(1,8):
        fila = w*i/8
        columna = w*i/8
        drawF = ImageDraw.Draw(im)
        drawF.line((0,fila,w,fila),fill="#0000FF")
        drawC = ImageDraw.Draw(im)
        drawC.line((columna,0,columna,h),fill="#0000FF")

    return im

load_board_from_image("pieces/board_w_pieces.png").show() #works
load_board_from_image("pieces/board1.jpg").show() #fails converting to b/w


#inverts the colors of an image white <-> black ;-)
#might be useful to check for pieces on black squares
# im2 = ImageOps.invert(im)
# im.show()
# im2.show()


