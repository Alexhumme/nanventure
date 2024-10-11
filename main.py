from os import system, get_terminal_size, terminal_size
from typing import Literal

height = 20
width = 31
floor = 5

class Item ():
    def __init__(self, imap, pos) -> None:
        self.pos: tuple = pos
        self.imap: list = imap
        pass
    def process_imap(self, imap) -> list: 
        return imap
    def draw_bit(self, bitpos: tuple) -> bool:
        active_cell = False
        cell_value = ""
        bit_y, bit_x = bitpos
        my_y, my_x = self.pos
        for i in range(len(self.imap)):
            for j in range(len(self.imap[i])):
                
                cell = self.imap[i][j]
                if cell != " " and my_x + j == bit_x and my_y + i == bit_y: 
                    active_cell = True
                    cell_value: str = cell
                if active_cell: break
            if active_cell: break

        if active_cell: print(cell_value, end="")
        return active_cell
    pass

class Tree (Item):
    def __init__(self, imap, pos) -> None:
        super().__init__(imap, pos) 
    
    def process_imap(self, imap):
        new_imap = []

        for row in imap:
            new_row = []

            for cell in row:
                new_cell = ""
                #if (cell == ╭──────╮)
                new_cell += cell
                new_cell += "\033[0m"
            
            new_imap.append(new_row)

        return new_imap
    pass

items: list[Item] = [
    Tree(
        [
            "╭──────╮  ",
            "│    * │  ",
            "│ *  ╭───╮",
            "╰────│   │",
            "  ╘╣║╰───╯",
            "   ╨╨     ",
        ],
        (height - floor - 5, int(width/2) - 5)
    )
]

def draw_bg_items(pos):
    return any(item.draw_bit(pos) for item in items)


def padding():
    term_w: int = get_terminal_size().columns
    return " ".rjust(int(term_w/2)-int(width/2))

print(padding(),end="")
print("┏", end="")
for i in range(width-2): print("━", end="")
print("┓")

for i in range(height-2):
    print(padding(), end='')
    if (i == height - floor): print("┠", end="")
    else: print("┃", end="")
    
    for j in range(width-2):
        if (draw_bg_items((i,j))) : continue
        elif (i == height - floor): print("─", end="")
        else : print(" ", end="")

    if (i == height - floor): print("┨")
    else: print("┃")

print(padding(),end="")
print("┗", end="")
for i in range(width-2): print("━", end="")
print("┛")


