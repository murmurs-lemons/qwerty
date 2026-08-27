# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ReadingCircle
class ActionHistory:
    def __init__(self):
        self.history = []
        self._undo_stack = []
    
    def record(self, action):
        self.history.append(action)
        self._undo_stack.append(action)
    
    def undo(self):
        if not self._undo_stack:
            return None
        action = self._undo_stack.pop()
        self.history.remove(action)
        return action
    
    def undo_all(self):
        while self._undo_stack:
            self.undo()
