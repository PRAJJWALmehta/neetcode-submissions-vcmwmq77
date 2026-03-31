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
        curr = head
        dummy = Node(0)
        seek = dummy
        nodeMap = {}

        while curr:
            seek.next = Node(curr.val)
            seek = seek.next
            nodeMap[curr] = seek
            
            curr = curr.next
        
        curr = head
        seek = dummy.next
        while curr:
            seek.random = nodeMap[curr.random] if curr.random else None
            curr = curr.next
            seek = seek.next
        
        return dummy.next




        