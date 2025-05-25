
from offloader import compute_total_time

def schedule_tasks(tasks, nodes, user_x=0, user_y=0):
    assignments = []
    for task in tasks:
        best_node = None
        best_time = float('inf')
        for node in nodes:
            dist = node.distance_to(user_x, user_y)
            total_time = compute_total_time(task, node, dist)
            if total_time <= task.deadline and total_time < best_time and node.credibility >= 0.6:
                best_node = node
                best_time = total_time
        if best_node:
            best_node.assign_task(task)
            task.finish_time = round(best_time, 2)
            assignments.append((task.task_id, best_node.node_id, task.finish_time))
        else:
            assignments.append((task.task_id, "NOT ASSIGNED", "Deadline Missed"))
    return assignments
