""""

""""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if i != j:
                    return sorted([i, j])
            else:
                continue
        return l

""""
other answer
""""

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}

    for i in range(len(nums)):
      x = nums[i]
      needed = target - x
      if needed in d:
        return [d[needed],i]
      d[x] = i

      
      
