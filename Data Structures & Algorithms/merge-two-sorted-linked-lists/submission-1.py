# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        prev, head = None, None
        ptr1, ptr2 = list1, list2


        while ptr1 and ptr2:
            if ptr2.val < ptr1.val:
                if prev:
                    prev.next = ptr2
                else:
                    head = ptr2
                prev = ptr2
                ptr2 = ptr2.next
            else:
                if prev:
                    prev.next = ptr1
                else:
                    head = ptr1
                prev = ptr1
                ptr1 = ptr1.next
        
        if ptr1 and prev:
            prev.next = ptr1
        
        if ptr2 and prev:
            prev.next = ptr2
        
        return head
        



        