class MinStack:

    def __init__(self):
        self.m = []
        self.s = []

    def push(self, val: int) -> None:
        if not self.m:
            self.m.append(val)
        else:
            smallest = min(self.m[-1], val)
            self.m.append(smallest)
            
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
