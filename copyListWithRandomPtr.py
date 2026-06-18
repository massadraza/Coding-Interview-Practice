"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        dummy = Node(0)
        ptr = dummy

        # Keep a dictionary for O(1) lookup
        oldToNew = {}

        # Copy all the next's first
        while p:
            newNode = Node(p.val)
            oldToNew[p] = newNode
            ptr.next = newNode
            ptr = ptr.next
            p = p.next
        
        # Next copy all of the randoms now
        # Use a dictionary to keep track
        q = head
        ptr2 = dummy.next

        while q:
            # Get random of q
            newRandom = oldToNew.get(q.random, None)
            ptr2.random = newRandom
            ptr2 = ptr2.next
            q = q.next

        return dummy.next