# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x = y = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                x.next = list1
                list1, x = list1.next, list1
            else:
                x.next = list2
                list2, x = list2.next, list2
        if list1:
            x.next = list1
        else :
            x.next = list2
        return y.next
