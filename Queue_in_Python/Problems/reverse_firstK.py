from queue import Queue

def reverse_k_elements(queue, k):
    if queue.qsize() < k or k <= 0:
        return queue

    stack = []

    # Step 1: Dequeue the first K elements and push them onto the stack
    for _ in range(k):
        stack.append(queue.get())

    # Step 2: Enqueue the stack elements back into the queue (reversed order)
    while stack:
        queue.put(stack.pop())

    # Step 3: Move the remaining elements to the back of the queue to retain order
    size = queue.qsize()
    for _ in range(size - k):
        queue.put(queue.get())

    return queue

# Example usage
if __name__ == "__main__":
    q = Queue()
    elements = [1, 2, 3, 4, 5]
    for element in elements:
        q.put(element)

    k = 3
    print("Original Queue:", list(q.queue))
    reversed_queue = reverse_k_elements(q, k)
    print("Queue after reversing first K elements:", list(reversed_queue.queue))
