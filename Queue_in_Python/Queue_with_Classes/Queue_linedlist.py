class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to the first element (head of the queue)
        self.rear = None   # Points to the last element (tail of the queue)
        self.size = 0      # Tracks the number of elements in the queue
    
    def enQueue(self, data):            # Adds an element to the end of the queue.
        new_node = Node(data)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued: {data}")
    
    def deQueue(self):                  # Removes and returns the front element of the queue.
        if self.front is None:          # Queue is empty
            print("Queue is empty!")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:          # Queue becomes empty
            self.rear = None
        self.size -= 1
        print(f"Dequeued: {data}")
        return data
    
    def isEmpty(self):                  # Checks if the queue is empty.
        return self.front is None
    
    def peek(self):                     # Returns the front element without removing it.
        if self.front is None:
            print("Queue is empty!")
            return None
        return self.front.data

    def getSize(self):                  # Returns the number of elements in the queue.
        return self.size
    
    def display(self):                  # Displays the entire queue.
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Main function to test the Queue
def main():
    q = Queue()

    # Enqueue elements
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    print(f"Front element: {q.peek()}")
    print(f"Queue size: {q.getSize()}")

    # Displaying Queue Elements
    print(f"The elements of the queue are: {q.display()}")

    # Dequeue elements
    q.deQueue()
    q.deQueue()
    print(f"Front element after dequeuing: {q.peek()}")
    print(f"Queue size after dequeuing: {q.getSize()}")

    # Attempt to dequeue from an empty queue
    q.deQueue()
    q.deQueue()  # This will indicate the queue is empty

if __name__ == "__main__":
    main()
