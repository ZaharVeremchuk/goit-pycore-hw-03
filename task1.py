from datetime import datetime

# Створіть функцію get_days_from_today(date), 
# яка розраховує кількість днів між заданою датою і поточною датою.

def get_days_from_today(date: str):
    try:
        # Convert str to date
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        print(f"Value has not correct format: {e}")
        return None
    # Get today date 
    today = datetime.today().date()
    # Calculate difference in days
    difference = today - date
    return difference.days

a = get_days_from_today('2021-10-09')
print(a)