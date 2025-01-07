class Queue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, x):
        self.values.append(x)
        
    def dequeue(self):
        front = self.values[0]
        self.values = self.values[1:]
        return front
    
    def peek(self):
        if self.is_empty():
            print("Peek operation failed: Queue is empty.")
            return -1
        else:
            return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

# Test the working:
q = Queue()

q.enqueue(1)
q.enqueue(2)
print(f"Queue after Enqueue: {q.values}")

front_num = q.peek()
print(f"The fisrt element is : {front_num}")

first = q.dequeue()
second = q.dequeue()
print(f"Queue after Dequeue: {q.values}")
