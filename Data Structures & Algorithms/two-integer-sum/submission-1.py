class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums[j] = target - nums[i]
        #numsMap key is the number, value is the index in the nums array
        numsMap = {}
        for i in range(len(nums)):
            currentNum = nums[i]
            difference = target - currentNum
            if difference in numsMap:
                return [numsMap[difference], i]
            else:
                numsMap[currentNum] = i
        return []



        