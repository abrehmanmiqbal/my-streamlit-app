
class Task:
    def __init__(self, task_id, data_size, cpu_cycles, deadline, is_secure):
        self.task_id = task_id
        self.data_size = data_size
        self.cpu_cycles = cpu_cycles
        self.deadline = deadline
        self.is_secure = is_secure
        self.assigned_node = None
        self.finish_time = None

    def __repr__(self):
        return f"Task({self.task_id}, Secure={self.is_secure})"


class Node:
    def __init__(self, node_id, node_type, cpu_power, bandwidth, credibility, x, y):
        self.node_id = node_id
        self.node_type = node_type
        self.cpu_power = cpu_power
        self.bandwidth = bandwidth
        self.credibility = credibility
        self.x = x
        self.y = y
        self.tasks = []

    def move(self):
        import random
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)

    def assign_task(self, task):
        self.tasks.append(task)
        task.assigned_node = self.node_id

    def distance_to(self, ox, oy):
        return ((self.x - ox)**2 + (self.y - oy)**2)**0.5

    def __repr__(self):
        return f"{self.node_id} ({self.node_type}) @({self.x},{self.y})"
