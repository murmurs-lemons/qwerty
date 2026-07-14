# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ReadingCircle
class Tag:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other.lower()
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"<Tag {self.name}>"


class TagManager:
    _tags = {}  # name -> Tag

    @classmethod
    def get_tag(cls, name):
        if name not in cls._tags:
            cls._tags[name] = Tag(name)
        return cls._tags[name]

    @classmethod
    def remove_tag(cls, tag):
        name = tag.name if isinstance(tag, Tag) else tag
        del cls._tags[name]
