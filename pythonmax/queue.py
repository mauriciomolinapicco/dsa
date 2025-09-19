from collections import deque

queue = deque()

queue.append(4)
queue.append(7)

queue.appendleft(0)
queue.popleft()

print(queue)

