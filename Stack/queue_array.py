class Queue:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return len(self.items) == 0 

    def enqueue(self,item):
        self.items.append(item) 

    def dequeue(self):
        if len(self.items) == 0:
            print("dequeue from empty queue") 
            return 
        x = self.items.pop(0) 
        return x  

    def front(self): # pointing the starting value  
        if len(self.items) == 0:
            print("Cannot peek , queue is empty ") 
            return 
        return print(f"first number be {self.items[0]}") 

    def rear(self):
        if len(self.items) == 0:
            print("Cannot read , queue is empty ") 
        return print(f"Last number be {self.items[-1]}")  

    def size(self):
        return len(self.items) 

queue = Queue()
queue.enqueue(5) 
queue.enqueue(10) 
queue.enqueue(15) 
queue.enqueue(20)
queue.front()
queue.rear() 
print(queue.is_empty()) 