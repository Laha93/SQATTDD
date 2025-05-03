class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True
