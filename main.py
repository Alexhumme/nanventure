from os import system, get_terminal_size, terminal_size
from typing import Literal

height = 20
width = 50
floor = 5

class Item ():
    def __init__(self, imap, pos) -> None:
        self.pos: tuple = pos
        self.imap: list = self.process_imap(imap)
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
                
                cell: str = self.imap[i][j]
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
                if cell != " ":
                    if (cell in ["╭","─","╮","╰","╯","│"]) : new_cell += "\033[32m"
                    elif (cell in ["*"]) : new_cell += "\033[31m"
                    else: new_cell += "\033[33m"
                new_cell += cell
                if cell!=" ": new_cell += "\033[0m"
                new_row.append(new_cell)
            
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

def topping():
    term_h: int = get_terminal_size().lines
    for i in  range(int(term_h/2) - int(height/2) - 3 ):
        print("")


system("clear")
topping()

print(padding(),end="")
print("╔", end="")
for i in range(width-2): print("═", end="")
print("╗")

for i in range(height-2):
    print(padding(), end='')
    if (i == height - floor): print("╟", end="")
    else: print("║", end="")
    
    for j in range(width-2):
        if (draw_bg_items((i,j))) : continue
        elif (i == height - floor): print("─", end="")
        else : print(" ", end="")

    if (i == height - floor): print("╢")
    else: print("║")

options = [
    "Move",
    "Exit",
]

print(padding(),end="")
print("╠", end="")
for i in range(width-2): print("═", end="")
print("╣")

opt_btn_widht = int((width-2) / len(options))

print(padding(), end="")
print("║ ", end="")
for i, option in enumerate(options):
    r_pad = 4
    if i != 0: r_pad -= 1
    print("┌", end="")
    for i in range(opt_btn_widht-r_pad): print("─", end="")
    print("┐ ", end="")
print("║")


print(padding(), end="")
print("║ ", end="")
for i, option in enumerate(options):
    r_pad = 5
    if i != 0: r_pad -= 1 
    print("│ "+option, end="")
    for i in range(opt_btn_widht- len(option) - r_pad): print(" ", end="")
    print("│ ", end="")
print("║")

print(padding(), end="")
print("║ ", end="")
for i, option in enumerate(options):
    r_pad = 4
    if i != 0: r_pad -= 1
    print("└", end="")
    for i in range(opt_btn_widht-r_pad): print("─", end="")
    print("┘ ", end="")
print("║")

print(padding(), end="")
print("╚", end="")
for i in range(width-2): print("═", end="")
print("╝")
