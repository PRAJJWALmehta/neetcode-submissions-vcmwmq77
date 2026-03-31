# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr2.val < ptr1.val:
                node.next = ptr2
                ptr2 = ptr2.next
            else:
                node.next = ptr1
                ptr1 = ptr1.next
            node = node.next
        
        node.next = ptr1 or ptr2

        return head.next
