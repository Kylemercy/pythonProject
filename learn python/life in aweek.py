age = int(input('Enter your age: '))
year_live = 90
year_remaining = 90-age
month_remaining = year_remaining * 12
weeks_remaining = year_remaining * 52
days_remaining = year_remaining * 365
print(f'You have {year_remaining}years, {month_remaining}months,{weeks_remaining}weeks,{days_remaining}days remaining to live.')