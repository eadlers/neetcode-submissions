class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #hashmap solution
        #iterate over s and then over t
        #use each char as key, count as value
        #s increases count, t decreases
        #each key must have 0 as value after all chars are iterated
        anagramDict = {}
        for x in s:
            anagramDict[x] = anagramDict.get(x, 0) + 1
        for y in t:
            anagramDict[y] = anagramDict.get(y, 0) - 1
        for count in anagramDict.values():
            if count != 0:
                return False
        return True
        