class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        l=0
        for i in s:
            if i-1 in s:
                continue
            else:
                curr=0
                while i in s:
                    i+=1
                    curr+=1
                l=max(l,curr)
        return l


            