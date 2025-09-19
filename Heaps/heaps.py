import heapq
"""
orders elements by priority. Tree DS. Can be max or min heap

- O(1) to read the top (or bottom in min heap) element
- O(log n) to insert a new element at the top
- O(n) to create from scratch
- O(>n) to insert an element in the middle. NOT MADE FOR THIS

""" 

data = [20,43,44,23,1,5,77,1,2,2,6,38,54]

heapq.heapify(data)

print(data)