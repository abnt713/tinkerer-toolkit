class Atendant(object):

    def say(self, sentence):
        pass

    def ask(self, question):
        pass

    def silence(self):
        pass


class CommandLineAtendant(Atendant):

    def say(self, sentence):
        print(sentence)

    def ask(self, question):
        input(question)

    def silence(self):
        print('')

