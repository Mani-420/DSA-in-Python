class Queue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, x):
        self.values.append(x)
        
    def dequeue(self):
        front = self.values[0]
        # self.values.pop(front)
        self.values = self.values[1:]
        return front

# Test the working:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue after Enqueue: {q.values}")
first = q.dequeue()
second = q.dequeue()
third = q.dequeue()
print(f"Queue after Dequeue: {q.values}")
print (f"Third value of queue is: {third}")
