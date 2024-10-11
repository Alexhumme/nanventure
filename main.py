from os import system, get_terminal_size, terminal_size

height = 20
width = 31
floor = 5

class Item ():
    pass

class Tree (imap, pos):
    pass

items: list = [
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

def draw_fore_items(pos):
    for item in items:
        item.draw(pos)
    pass

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
        if (i == height - floor): print("─", end="")
        elif draw_fore_items((i,j)): continue
        else: print(" ", end="")
    if (i == height - floor): print("┨")
    else: print("┃")

print(padding(),end="")
print("┗", end="")
for i in range(width-2): print("━", end="")
print("┛")


