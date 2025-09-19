# devolver la cantidad de pares que suman k

#brute force
class Solution(object):
    def countKDifference(self, nums, k):
        n = len(nums)
        con = 0
        for i in range(n-1):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) == k:
                    con += 1
        return con
    

#better approach using list
class Solution(object):
    def countKDifference(self, nums, k):
        l = []
        con = 0
        for i in range(len(nums)):
            con += l.count(nums[i])
            l.append(nums[i]-k)
            l.append(nums[i]+k)
        return con
    


#using hashmap
class Solution(object):
    def countKDifference(self, nums, k):
        cont = {}
        res = 0
        for num in nums:
            res += cont.get(num+k, 0)
            res += cont.get(num-k, 0)

            a = cont.get(num, 0)
            cont[num] = a+1
                
        return res