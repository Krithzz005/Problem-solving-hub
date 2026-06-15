from datetime import datetime

def check_dates(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")

    if d1 > d2:
        d1, d2 = d2, d1

    months = (d2.year - d1.year) * 12 + (d2.month - d1.month)

    if months == 1 and d1.day == d2.day:
        return "Exactly 1 month apart"
    elif months < 1:
        return "Less than 1 month apart"
    else:
        return "More than 1 month apart"


print(check_dates("06-06-2011", "06-07-2011"))
print(check_dates("01-03-2011", "25-03-2011"))
