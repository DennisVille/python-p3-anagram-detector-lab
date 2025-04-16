# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, l):
        results = [i for i in l if sorted(list(i)) == sorted(list(self.word))]
        return results
