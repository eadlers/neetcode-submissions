class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        countMap = defaultdict(list)
        for x in strs:
            charCounter = [0] * 26
            for char in x:
                order = ord(char) - ord('a')
                charCounter[order] += 1
            countMap[tuple(charCounter)].append(x)
        return list(countMap.values())