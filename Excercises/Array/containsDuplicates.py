#Determine if array contains any duplicate value


class Solution(object):
    def containsDuplicate(self, nums):
        app = set()
        for i in range(len(nums)):
            if nums[i] in app:
                return True
            app.add(nums[i])
        return False