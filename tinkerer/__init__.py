class TinkererMenu(object):

    def __init__(self, atendant):
        self.atendant = atendant

    def show(self):
        self.atendant.say("== Tinkerer Toolkit ==")
        self.atendant.silence()
        self.atendant.say("Please choose one of the actions below")
        self.atendant.say("1. Run all scripts")
        self.atendant.say("2. Archlinux")
        self.atendant.say("3. Neovim")
        self.atendant.say("---")
        self.atendant.say("0. Quit")
        self.atendant.silence()
        option = self.atendant.ask("Please enter the desired option: ")



