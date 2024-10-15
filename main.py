import asyncio as aio
import keyboard
import time
from os import system
from utils.utils import *
from elements.elements import *


def draw_bg_elements(pos):
    return any(element.draw_bit(pos) for element in elements)

# util # scene components

def draw_game():
    for i in range(height-2):
        print(padding_left(), end='')
        if (i == height - floor): print("╟", end="")
        else: print("║", end="")

        for j in range(width-2):
            if (draw_bg_elements((i,j))) : continue
            elif (i == height - floor): print("─", end="")
            else : print(" ", end="")

        if (i == height - floor): print("╢")
        else: print("║")

options = [
    "Move",
    "Exit",
]

def draw_opts():
    opt_btn_widht = int((width-2) / len(options))

    print(padding_left(), end="")
    print("║ ", end="")
    for i, option in enumerate(options):
        r_pad = 4
        if i != 0: r_pad -= 1
        print("┌", end="")
        for i in range(opt_btn_widht-r_pad): print("─", end="")
        print("┐ ", end="")
    print("║")


    print(padding_left(), end="")
    print("║ ", end="")
    for i, option in enumerate(options):
        r_pad = 5
        if i != 0: r_pad -= 1
        print("│ "+option, end="")
        for i in range(opt_btn_widht- len(option) - r_pad): print(" ", end="")
        print("│ ", end="")
    print("║")

    print(padding_left(), end="")
    print("║ ", end="")
    for i, option in enumerate(options):
        r_pad = 4
        if i != 0: r_pad -= 1
        print("└", end="")
        for i in range(opt_btn_widht-r_pad): print("─", end="")
        print("┘ ", end="")
    print("║")

def draw_scene(buffer, x, y):
    buffer[y][x] = 'A'
    # Muestra el buffer en la consola
    system('clear')
    padding_top()
    for row in buffer:
        print(padding_left(), end="")
        print("-".join(row))

def run():
    width, height = 20, 10
    buffer = [['.' for _ in range(width)] for _ in range(height)]
    x, y = 0, 5
    while True:
        draw_scene(buffer, x, y)
        time.sleep(0.1)
        # Borra el aventurero de su posición anterior
        buffer[y][x] = ' '
        x = (x + 1) % width  # Mueve al aventurero de forma circular

class Nanventure():
    def __init__(self) -> None:
        self.exit = False
        self.scene = 0
        self.second = 0
        self.main_menu_opt = 0
        self.main_menu_opts: list = [
            ("New game", lambda: (self.set_scene(1))),
            ("Local PvP", (lambda: print("hola"))),
            ("Exit", self.run_exit)
        ]

    def run_exit(self):
        self.exit = True

    def set_scene(self, id):
        self.scene = id

    def scene_game(self):

        top_line()

        draw_game()

        middle_line()

        draw_opts()

        bottom_line()

    def sc0_handle_input(self):
        if (keyboard.is_pressed("down")):
            self.main_menu_opt = (self.main_menu_opt + 1) % len(self.main_menu_opts)
        if (keyboard.is_pressed("up")):
            self.main_menu_opt = (self.main_menu_opt - 1) % len(self.main_menu_opts)
        if (keyboard.is_pressed("enter")): self.main_menu_opts[self.main_menu_opt][1]()

    def scene_main_menu(self):

        self.sc0_handle_input()

        top_line()
        center_text_line("\033[1;34mMAIN MENU\033[0m")
        middle_line()

        empty_line()
        for index, opt in enumerate(self.main_menu_opts):
            if (index == self.main_menu_opt): text_line("\033[44;30m  ▶ "+opt[0], end="\033[0m ")
            else: text_line(" ■ "+opt[0])
            empty_line()

        bottom_line()

    def draw_scene(self):

        if self.scene == 0: self.scene_main_menu()
        elif self.scene == 1: self.scene_game()

    def draw_second(self):
        secs = "second: "+str(self.second)
        top_line(len(secs)+2)
        text_line("second: "+str(self.second), len(secs)+1)
        bottom_line(len(secs)+2)

    def run(self):
        while True:

            system("clear")
            padding_top()

            self.draw_second()

            self.draw_scene()

            if self.exit: break

            self.second += 1

            time.sleep(0.1)

def main():
    print("\033[?1049h")
    Nanventure().run()
    print("\033[?1049l")

if __name__ == "__main__": main()
