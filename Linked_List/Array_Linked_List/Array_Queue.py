from queue import Empty
class ArrayQueue:
    def __init__(self):
        self._array = []
    def __len__(self):
        return len(self._array)
    def is_Empty(self):
        return len(self._array) == 0
    def clear(self):
        self._array = []
    def enqueue(self,data):
        self._array.append(data)
    def dequeue(self):
        if self.is_Empty():
            raise Empty("Queue is empty")
        else:
            print(self._array[0])
            self._array.remove(self._array[0])
    def first(self):
        if self.is_Empty():
            raise Empty("Queue is empty")
        else: print(self._array[0])
    def traverse(self):
        print(*[ele for ele in self._array])
    def insertMul(self,array):
        [self._array.append(ele) for ele in array]
    def convert_to_bin(self,decimal):
        while decimal != 0:
            remainder = decimal % 2
            decimal = decimal // 2
            self._array.append(remainder)
        self._array = self._array[::-1]
        return self._array
    def convert_float_to_bin(self,number:float,num_digits):
        integral = int(number // 1)
        fraction = number % 1
        Queue = ArrayQueue()
        Queue.convert_to_bin(integral)
        Queue.enqueue(".")
        for i in range(num_digits):
            Queue.enqueue(int((fraction*2)//1))
            fraction = (fraction * 2) % 1
        Queue.traverse()
    def convert_negative_to_bin(self,number,bin_digits):
        number *= -1
        Queue = ArrayQueue()
        Queue.convert_to_bin(number)
        for ele in Queue._array[:len(Queue)-1]:
            if ele == 1:
                Queue.dequeue()
                Queue.enqueue(0)
            else:
                Queue.dequeue()
                Queue.enqueue(1)
        Queue.dequeue()
        Queue.enqueue(1)
        return Queue.traverse()
if __name__ == '__main__':
    Queue = ArrayQueue()
    Queue.enqueue(7)
    Queue.enqueue(12)
    Queue.enqueue("hello")
    Queue.enqueue("o")
    Queue.traverse()
    Queue.dequeue()
    Queue.traverse()
    Queue.insertMul([2,7,8,1,9])
    Queue.traverse()
    Queue.clear()
    Queue.convert_to_bin(32)
    Queue.traverse()
    Queue.clear()
    Queue.convert_float_to_bin(12.35124,5)
    Queue.clear()
    Queue.convert_negative_to_bin(-32,5)
