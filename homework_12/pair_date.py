from datetime import datetime, timedelta


def paired_days(finish_date):
    days = abs((datetime.now() - datetime.strptime(finish_date, '%d.%m.%Y')).days)
    for i in range(days):
        day = datetime.today() + timedelta(i)
        new_date = datetime.strftime(day, "%d.%m.%y")
        if int(datetime.strftime(day, "%d")) % 2 == 0:
            print(new_date)


finish_date = "31.12.2021"

paired_days(finish_date)
