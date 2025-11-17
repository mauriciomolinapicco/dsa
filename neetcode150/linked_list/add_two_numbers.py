# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode(None, None)
        res = p
        lleva = False
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if lleva:
                v = (v1 + v2 + 1)
            else:
                v = (v1 + v2)
            lleva = True if v >= 10 else False
            v %= 10

            p.next = ListNode(v, None)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if lleva:
            p.next = ListNode(1,None)
            
        return res.next