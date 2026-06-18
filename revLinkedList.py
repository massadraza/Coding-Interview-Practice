# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None

        if head is None:
            return None

        while p != None:
            q = p.next
            p.next = prev
            prev = p
            p = q

        return prev
        

     

        