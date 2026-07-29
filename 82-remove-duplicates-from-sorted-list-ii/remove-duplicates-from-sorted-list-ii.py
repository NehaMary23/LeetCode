# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        l=[]
        val=None
        while curr and curr.next:
            if curr.next.val!=curr.val and curr.val != val:
                l.append(curr.val)
                curr=curr.next
                continue
            val=curr.val
            curr=curr.next
        if curr.val != val:
            l.append(curr.val)
        if not l:
            return None
        head=ListNode(l[0])
        curr=head
        for i in range(1,len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return head