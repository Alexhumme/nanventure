from elements.Element import Element

class Tree (Element):
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


