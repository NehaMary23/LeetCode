# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        dup=[]
        while curr!=None:
            if curr.val in dup:
                curr=curr.next
                prev.next=curr
                continue

            else:
                dup.append(curr.val)
            prev=curr
            curr=curr.next
        return head