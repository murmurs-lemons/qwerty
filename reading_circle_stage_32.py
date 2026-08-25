# === Stage 32: Добавь журнал действий пользователя ===
# Project: ReadingCircle
class ActionLogger:
    def __init__(self):
        self._actions = []

    def log(self, user_id, action_type, description):
        self._actions.append({
            'user_id': user_id,
            'type': action_type,
            'description': description,
            'timestamp': datetime.now().isoformat()
        })

    def get_recent(self, limit=10):
        return self._actions[-limit:]

    def clear(self):
        self._actions.clear()

    def summary(self):
        from collections import Counter
        counts = Counter(a['type'] for a in self._actions)
        return {k: v for k, v in counts.items()}
