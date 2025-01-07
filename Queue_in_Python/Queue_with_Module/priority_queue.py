# It works on the Priority

import queue
q = queue.PriorityQueue()

q.put((4, "Zizou"))
q.put((2, "LM10"))
q.put((3, "Neymar"))
q.put((1, "CR7"))
    
# get() is used to get numbers from the queue
# while not q.empty():
#     print(q.get())

while not q.empty():
    print(q.get()[1])

print(q.queue)

# -------------------------------------------------------------------

# Create a priority queue instance
priority_queue = queue.PriorityQueue()

# Ask the user how many tasks they want to add
num_tasks = int(input("Enter the number of tasks to add to the priority queue: "))

# Get tasks and their priorities from the user
for _ in range(num_tasks):
    task = input("Enter the task: ")
    priority = int(input(f"Enter the priority for '{task}' : "))
    priority_queue.put((priority, task))

# Display tasks based on priority
print("\nTasks in the priority queue based on priority:")
while not priority_queue.empty():
    priority, task = priority_queue.get()
    print(f"Priority: {priority}, Task: {task}")
