
from models import Task, Node
import random

def generate_tasks(n=10):
    return [
        Task(
            task_id=f"T{i}",
            data_size=random.randint(10, 100),
            cpu_cycles=random.randint(500, 2000),
            deadline=random.randint(5, 25),
            is_secure=random.choice([True, False])
        ) for i in range(n)
    ]

def generate_nodes(fog=3, cloud=2):
    nodes = []
    for i in range(fog):
        nodes.append(Node(f"F{i}", "fog", 1000, random.randint(50, 100), round(random.uniform(0.5, 1.0), 2), random.randint(0, 100), random.randint(0, 100)))
    for j in range(cloud):
        nodes.append(Node(f"C{j}", "cloud", 3000, random.randint(200, 500), round(random.uniform(0.7, 1.0), 2), random.randint(100, 200), random.randint(100, 200)))
    return nodes

def simulate_mobility(nodes):
    for node in nodes:
        node.move()
