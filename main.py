from collections import defaultdict
from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    # current_day_of_week = today.weekday()
    
    birthday_dict = defaultdict(list)
    
    for user in users:
        birthday = user["birthday"]
        name = user["name"]
        
        current_year_bd = birthday.replace(year=today.year)
        if current_year_bd < today:
            current_year_bd = current_year_bd.replace(year=today.year + 1)
    
        # if current_year_bd.weekday() >= 5:
        if today <= current_year_bd <= today + timedelta(days=7):
#             # Переносимо вихідний день на понеділок
#             birthday += timedelta(days=7 - birthday.weekday())
#         #перевірка чи минув день народження
#         if birthday.month == today.month and birthday.day < today.day:
#             birthday = birthday.replace(year=today.year + 1)
# #визначає день тиждень дня народження
#         if birthday.month == today.month and birthday.day == today.day:
#             day_of_week = current_day_of_week
#         else:
#             day_of_week = (birthday.weekday() - current_day_of_week) % 7
#         #робочі дні
            if current_year_bd.weekday() in (5, 6):  # Понеділок
                birthday_dict["Monday"].append(name)
        # if day_of_week <= 4:
        #     day_name = list(birthday_dict.keys())[day_of_week]
        #     birthday_dict[day_name].append(name)
            else: #переносить дн на наступний день,тобто понеділок
            # day_of_week = today + timedelta(days=(7 - current_day_of_week))
            # day_name = 'Monday'
                birthday_dict[current_year_bd.strftime("%A")].append(name)
              
# #якщо нема дня народження
#     if not any(birthday_dict.values()):
#         return {}
# #дн які минули
#     if all(user["birthday"] < today for user in users):
#         return {}

    return birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": date(1955, 10, 28)},
        {"name": "Kim", "birthday": date(1990, 10, 11)},
        {"name": "John Doe", "birthday": date(1980, 11, 24)},
        {"name": "Alice", "birthday": date(2000, 11, 1)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
