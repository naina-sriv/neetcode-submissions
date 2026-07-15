"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otp={None:None}
        temp=head
        while temp!=None:
            otp[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp!=None:
            copy=otp[temp]
            copy.next=otp[temp.next]
            copy.random=otp[temp.random]
            temp=temp.next
        return otp[head]
            

            
