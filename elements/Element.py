class Element ():
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


