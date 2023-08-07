'''15. 3Sum
Medium
27.4K
2.5K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.'''

class Solution:
    def threeSum(self, nums):
        first = 0
        second = 1
        third = 2
        list1 = []

        while first < len(nums) and third < len(nums):
            integer1 = nums[first]
            integer2 = nums[second]
            integer3 = nums[third]
            # print(integer1,integer2,integer3)
            # print(integer1+integer2+integer3)
            if integer1 + integer2 + integer3 == 0:
                list1.append([integer1, integer2, integer3])
            third += 1
            if third >= len(nums):
                second += 1
                third = second + 1
            if second >= len(nums) - 2:
                first += 1
                second = first + 1
                third = second + 1
        
        # if not list1[0]:
        #     return []

       

        for i in list1:
            i.sort()
            if list1.count(i) > 1:
                list1.remove(i)
        print(list1)
        return list1

sol = Solution()
sol.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49])