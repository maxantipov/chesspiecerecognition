from chess_recognition import Board
from PIL import Image
import os,sys

def get_board_coords(image):
    #todo: find board in image
    b = board(0,0,0,0)
    return b

def load_board(board):
    for square in board:
        pass


def get_piece_in_square(square):
    pass


if __name__ == "__main__":
    pass

def init(path_to_file):
       if os.path.isfile(path_to_file):
           actualBoard = Board(path_to_file)
           actualBoard.getBoardFromImage()
path_to_file = "pieces/board_w_pieces.png"
init(path_to_file)