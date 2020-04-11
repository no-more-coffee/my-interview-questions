from collections import deque


class MinStack:
    def __init__(self):
        self.stack = deque(())
        self.mins = deque(())

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self) -> None:
        item = self.stack.pop()
        if self.mins and self.mins[-1] == item:
            self.mins.pop()
        return item

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None


minStack1 = MinStack()
minStack1.push(-2)
minStack1.push(0)
minStack1.push(-3)
print(minStack1.getMin())
minStack1.pop()
print(minStack1.top())
print(minStack1.getMin())

print()

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.getMin())
