import re
from utils.configs import height, width
from os import system, get_terminal_size

# util components

def padding_left():
    term_w: int = get_terminal_size().columns
    return " ".rjust(int(term_w/2)-int(width/2))

def padding_top():
    term_h: int = get_terminal_size().lines
    for i in  range(int(term_h/2) - int(height/2) - 3 ):
        print("")

def top_line(w = width-2):
    print(padding_left(),end="")
    print("╔", end="")
    for i in range(w): print("═", end="")
    print("╗")

def middle_line(w = width-2):
    print(padding_left(),end="")
    print("╠", end="")
    for i in range(w): print("═", end="")
    print("╣")

def empty_line(w = width - 2):
    print(padding_left(),end="")
    print("║", end="")
    for i in range(w): print(" ", end="")
    print("║")

def bottom_line(w = width-2):
    print(padding_left(), end="")
    print("╚", end="")
    for i in range(w): print("═", end="")
    print("╝")

def text_line(value, w=width-3, end=""):
    txt_w = len(re.sub(r"\u001B\[[;\d]*m", "",value))
    end_w = len(re.sub(r"\u001B\[[;\d]*m", "",end))
    print(padding_left(), end='')
    print("║ "+value, end="")
    for i in range(w - txt_w - end_w):
        print(" ", end="")
    print(end, end="")
    print("║")

def center_text_line(value, w=width, end=""):
    txt_w = len(re.sub(r"\u001B\[[;\d]*m", "",value))
    end_w = len(re.sub(r"\u001B\[[;\d]*m", "",end))

    print(padding_left(), end="")
    print("│", end="")
    padding = int((w - txt_w) / 2)
    for i in range(padding - 1): print(" ", end="")

    print(value, end="");
    if (txt_w % 2 == w % 2): padding -= 1

    for i in range(padding - end_w): print(" ", end="")
    print(end, end="")
    print("│")

