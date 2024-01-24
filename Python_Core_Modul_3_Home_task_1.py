from datetime import datetime

date_input = input('Enter date in format: YYYY-MM-DD --->')
date = datetime.strptime(date_input, "%Y-%m-%d")
current_date = datetime.today()
get_days_from_today = current_date.toordinal() - date.toordinal()

print(get_days_from_today)

# Код все розраховує вірно, але не була створена функція. Чи вважається завдання виконаним?