from datetime import datetime
import re 

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
# яка допоможе вам визначати, кого з колег потрібно привітати. 
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження.
# Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

def get_upcoming_birthdays(users: dict[str, str]):
    today = datetime.today().date()
    next_week_birthday = dict()
    for user in users:
        name = user["name"]
        birthday = re.sub(r'\b\d{4}\b', str(today.year), user["birthday"])
        birthday = datetime.strptime(birthday, "%Y.%m.%d").date()
        if (birthday - today).days <= 7:
            next_week_birthday['name'] = name
            next_week_birthday['birthday'] = datetime.strftime(birthday, '%Y.%m.%d')
    
    return next_week_birthday

        

users = [
    {"name": "John Doe", "birthday": "1985.07.09"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(users))