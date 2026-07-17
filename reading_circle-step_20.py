# === Stage 20: Добавь восстановление записей из архива ===
# Project: ReadingCircle
import json, os, glob

def restore_from_archive():
    archive_dir = "archives"
    if not os.path.isdir(archive_dir): return []
    results = {}
    for fpath in glob.glob(os.path.join(archive_dir, "*.json")):
        try:
            with open(fpath) as fh: json.load(fh); results[fpath] = True
        except Exception: pass
    print(results)
