
def should_offload(task, node):
    return node.bandwidth > 50 and node.credibility >= 0.6

def compute_communication_time(task, node):
    return task.data_size / node.bandwidth

def compute_execution_time(task, node):
    return task.cpu_cycles / node.cpu_power

def compute_total_time(task, node, dist):
    latency = dist / 100  # simple latency model
    return compute_communication_time(task, node) + compute_execution_time(task, node) + latency
