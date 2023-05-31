from queue import PriorityQueue
import random
import threading
import time


COUNT_TASKS = 10


class Task:
    def __init__(self, pr, sleep_time):
        self.priority = pr
        self.sleep_time = sleep_time

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        time.sleep(self.sleep_time)
        return f'Task(priority={self.priority}).      sleep({self.sleep_time})'


class Producer(threading.Thread):
    def __init__(self, q, cnt):
        super().__init__()
        self.queue = q
        self.count = cnt
        print('Producer: Running')

    def run(self):
        for i in range(self.count):
            priority = random.randint(0, 6)
            self.queue.put((priority, Task(priority, random.random())))
        consumer = Consumer(self.queue, self.count)
        consumer.start()
        consumer.join()
        print('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, q, cnt):
        super().__init__()
        self.queue = q
        self.tasks_done = 0
        self.count_tasks = cnt
        print('Consumer: Running')

    def run(self):
        while True:
            if not self.queue.empty():
                priority, task = self.queue.get()
                print(f'>running {task}')
                self.queue.task_done()
                self.tasks_done += 1
                if self.tasks_done == self.count_tasks:
                    print('Consumer: Done')
                    break


def main():
    q = PriorityQueue()
    producer = Producer(q, COUNT_TASKS)
    producer.start()
    q.join()
    producer.join()

if __name__ == '__main__':
    main()
