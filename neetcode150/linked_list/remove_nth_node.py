from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        h = head
        nodes = 0
        while h:
            h = h.next
            nodes += 1
        c = 0

        corte = nodes-n-1
        if corte < 0:
            head = head.next
            f = head
            
        while head:
            if c == corte:
                if head.next:
                    head.next = head.next.next
                
            head = head.next
            c += 1

        return f


# version con una pasada usando dos punteros
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        h1, h2 = head, None
        c = 0

        while True:
            h1 = h1.next
            if c >= n:
                if not h2:
                    h2 = head
                else:
                    h2 = h2.next
            if not h1:
                if not h2:
                    return head.next
                if h2.next:
                    h2.next = h2.next.next
                break
            c += 1

        return r
