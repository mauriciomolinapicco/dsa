'''
Given a string n that represents a positive decimal integer, return the minimum 
number of positive deci-binary numbers needed so that they sum up to n.
'''
#la solucion es basicamente encontrar el digito mas alto
class Solution(object):
    def minPartitions(self, n):
        #mejor opcion
        for i in range(9,0,-1):
            if str(i) in n:
                return int(i)
        
        '''Opcion 2
            return int(max(n))
        '''
