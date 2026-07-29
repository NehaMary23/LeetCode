# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        
        L=[]
        while curr:
            l=[]
            for i in range(k):
                l.append(curr.val)
                curr=curr.next
                if not curr:
                    break
            if i==k-1:
                l.reverse()
            L.extend(l)
        head=ListNode(L[0])
        curr=head
        for i in range(1,len(L)):
            curr.next=ListNode(L[i])
            curr=curr.next
        curr.next=None
        return head
        