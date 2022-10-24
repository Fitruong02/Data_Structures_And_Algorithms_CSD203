from queue import Empty
class ArrayStack:
    def __init__(self):
        self._array = []
    def __len__(self):
        return len(self._array)
    def is_Empty(self):
        return len(self._array) == 0
    def clear(self):
        self._array = []
    def push(self,data):
        self._array.append(data)
    def pop(self):
        if self.is_Empty():
            raise Empty("Stack is empty")
        else: print(self._array.pop())
    def top(self):
        if self.is_Empty():
            raise Empty("Stack is empty")
        else: print(self._array[-1])
    def traverse(self):
        print(*[ele for ele in self._array[::-1]])
    def convert_to_Bin(self,decimal):
        while decimal != 0:
            remainder = decimal % 2
            decimal = decimal //2
            self._array.append(remainder)
        return self.traverse()
if __name__ == '__main__':
    stack = ArrayStack()
    anotherStack = ArrayStack()
    anotherStack.push(23)
    stack.push(anotherStack)
    stack.push("xinchào")
    stack.push("h")
    stack.traverse()
    stack.pop()
    stack.clear()
    stack.convert_to_Bin(12)
