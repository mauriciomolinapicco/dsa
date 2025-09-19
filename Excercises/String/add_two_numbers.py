'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        node = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #nuevo digito
            valor = v1 + v2 + carry

            if valor > 9:  #Todo esto es lo mismo que hacer carry = valor // 10
                carry = 1
            else:
                carry = 0
                
            valor %= 10 
            node.next = ListNode(valor)
            node = node.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next