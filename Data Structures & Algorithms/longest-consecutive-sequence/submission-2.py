class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        lcs=0
        for i in nums:
            s.add(i)
        for i in s:
            curr=1
            if i-1 in s:
                continue
            while i+1 in s:
                curr+=1
                i+=1
            lcs=max(curr,lcs)
        return lcs


            