class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans=0
        k=0
        t=n
        if n==0:
            return 1
        while(n>0):
            n=n>>1
            k+=1
        n=t

        for i in range(k):
            if (n>>i)&1==0:
                ans+=(1<<i)
        return ans