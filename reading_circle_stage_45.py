# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ReadingCircle
import json
import os
import sys

def load_from_backup(backup_path):
    """Restore data from a JSON backup file.
    
    Args:
        backup_path: Path to the backup JSON file.
    
    Returns:
        The loaded data dictionary, or None if backup not found or invalid.
    
    Raises:
        FileNotFoundError: If the backup file does not exist.
        json.JSONDecodeError: If the backup file is not valid JSON.
    """
    if not os.path.exists(backup_path):
        print(f"Backup file not found: {backup_path}")
        return None
    
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Successfully loaded backup from: {backup_path}")
        return data
    except json.JSONDecodeError as e:
        print(f"Error reading backup file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error loading backup: {e}")
        return None
