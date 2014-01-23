import os, sys
from PIL import Image
class Board:
    
    def __init__(self,board_path):
        self.board_path = board_path
        self.cord_a = 0
        self.cord_b = 0
        self.cord_c = 0
        self.cord_d = 0
        
    def getBoardFromImage(self):
        pngfileBoard = Image.open(self.board_path)
        print pngfileBoard.size, pngfileBoard.format 
        #now, read pixel by pyxel and get the coords.
        #...
        #...
        #...




