# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr!=None:
            if curr.val==val and curr==head:
                head=curr.next
                
            elif curr.val==val:
                curr=curr.next
                prev.next=curr
                continue
                
            prev=curr
            curr=curr.next
        return head