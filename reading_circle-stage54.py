# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: ReadingCircle
class Favorites:
    def __init__(self):
        self._favorites = set()

    def add(self, record_id):
        self._favorites.add(record_id)

    def remove(self, record_id):
        self._favorites.discard(record_id)

    def is_favorited(self, record_id):
        return record_id in self._favorites

    def list_favorites(self):
        return sorted(self._favorites)

    def toggle(self, record_id):
        if self.is_favorited(record_id):
            self.remove(record_id)
        else:
            self.add(record_id)

    def count(self):
        return len(self._favorites)

    def quick_access(self, all_records):
        return [r for r in all_records if r['id'] in self._favorites]
