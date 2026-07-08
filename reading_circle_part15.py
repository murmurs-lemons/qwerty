# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ReadingCircle
def weekly_stats(self):
        """Вычисляет статистику по датам: количество участников, встреч, вопросов за неделю."""
        results = {}
        for date in self.memberships.keys() | set(m['date'] for m in self.meetings) | {q['created_at'] for q in self.questions}:
            week_start = (date - timedelta(days=date.weekday())).strftime('%Y-%m-%d')
            week_end = (week_start + timedelta(days=6)).strftime('%Y-%m-%d')
            results[week_start] = {
                'members': sum(1 for m in self.memberships.values() if start_date <= m['date'] <= end_date),
                'meetings': sum(1 for m in self.meetings if start_date <= m['date'] <= end_date),
                'questions': sum(1 for q in self.questions if start_date <= q['created_at'] <= end_date)
            }
        return results
