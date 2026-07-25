class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows=[""]*numRows
        k=numRows-2
        ind=0
        if numRows==1:
            return s
        for i in range(len(s)):         # 0 1 2 3 4 5 6
            if ind==len(s):           # 12
                break
            if i%(numRows-1)!=0:        # 6%2 = 0
                rows[k]+=s[ind]         # 1 ["PAH","APLSII","YIR"]
                ind+=1                  # 12
                k-=1                    # 0
                if k==0:
                    k=numRows-2         # 1
                continue
            
            for j in range(numRows):        # 0
                if ind==len(s):
                    break
                rows[j]+=s[ind]             # ["PAHN","APLSIG","YIR"]
                ind+=1                      # 14
        zz=""
        for i in range(numRows):
            zz+=rows[i]
        return zz