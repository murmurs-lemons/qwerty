# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ReadingCircle
class Template:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def create(self):
        return [TemplateField(name, type="text") for name in self.fields]


class TemplateField:
    def __init__(self, name, type="text"):
        self.name = name
        self.type = type
