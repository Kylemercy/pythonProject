# to check if a number is a palindrome
def palindrome(num : int):
    if num < 0:
        return False
    number = num
    temp = 0

    while number:
        rem = number % 10
        temp = temp * 10 + rem
        number = number // 10

    if num == temp:
        return True
    return False


num = 121
num1 = -121
num2 = 547
print(palindrome(num))
