from datetime import datetime, timedelta


def paired_days():
    start_day = datetime.today().date() - timedelta(datetime.today().day-1)
    for i in range(31):
        date = start_day + timedelta(i)
        if date.month == datetime.now().month:
            if int(date.day) % 2 == 0:
                date = datetime.strftime(date, "%d.%m.%y")
                print(date)


paired_days()