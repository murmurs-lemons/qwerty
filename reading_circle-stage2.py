# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ReadingCircle
class ValidationError(Exception): pass

def validate_name(value: str) -> str:
    if not value or len(value.strip()) < 2:
        raise ValidationError("Имя должно содержать от 2 символов")
    return value.strip()

def validate_email(value: str) -> str:
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, value):
        raise ValidationError("Некорректный формат email")
    return value.lower()

def validate_date(value: str) -> str:
    try:
        from datetime import datetime
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        raise ValidationError("Дата должна быть в формате YYYY-MM-DD")
