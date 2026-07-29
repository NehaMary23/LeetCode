class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=set(nums1) if len(nums1)>len(nums2) else set(nums2)
        nums=set()
        for i in (nums2 if len(nums1)>len(nums2) else nums1):
            if i in num:
                nums.add(i)
        return list(nums)
        