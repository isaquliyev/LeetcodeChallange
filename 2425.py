class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        l_nums1 = len(nums1)
        l_nums2 = len(nums2)

        if l_nums1 % 2 == 0 and l_nums2 % 2 == 0:
            return ans
        elif l_nums1 % 2 == 1 and l_nums2 % 2 == 0:
            it = nums2
        elif l_nums1 % 2 == 0 and l_nums2 % 2 == 1:
            it = nums1
        else:
            it = nums1 + nums2
        for num in it:
            ans ^= num
    
        return ans
