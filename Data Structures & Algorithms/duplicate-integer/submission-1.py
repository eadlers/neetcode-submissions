class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenQuestions = set()
        for x in nums:
            if x in seenQuestions:
                return True
            else:
                seenQuestions.add(x)
        return False
                
        
        