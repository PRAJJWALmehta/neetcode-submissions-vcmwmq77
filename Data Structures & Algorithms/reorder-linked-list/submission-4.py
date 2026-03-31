# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = curr = head
        prev = None

        while tmp:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        revHead = self._reverseList(slow.next)
        slow.next = None

        a, b = head, revHead

        while a and b:
            temp = a.next
            a.next = b
            a = temp
            temp = b.next
            if a:
                b.next = a
            b = temp
        

        