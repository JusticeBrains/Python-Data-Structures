from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f'{self.items}'
    
    def __repr__(self):
        return f'{self.items}'


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push('Using')
    s.push('Collections')
    s.push('deque')
    s.push('method')
    s.push('to')
    s.push('create')
    s.push('stack')
    print(s.is_empty())
    print(s)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s)
    print(s.size())
    