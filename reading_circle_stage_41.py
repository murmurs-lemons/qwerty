# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ReadingCircle
def dry_run_mode():
    global _dry_run
    _dry_run = True

def set_dry_run(enabled):
    global _dry_run
    _dry_run = enabled
