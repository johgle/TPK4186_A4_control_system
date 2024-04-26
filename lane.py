
import random


class Lane:

    def __init__(self, id):
        self.id = id
        self.tasks = []
        self.workload = 0

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_tasks(self):
        return self.tasks
        
    def append_task(self, task):
        self.tasks.append(task)

    def generate_workload(self):
       self.workload = random.random() #number between 0 and 1

    def get_workload(self):
        return self.workload
    
    def set_workload(self, workload):
        self.workload = workload
