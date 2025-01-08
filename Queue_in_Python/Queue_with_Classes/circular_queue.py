class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.head = 0               # From where data will be removed
        self.tail = 0               # From where data will be added
        self.capacity = 0            # Number of elements in queue
    
    def enQueue(self, data):
        if self.isFull():
            raise Exception("Queue is Full.")
        self.queue[self.tail] = data
        self.tail = (self.tail+1) % self.size 
        self.capacity += 1
        
    def deQueue(self):
        if self.capacity == 0:
            return None
        data = self.queue[self.head]
        self.queue[self.head] = 0
        self.head = (self.head+1) % self.size
        self.capacity -= 1
        return data
    
    def isFull(self):
        return self.size == self.capacity
    
    
def main():
    size = int(input("Enter the size of array: "))
    q = Queue(size)

    q.enQueue(1)
    q.enQueue(2)
    q.deQueue()
    q.enQueue(3)
    q.enQueue(4)
    q.deQueue()
    q.enQueue(5)
    q.enQueue(6)

    print(f"Queue after multiple enQueue & deQueue: {q.queue}")

if __name__ == "__main__":
    main()