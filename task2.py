import random

# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами,
# що випали випадковим чином і в певному діапазоні під час чергового тиражу.
# Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Init list 
    random_numbers = []
    # Parameters validation
    if min <= 0 :
        print("Min should be greater then 0")
        return random_numbers
    elif max >= 1000:
        print("Max should be greater then 1000")
        return random_numbers
    elif quantity == 0:
        return random_numbers
    
    # Do iterations until length of list not equal quantity
    while len(random_numbers) != quantity:
        random_number = random.randint(min, max)
        # if random number exist in list skip this iteration else add to list (for uniquess)
        if random_number in random_numbers:
            continue
        else:
            random_numbers.append(random_number)
    # Sort list
    random_numbers.sort()
    return random_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)