# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        if not l:
            return None
        l.sort()
        head=ListNode(l[0])
        curr=head
        for i in range(1,len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        curr.next=None
        return head
        