# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        curr=head
        r=k%length
        for i in range(r):
            prev=None
            while curr.next:
                prev=curr
                curr=curr.next
            curr.next=head
            head=curr
            
            if prev:
                prev.next=None
        return head
