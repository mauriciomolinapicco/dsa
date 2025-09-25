class MinStack(object):
    def __init__(self):
        self.stack = []
        self.ms = []

    def push(self, val):
        if (self.ms == [] or val <= self.ms[-1]): self.ms.append(val)
        
        self.stack.append(val)

    def pop(self):
        if self.stack[-1] == self.ms[-1]:
            self.ms.pop()
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.ms[-1]
