from collections import deque

class CircularQueue:
    def __init__(self):
        self.items = deque(maxlen=12)

    def is_empty(self):
        """
        Check if the CircularQueue is empty
        """
        return not self.items
    
    def add_first(self,item):
        """
        Add an element to the begin(left) of the array
        """
        if self.items[0] is not None:
            return f"{self.items[0]} Index occupied" 
        self.items.appendleft(item)

    def add_last(self, item):
        """
        Add an element to the end(right) of the circular array
        """
        if self.items[-1] is not None:
            return f"{self.items[-1]} Index occupied"
        self.items.append(item)
    
    def remove_first(self):
        """
        Remove the first element in the circular array
        """
        if self.is_empty():
            return f"Array is empty"
        return self.items.popleft()
    
    def remove_last(self):
        """
        Remove the last element in the circular array
        """

        if self.is_empty():
            return f"Array is empty"
        return self.items.pop()
    
    def first_element(self):
        """
        Return the first element in the circular array
        """
        if self.is_empty():
            return f"Array is empty"
        return self.items[0]
    
    def last_element(self):
        """
        Return the last element in the circular array
        """
        if self.is_empty():
            return f"Array is empty"
        return self.items[-1]

    def size(self):
        """
        Returns the total length of the circular array
        """

        return len(self.items)

    def __repr__(self):
        return self.items
    
    def __str__(self) -> str:
        return f"{self.items}"

if __name__ == '__main__':
    ca = CircularQueue()
    print(ca)
    print(ca.remove_first())
    print(ca.remove_last())
    print(ca.first_element())
    print(ca.last_element())