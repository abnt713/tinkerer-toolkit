from tinkerer import TinkererMenu
from tinkerer.atendants import CommandLineAtendant


if __name__ == "__main__":
    menu = TinkererMenu(CommandLineAtendant())
    menu.show()
