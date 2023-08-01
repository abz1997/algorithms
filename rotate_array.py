''''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     print(nums)
        #     last = nums[-1]
        #     for n in range(len(nums[:-1]), 0, -1):
        #         nums[n] = nums[n-1]
        #     nums[0] = last

        # print(nums)

        temp = []
        k = k % len(nums) # the remainder decides how much we need to shift over the numbers
        print(k)
        temp = nums[-k:] # we set the last numbers to temp variable
        print(temp)
        print(nums[k:])
        print(nums[:-k])
        nums[k:] = nums[:-k] # we swap the end with the beginning
        print(nums)
        nums[:k] = temp # we set the beginning to temp (last numbers) 
        nums[:k]
        print(nums)

sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 30)