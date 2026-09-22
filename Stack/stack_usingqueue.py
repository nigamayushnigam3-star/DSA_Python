#  see the ss 
from collections import deque 
class StackUsingQueue:
    def __init__(self):
        self.queue = deque() 

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft()) 

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft() 

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return print(self.queue[0])  

    def is_empty(self):
        return len(self.queue) == 0 

    def size(self):
        return len(self.queue) 

SQ = StackUsingQueue() 
SQ.push(5)
SQ.push(10)
SQ.push(15)
SQ.push(20)  
SQ.peek() 
SQ.pop() 
SQ.peek()
SQ.pop() 
SQ.peek()
SQ.pop()
SQ.peek()
print(SQ.is_empty())  
SQ.peek()
SQ.pop()
print(SQ.is_empty())           
    