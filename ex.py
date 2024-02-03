import datetime as dt
from datetime import date, timedelta
import pandas as pd
from collections import Counter
import calendar

# Установка дат начала и окончания учебного года
date_str = input("Введите дату начала учебного года (dd/mm/yyyy)\n")
beginning_of_the_year = dt.datetime.strptime(date_str, '%d/%m/%Y').date()
date_str = input("Введите дату окончания учебного года (dd/mm/yyyy)\n")
end_of_the_year = dt.datetime.strptime(date_str, '%d/%m/%Y').date()
# print(beginning_of_the_year)
# print(end_of_the_year)



# Установка дат начала и окончания каникул
vacations = []
while True:
    date_str_start = input("Введите дату начала каникул (dd/mm/yyyy)\n")
    if date_str_start == '':
        break
    try:
        beginning_of_the_vacations = dt.datetime.strptime(date_str_start, '%d/%m/%Y').date()
        date_str_end = input("Введите дату окончания каникул (dd/mm/yyyy)\n")
        end_of_the_vacations = dt.datetime.strptime(date_str_end, '%d/%m/%Y').date()
        for i in pd.date_range(beginning_of_the_vacations, end_of_the_vacations):
            vacations.append(i)
    except:
        break
print(vacations)

#Добавление праздников и перенесенных выходных дней

while True:
    date_str = input("Введите праздничный день (dd/mm/yyyy)\n")
    if date_str == '':
        break
    try:
        date = pd.Timestamp(dt.datetime.strptime(date_str, '%d/%m/%Y').date())
        print(type(date))
        vacations.append(date)
    except:
        break
print(vacations)



# Ввод дней недели, когда будут уроки
less = []

while True:
    str = input("Введите дни недели, в которые проходят уроки через '' (Пн - '0', Вт - '1' и т.д. ): \n")
    if str == '':
        break
    try:
        less = list(map(int, str.split()))
        lessons = Counter(less)
    except:
        break

print(lessons)
print(less)




# Вывод всех дат в диапазоне
# start_date = date(2023, 9, 1)
# end_date = date(2023, 9, 30)
daterange = pd.date_range(beginning_of_the_year, end_of_the_year)

for single_date in daterange:
    if single_date not in vacations:
        for item in lessons.items():
            if single_date.day_of_week == item[0]:
                for j in range(item[1]):
                    print(single_date, calendar.day_name[single_date.day_of_week])




# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days+1)):
#         for i in range(len(vacations)):
#             if not vacations[i][0] <= (start_date + timedelta(n)) <= vacations[i][1]:
#                 yield start_date + timedelta(n)
#         continue




# start_date = date(2023, 9, 1)
# end_date = date(2023, 9, 30)
# delta = end_date - start_date
# print(delta)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))