from collections import deque

class NumberQueue:
    def __init__(self, max_size=15):
        self.queue = deque()
        self.max_size = max_size

    def add_number(self, number):
        if number in range(1, 11):
            return "Number 1-10 are not allowed in the flow."
        
        if len(self.queue) >= self.max_size:
            return "Queue is full."
        
        self.queue.append(number)
        return f"Added {number} to the queue."

    def remove_number(self):
        if not self.queue:
            return "Queue is empty."
        return f"Removed {self.queue.popleft()} from the queue."

    def get_queue(self):
        return list(self.queue)

queue = NumberQueue()
print(queue.add_number(12))
print(queue.add_number(5))
print(queue.add_number(20))

for num in range(11, 30):
    print(queue.add_number(num))

print(queue.get_queue())
print(queue.add_number(30))
print(queue.remove_number())
print(queue.get_queue())
