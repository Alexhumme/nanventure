from elements.Element import Element
from elements.Tree import Tree
from utils.configs import *

elements: list[Element] = [
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
