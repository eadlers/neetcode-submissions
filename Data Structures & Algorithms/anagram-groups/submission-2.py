class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #26 char combination is key, index is value
        countMap = {}
        for x in strs:
            #26 options here
            charCounter = [0] * 26
            for char in x:
                #calculate the alphabet order (0-25)
                order = ord(char) - ord('a')
                charCounter[order] += 1
            countStr = str(charCounter)
            countMap.setdefault(countStr, []).append(x)
        response = []
        for value in countMap.values():
            response.append(value)
        return response
        
            
                




        