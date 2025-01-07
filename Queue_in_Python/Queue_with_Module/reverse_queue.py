# It works on the LIFO principle

import queue
q = queue.LifoQueue()

# A Simple list 
numbers = [10, 20, 30, 40, 50, 60, 70]

# Add whole list to queue
for number in numbers:
    q.put(number)           # put() is used to enter list into queue
    
# get() is used to get numbers from the queue
value = q.get()
print(f"The last number from the list is: {value}")
print (q.queue)
