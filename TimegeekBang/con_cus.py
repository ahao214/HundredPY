from threading import Thread, current_thread
import time
import random
from queue import Queue

queue = Queue(5)


class ProduceThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者%s生产了数据%s' % (name, num))
            t = random.randint(1, 3)


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者%s消耗了数据%s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)


p1 = ProduceThread(name='p1')
p1.start()
c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()
