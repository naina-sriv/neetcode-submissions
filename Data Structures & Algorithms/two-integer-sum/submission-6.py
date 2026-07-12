class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi=dict()
        for i in range(len(nums)):
            hashi[nums[i]]=i
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hashi and i!=hashi[comp]:
                return sorted([i,hashi[comp]])
