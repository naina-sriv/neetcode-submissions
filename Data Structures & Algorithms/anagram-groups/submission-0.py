class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=dict()
        for i in strs:
            sorted_str="".join(sorted(i))
            if sorted_str in groups:
                groups[sorted_str].append(i)
            else:
                groups[sorted_str]=[i]
        ans=[]
        for i in groups:
            ans.append(groups[i])
        return ans


            