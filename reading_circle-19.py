# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ReadingCircle
def archive_old_records(self):
        """Перемещает записи с датой больше 90 дней в архив."""
        cutoff = datetime.now() - timedelta(days=90)
        for rec in self.records:
            if isinstance(rec, Record) and rec.created_at < cutoff:
                rec.status = "archived"
        return [r for r in self.records if r.status == "archived"]
