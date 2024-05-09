
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

    def get_workload(self):
        return self.workload
    
    def set_workload(self, workload):
        self.workload = workload
