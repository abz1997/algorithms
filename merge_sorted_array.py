class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m,m+n):
            print(i)
            nums1[i]=nums2[i-m]
        nums1.sort()
        print(nums1)

sol = Solution()
sol.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
