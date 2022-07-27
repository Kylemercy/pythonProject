year = int(input('Which year DO YOU WANT TO CHECK: '))
if year % 4 == 0:
    if year % 100 == 0:

      if year % 400 == 0:
        print(f'the year {year} given  is a leap year')
      else:
          print(f' the year {year} given is not a leap year')
    else:
        print(f' the year {year} given is  a leap year')
else:
    print('not a leap year')
