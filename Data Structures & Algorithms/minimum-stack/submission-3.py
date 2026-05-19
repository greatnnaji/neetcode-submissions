class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack and val <= self.min_stack[0]:
           self.min_stack.insert(0, val)
        else:
            self.min_stack.append(val)

        self.stack.append(val)


    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[0]:
            self.min_stack.remove(top)


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[0]
        
