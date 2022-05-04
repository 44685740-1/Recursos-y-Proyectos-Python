import calendar
year = int(input("año: "))

for i in range (1,13):
    print(calendar.month(year,i))
