import datetime
import re

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
# яка допоможе вам визначати, кого з колег потрібно привітати. 
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження.
# Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

def get_upcoming_birthdays(users: list[dict[str, str]]):
    today = datetime.datetime.today().date()
    next_week_birthday = []

    for user in users:
        birthday = re.sub(r'\b\d{4}\b', str(today.year), user["birthday"])
        birthday = datetime.datetime.strptime(birthday, "%Y.%m.%d").date()
        if 0 < (birthday - today).days <= 7:
            if birthday.weekday() == 6: # if Sunday
                birthday = birthday + datetime.timedelta(days=1)
            elif birthday.weekday() == 5: # if Sutarday
                birthday = birthday + datetime.timedelta(days=2)
            new_dict = {user["name"]: birthday.strftime('%Y.%m.%d')}
            next_week_birthday.append(new_dict)
    
    return next_week_birthday

        

users = [
    {"name": "John Doe", "birthday": "1985.07.14"},
    {"name": "Jane Smith", "birthday": "1990.07.17"}
]

print(get_upcoming_birthdays(users))