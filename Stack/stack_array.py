class Stack:
    def __init__(self):
        self.items = []  

    def is_empty(self): # 0(1)
        return len(self.items) == 0   

    def push(self,item):  # 0(1)
        self.items.append(item) 

    def pop(self):  # 0(1)
        if len(self.items) == 0 :
            return "Cannot pop , stack is empty"
        x = self.items.pop()
        return x 

    def top(self):  # 0(1)
        if len(self.items) == 0:
            return "Caanot top , Stack is empty "     
        return self.items[-1]     

    def size(self):         # 0(1)
        return len(self.items)


stack = Stack() 
stack.push(5) 
stack.push(10) 
stack.push(15)  
stack.push(25) 
print(f"Stack Content = {stack}")    
print(f"popped item = {stack.pop()}")
print(f"Stack Content = {stack}") 
# print(f"Top item after pop = {stack.peek()}") 
print(f"Stack is empty = {stack.is_empty()}") 
