# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode()
        curr.next = head
        fast = curr
        res = curr

        while fast.next:
            if not n:
                curr = curr.next
            else:
                n -= 1
            fast = fast.next

        if curr.next:
            curr.next = curr.next.next
        else:
            res = None

        return res.next
        