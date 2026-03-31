# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverseList(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        curr = start.next
        first = curr
        prev = start

        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first.next = end.next
        end.next = prev
        start.next = end

        return first

        
        


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode()
        start = ListNode()
        curr = head

        start.next = curr
        isFirst = True

        while curr:
            count = k

            while count and curr:
                count -= 1
                if count:
                    curr = curr.next
            if isFirst:
                isFirst = False
                dummy.next = curr
            end = curr
            curr = curr.next if curr else None
            
            if not count:
                start = self._reverseList(start, end)
        
        return dummy.next


        