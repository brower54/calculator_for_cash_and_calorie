import datetime as dt

class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    # Функция добавления записи
    def add_record(self, record):
        self.records.append(record)

    # Функция отображения сегодняшней статистики
    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    # Функция отображеения недельной статистики
    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)
    
    # Функция получения остатка на счёте
    def get_today_limit_balance:
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance