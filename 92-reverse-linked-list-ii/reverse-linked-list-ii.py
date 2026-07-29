# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next==None:
            return head
        curr=head
        prev=None
        if left==1:
            for i in range(right):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            head.next=curr
            return prev
        for i in range(left-1):
            prev=curr
            curr=curr.next
        before=prev
        last=curr
        prev=None
        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        before.next=prev
        last.next=curr
        while curr:
            curr=curr.next
        return head