# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        small=[]
        large=[]        
        while curr:
            if curr.val<x:
                small.append(curr.val)      # 1 3                
            elif curr.val>x:
                large.append(curr.val)      # 4 3 5                
            else:
                large.append(x)
            curr=curr.next

        small.extend(large)
        
        head=ListNode(small[0])
        curr=head
        for i in range(1,len(small)):
            curr.next=ListNode(small[i])
            curr=curr.next
        return head
        