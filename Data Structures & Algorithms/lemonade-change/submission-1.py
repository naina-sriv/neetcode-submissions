class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5=0
        bill10=0
        for i in bills:
            if i==5:
                bill5+=1
            elif i==10:
                bill10+=1
                if bill5>0:
                    bill5-=1
                else:
                    return False
            elif i==20:
                if (bill5>0 and bill10>0):
                    bill5-=1
                    bill10-=1
                elif (bill5>2):
                    bill5-=3
                else:
                    return False
        return True
                
