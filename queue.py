from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self,item):
        """
        Add an item to the end of the queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and print the first item
        """
        return self.items.popleft()
    
    def peek(self):
        """
        returns the first item in the queue
        """
        return self.items[0]
    
    def size(self):
        """
        returns the length of the queue
        """
        return len(self.items)
    
    def __str__(self):
        return f"{self.items}"
    
    def __repr__(self):
        return f"{self.items}"

if __name__ == '__main__':
    q = Queue()
    print(q)
    print(f"Is the Queue Empty: {q.is_empty()}")
    q.enqueue("Learning")
    q.enqueue("Queue")
    q.enqueue("Data")
    q.enqueue("Structures")
    print(q)
    print(f"Is the Queue Empty: {q.is_empty()}")
    print(f"Size of the Queue is: {q.size()}")
    print(f"First element in the Queue is: {q.peek()}")
    print(f"Removing first element: {q.dequeue()}")
    print(q)
    print(f"Size of the Queue is: {q.size()}")
    