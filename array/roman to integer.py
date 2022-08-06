def roman_integer(s: str):
    # s is the roman number
    # if it goes from largest to smallest add the result up
    # if it goes from smallest to largest subtract the result
    symbol = {'i': 1,
              'v': 5,
              'x': 10,
              'l': 50,
              'c': 100,
              'd': 500,
              'm': 1000,
              }
    n = len(s)
    res = 0
    for i in range(n):
        if i + 1 < n and symbol[s[i]] < symbol[s[i + 1]]:
            ''' i + 1 checks if there is a character that comes after the first 
            if so we check if the first character is smaller than the next if so we subtract the smallest character
            from the result, as it should go from largest to smallest
           > s here serve as a key use to iterate over the dictionary'''
            res -= symbol[s[i]]
        else:
            res += symbol[s[i]]
    return res


s = 'xviic'
print(roman_integer(s))
