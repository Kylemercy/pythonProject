import logging2

# 5 logging levels Debug, #2 info confirmation that things are working as expected 3 error due to a serious problem
# the software has not been able to function 4 warning an indication that something unexpected happened 5,critical a
# serious problem indicating  that the program itself may not continue running the default level of logging is set to
# warning it means it will capture everything that is a warning,critical,error and ignore info and debug
# because our logging default level is warning and ignore debug and info we change this default setting using logging config
logging2.basicConfig(level=logging2.DEBUG)


# all this logging levels reps an integer debug = 10
# info = 20,warning = 30,error = 40 critical = 50
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


# creating a logging file  this keeps record of all the changes carried out
logging2.basicConfig(filename='debug.log', level=logging2.DEBUG)
# changing logging format of the logging file
logging2.basicConfig(filename='debug.log', level=logging2.DEBUG, format='%(asctime)$:%(levelname)$:%(message)$')

logging2.basicConfig(level=logging2.DEBUG)


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


num1 = 10
num2 = 12
add_result = add(num1, num2)
print(f"{num1} '+' {num2} '=' {add_result}")
subtract_result = subtract(num1, num2)
print(f"{num1} '-' {num2} '=' {subtract_result}")
multi_result = multiply(num1, num2)
print(f"{num1} '*' {num2} '=' {multi_result}")
# to use logging inplace of print
add_result = add(num1, num2)
logging2.warning(f"{num1} '+' {num2} '=' {add_result}")
subtract_result = subtract(num1, num2)
logging2.warning(f"{num1} '-' {num2} '=' {subtract_result}")
multi_result = multiply(num1, num2)
logging2.warning(f"{num1} '*' {num2} '=' {multi_result}")
# changing our warning to debug
logging2.debug(f"{num1} '+' {num2} '=' {add_result}")
subtract_result = subtract(num1, num2)
logging2.debug(f"{num1} '-' {num2} '=' {subtract_result}")
multi_result = multiply(num1, num2)
logging2.debug(f"{num1} '*' {num2} '=' {multi_result}")
