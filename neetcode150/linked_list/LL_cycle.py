# trivial solution using set 0(n) space
 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


#solution using two pointers hare and tortoise o(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head
        f = False
        while hare:
            if f:
                turtle = turtle.next
            hare = hare.next
            if hare == turtle:
                return True
            f = not f
        return False

