import datetime

print('---------------------------')
print('     BIRTHDAY APP')
print('---------------------------')
print()

birth_yr = int(input('What year were you born [YYYY]? '))
birth_mo = int(input('What month were you born [MM]? '))
birth_day= int(input('What day were you born [DD]? '))

# Date object of birthday
birth_moment = datetime.date(birth_yr, birth_mo, birth_day)
today = datetime.date.today()
# Date object for this year's birthday
birthday_this_yr = datetime.date(today.year, birth_mo, birth_day)

if birthday_this_yr >= today:
    # Birthday has not happened this year
    days_to_birthday = birthday_this_yr - today
else:
    # Birthday has passed this year so find next year's birthday
    days_to_birthday = birthday_this_yr.replace(year=today.year+1) - today


birth_str = '{0}/{1}/{2}'.format(birth_yr, birth_mo, birth_day)

print('It looks like you were born on ', birth_str)

if days_to_birthday.days == 0:
    print('Happy birthday')
else:
    print('Looks like your birthday is in ', days_to_birthday.days, ' days.')
    print('Hope you\'re looking forward to it!')
