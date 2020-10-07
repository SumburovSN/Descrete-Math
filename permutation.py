class Permutation:
    '''
    Permutation(word) creates the list of permutations of symbols in the word
    Permutations are built since the instantiation
    '''
    def __init__(self, word):
        self.word = word
        self.permutations = []
        self.build_permutations(word)

    def __str__(self):
        '''
        function to format output self.permutation
        :return: self.permutation in the format like {a, b, c, d}, {a, b, d, c}, etc.
        '''
        result = ''
        for word in self.permutations:
            result += '{'
            for symbol in word:
                result += symbol + ", "
            result = result[0: -2]
            result += '}, '
        return result[0: -2]

    def build_permutations(self, rest, begin=''):
        for symbol in rest:
            if len(rest) == 1:
                self.permutations.append(begin + symbol)
                return
            else:
                self.build_permutations(rest.replace(symbol, ''), begin + symbol)


if __name__ == '__main__':

    my_suit = Permutation('abcd')

    print(my_suit.permutations)
    print(str(my_suit))

