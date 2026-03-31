# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def _mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        while l1 and l2:
            if l2.val < l1.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            
            prev = prev.next
        
        if l1:
            prev.next = l1
        
        if l2:
            prev.next = l2
        
        return dummy.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None

        for ll in lists:
            res = self._mergeLists(res, ll)
        
        return res

        