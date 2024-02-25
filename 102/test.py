from collections import deque 
	
# Declaring deque 
queue = deque(['name','age','DOB']) 
	
print(queue)
queue.append('xxxx')
print(queue)
queue.appendleft('yyyy')
print(queue)
queue.append(['zzzz'])
print(queue)
for i in range(len(queue)):
    print(queue.popleft())
print(queue)
