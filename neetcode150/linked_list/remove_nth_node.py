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
