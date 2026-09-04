class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        for x in nums:
            countDict[x] += 1
        countArr = []
        for num, count in countDict.items():
            countArr.append((count, num))
        countArr.sort(reverse=True)
        result = []
        for i in range(k):
            result.append(countArr[i][1])
        return result
        

        