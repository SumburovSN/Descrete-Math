class Derangement:
    '''
    Derangement(word) creates the list of derangement of symbols in the word
    (https://en.wikipedia.org/wiki/Derangement)
    Derangement is built since the instantiation
    At the start list of possible symbols for each position is created to use
    it in the build_derangement stage
    '''
    def __init__(self, word):
        self.word = word
        self.possibles = []
        self.form_possibles()
        self.derangement = []
        self.build_derangement(0, '')

    def form_possibles(self):
        for symbol in self.word:
            self.possibles.append(self.word.replace(symbol, ''))

    def build_derangement(self, position, begin=''):
        for symbol in self.possibles[position]:
            if symbol not in begin:
                if position == len(self.possibles) - 1:
                    self.derangement.append(begin + symbol)
                else:
                    self.build_derangement(position + 1, begin + symbol)


if __name__ == '__main__':

    my_suit = Derangement('abcdef')

    # print(my_suit.possibles)
    print(my_suit.derangement)
    print(len(my_suit.derangement))
