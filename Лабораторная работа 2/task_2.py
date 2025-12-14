salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend = 0
current_spend = spend

for month in range(10):
    total_spend += current_spend
    current_spend *= (1 + increase)

required_capital = total_spend - 10 * salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(required_capital))
