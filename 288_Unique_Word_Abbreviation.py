from collections import Counter
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.word_pool = Counter(dictionary)
        self.res = {}
        for i in range(len(dictionary)):
            if len(dictionary[i])<=2:
                key = dictionary[i]
            else:
                key = dictionary[i][0]+str(len(dictionary[i])-2)+dictionary[i][-1]
            if key in self.res:
                self.res[key] += 1
            else:
                self.res[key] = 1        

    def isUnique(self, word: str) -> bool:
        if word in self.word_pool:
            if len(word)<=2:
                if self.word_pool[word]==self.res[word]:
                    return True
                else:
                    return False
            else:
                key = word[0]+str(len(word)-2)+word[-1]
                if self.word_pool[word]==self.res[key]:
                    return True
                else:
                    return False
        else:
            if len(word)<=2:
                return True
            else:
                key = word[0]+str(len(word)-2)+word[-1]
                if key in self.res:
                    return False
                else:
                    return True
                        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)