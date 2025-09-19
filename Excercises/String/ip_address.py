class Solution(object):
    def defangIPaddr(self, address):
        s = ''
        for i in range(len(address)):
            if address[i] == '.':
                s += '[.]'
            else:
                s += address[i]
        return s