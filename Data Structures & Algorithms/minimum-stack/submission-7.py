class MinStack:

    def __init__(self):
        self.s = []
        self.m = [] # track at each level min

    def push(self, val: int) -> None:
        if not self.m:
            self.m.append(val)
        else:
            last = self.m[-1]
            if last < val:
                self.m.append(last)
            else:
                self.m.append(val)
        self.s.append(val)

    def pop(self) -> None:
        self.m.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
