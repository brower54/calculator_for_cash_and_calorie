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
    def get_today_limit_balance(self):
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance


class CaloriesCalculator(Calculator):

    def get_today_cash_remained(self):
        calories_remained = self.get_today_limit_balance
        if calories_remained > 0:
            message = (f'Сегодня можно съесть ещё что-то,'
                        f'но не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    # Денежные константы
    USD_RATE = 74.0
    EURO_RATE = 87.5
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'rub': ('руб', CashCalculator.RUB_RATE),
                      'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE)}
        cash_remained = self.get_today_limit_balance()
        if cash_remained == 0:
            return 'Денег нет, но вы держитесь'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось: {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, держись: твой долг составляет - {cash_remained}'
                       f'{name}')
        return message