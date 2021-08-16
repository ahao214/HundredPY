# 队列
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, ele):
        if not self.isFilled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = ele
        else:
            raise IndexError("Queue is full")

    def pop(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return self.rear == self.front

    def isFilled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(4):
    q.push(i)

print(q.pop())
