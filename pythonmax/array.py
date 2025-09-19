arr = [1,2,3]
arr.pop()
arr.append(4)

arr.insert(1, 99)
print(arr) # [1, 99, 2, 4]
#insert is O(n) time

arr[0] = 99 # this is O(1)

print(arr[::-1]) #invertido

print(arr[1:4])

print("----- iterando sobre 2 arrays con zip")
nums1 = [1,3,5,7]
nums2 = [2,4,6]
for n1, n2 in zip(nums1, nums2):
    print(n1,n2)
"""
1 2
3 4
5 6
"""