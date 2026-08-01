# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ReadingCircle
class Profile:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books_read = 0
    
    def read_book(self):
        self.books_read += 1
    
    def __str__(self):
        return f"{self.name} ({self.email}) — прочитано: {self.books_read}"

def add_profile(profiles, name, email):
    for p in profiles:
        if p.name == name and p.email == email:
            return None
    new = Profile(name, email)
    profiles.append(new)
    return new
