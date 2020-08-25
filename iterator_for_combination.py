class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.chars = characters
        self.combination = list(range(combinationLength))
        self.combination[-1] -= 1
        n = len(characters)
        self.final = list(range(n - combinationLength, n))
        

    def next(self):
        """
        :rtype: str
        """
        i = len(self.combination) - 1
        while self.combination[i] == self.final[i]:
            i -= 1
        self.combination[i] += 1
        for j in range(i+1, len(self.combination)):
            self.combination[j] = self.combination[j - 1]+1
        return "".join(self.chars[i] for i in self.combination)
 

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.combination != self.final
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()