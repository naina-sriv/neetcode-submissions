class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh=dict()
        th=dict()
        for i in s:
            if i in sh:
                sh[i]+=1
            else:
                sh[i]=1
        for i in t:
            if i in th:
                th[i]+=1
            else:
                th[i]=1
        for i in sh:
            if i in th and th[i]==sh[i]:
                continue
            else:
                return False
        for i in th:
            if i in sh and sh[i]==th[i]:
                continue
            else:
                return False
        return True

        