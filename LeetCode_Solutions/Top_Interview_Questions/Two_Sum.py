# QUestion Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        # init dict to store val,idx pairs
        check_dict = dict()
        
        for i,n in enumerate(nums):
            check_dict[n] = i
        
        # iterate through the nums list and check for the difference in check_dict
        for i,n in enumerate(nums):
            diff = target - n
            # make sure to not return the same index
            if diff in check_dict and i != check_dict[diff]:
                return [i, check_dict[diff]]