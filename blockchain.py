import datetime

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_secure_task(self, task, credibility):
        block = {
            "task_id": task.task_id,
            "credibility": credibility,
            "timestamp": str(datetime.datetime.now())
        }
        self.chain.append(block)
