# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        tail = ret
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next

        if not curr1 and curr2:
            tail.next = curr2
        elif not curr2 and curr1:
            tail.next = curr1

        return ret.next
                

            