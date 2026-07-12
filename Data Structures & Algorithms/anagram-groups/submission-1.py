class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=dict()
        for i in strs:
            punch_card=[0 for j in range(0,26)]
            for letter in i:
                index= 122 - ord(letter)
                if punch_card[index]!=0:
                    punch_card[index]+=1
                else:
                    punch_card[index]=1
            tup=tuple(punch_card)
            if tup in groups:
                groups[tup].append(i)
            else:
                groups[tup]=[i]
        return [groups[i] for i in groups]