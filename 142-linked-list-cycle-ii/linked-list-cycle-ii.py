# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        v=set()
        while curr:
            if curr in v:
                return curr
            v.add(curr)
            curr=curr.next
        return None
