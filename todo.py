class Todo:
    priority = 0
    todo = "nothing"

    def __init__(self, priority, todo):
        self.priority = priority
        self.todo = todo

    def setPriority(self, priority):
        self.priority = priority
        
    def getPriority(self):
        return self.priority

    def setTodo(self, todo):
        self.todo = todo
        
    def getTodo(self):
        return self.todo

