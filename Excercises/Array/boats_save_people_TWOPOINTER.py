"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

"""
# Lo ideal es juntar los de afuera, los mas pesados con los mas livianos e ir entrando hacia el medio
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r: #make sure they dont cross eachother
            remaining = limit - people[r]
            if remaining >= people[l]:
                l += 1
            r -= 1
            boats += 1
        return boats