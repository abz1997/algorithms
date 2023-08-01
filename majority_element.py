class Solution(object):
    def majorityElement(self, nums):
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            if i == sol:
                cnt += 1
            else:
                cnt -= 1
            print(cnt)
        print(sol)
        return sol

sol =Solution()
sol.majorityElement([3,4,4,4,2])