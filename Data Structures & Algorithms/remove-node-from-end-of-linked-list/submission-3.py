class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        if head.next==None:
            return None
        slow=head
        fast=head
        while fast.next!=None:
            fast=fast.next
            if count<n:
                count+=1
            elif count==n:
                slow=slow.next
        if count < n:
            return head.next
        slow.next=slow.next.next
        return head