class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        curr=0
        for i in nums:
            curr+=i
            if curr<i:
                curr=i
            maxi=max(curr,maxi)
        return maxi
            
        