import datetime


def print_header():
    line_one = '------------------------------------'
    line_two = '          BIRTHDAY COUNTDOWN'
    line_three = '------------------------------------'
    print(line_one + '\n' + line_two + '\n' + line_three)


def get_birthday_from_user():
    print("When were you born: ")
    bd_year = int(input("Year [YYYY]: "))
    bd_month = int(input("Month [MM]: "))
    bd_day = int(input("Day [DD]: "))

    birthday = datetime.datetime(bd_year, bd_month, bd_day)
    return birthday


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print('You had! your birthday already this year! {}'.format(days))
    else:
        print("Happy birthday!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

if __name__ == '__main__':
    main()
