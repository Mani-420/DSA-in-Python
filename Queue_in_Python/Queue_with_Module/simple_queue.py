# It works on the FIFO principle

import queue
q = queue.Queue()

# A Simple list 
numbers = [10, 20, 30, 40, 50, 60, 70]

# Add whole list to queue
for number in numbers:
    q.put(number)           # put() is used to enter list into queue
    
# get() is used to get numbers from the queue
value = q.get()
print(f"The first number from the list is: {value}")
print (q.queue)
