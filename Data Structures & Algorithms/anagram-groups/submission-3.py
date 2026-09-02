class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #26 char combination is key, index is value
        countMap = defaultdict(list)
        for x in strs:
            charCounter = [0] * 26
            for char in x:
                #calculate the alphabet order (0-25)
                order = ord(char) - ord('a')
                charCounter[order] += 1
            countMap[tuple(charCounter)].append(x)
        return list(countMap.values())
        
            
                




        