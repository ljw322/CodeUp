from collections import deque
queue = deque()

queue.append(1)
queue.append(3)
queue.append(7)
queue.append(9)
print(queue)
print(list(queue))

queue.popleft()
print(list(queue))
queue.reverse()
print(list(queue))