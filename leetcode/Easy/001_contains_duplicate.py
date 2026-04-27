""""
problem: Contains Duplicate
Difficulty: Easy
Topic: Array, Hash table
""""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reps = 0 
        for i in nums:
            if nums.count(i) > 1:
                reps += 1
            else: continue
        if reps > 0 :
            return True
        else:
            return False
