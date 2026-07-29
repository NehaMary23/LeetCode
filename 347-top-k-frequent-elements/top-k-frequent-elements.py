class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=set(nums)
        dnum={}
        for i in num:            
            dnum[i]=nums.count(i)
        d=dict(sorted(dnum.items(), key=lambda x:x[1], reverse=True))
        l=list(d.keys())
        freq=[]
        for i in range(k):
            freq.append(l[i])
        return freq
        