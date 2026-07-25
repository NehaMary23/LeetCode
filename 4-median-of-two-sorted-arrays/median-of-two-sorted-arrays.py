class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        i=len(num)//2
        if len(num)%2==0:
            return float((num[i]+num[i-1])/2)
        else:
            return float(num[i])