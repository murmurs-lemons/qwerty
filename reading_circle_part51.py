# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ReadingCircle
from datetime import datetime

class ChangeLog:
    def __init__(self):
        self._entries = []

    def record(self, action: str, entity_type: str, entity_id: int, detail: str = ""):
        self._entries.append({
            "time": datetime.now().isoformat(),
            "action": action,
            "type": entity_type,
            "id": entity_id,
            "detail": detail,
        })

    def summary(self):
        return f"Changes: {len(self._entries)}"
