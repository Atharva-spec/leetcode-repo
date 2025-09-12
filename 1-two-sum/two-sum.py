'''basic logic of running one nested for loop iin which it checks all the giving elements in the array and check if the sum of the then is 9 or not in this code written as target'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if  nums[i]+nums[j] == target:
                    return [i, j]
