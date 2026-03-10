class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnta=0
        cntb=0
        candidatea=0
        candidateb=0
        n=len(nums)
        for i in range(n):
            if cnta==0 and nums[i]!=candidateb:
                candidatea=nums[i]
                cnta=1
                # print(candidatea,candidateb)
            elif cntb==0 and nums[i]!=candidatea:
                candidateb=nums[i]
                cntb=1
            elif nums[i]==candidatea:
                cnta+=1
            elif nums[i]==candidateb:
                cntb+=1
            else:
                cnta-=1
                cntb-=1
        cnta=0
        cntb=0
        third=n//3
        for i in range(n):
            if nums[i]==candidatea:
                cnta+=1
            elif nums[i]==candidateb:
                cntb+=1
        res=[]
        if cnta>third:
            res.append(candidatea)
        if cntb>third:
            res.append(candidateb)
        return res