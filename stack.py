

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """
        Returns a boolean value if the stack is empty
        """
        return not self.items
    
    def push(self,item):
        """
        Adds an item to the end of stack
        """
        self.items.append(item)
    
    def pop(self):
        """"
        Removes and returns the top item from the stack
        """
        return self.items.pop()
    
    def peek(self):
        """
        Returns the last item from the stack
        """
        return self.items[-1]
    
    def size(self):
        """
        Returns the length of the stack
        """
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return self.items
    

if __name__ == '__main__':
    # creating an instance of the class
    stack = Stack()
    print(f"Is the stack empty: {stack.is_empty()}")
    print(stack.push(3))
    print(stack.push(5))
    print(f"Is the satck empty: {stack.is_empty()}")
    print(f"Items in the stack: {stack}")
    print(f"The size of the stack is: {stack.size()}")
    print(f"The last added item in the stack is: {stack.peek()}")
    print(f"Removes and returns the last item in the stack: {stack.pop()}")
    print(f"Items in the stack: {stack}")
    stack
    