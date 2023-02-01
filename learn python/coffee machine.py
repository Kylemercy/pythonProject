coffee = '☕'
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        # if our comparing order is greater than the resources available
        if order_ingredient[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        # this returns false if any of the ingredient in the order is greater than that in the resource
    return True


def process_coin():
    """returns the total coin calculated which returns true when order can
    be made and false if it cant"""
    print('Please insert coin')
    total = int(input('how many quarters')) * 0.25
    total += int(input('how many dimes')) * 0.1
    total += int(input('how many nickles')) * 0.05
    total += int(input('how many pennies')) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """returns true when the payment is successful and false when it is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    # deduct the required ingredients from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}{coffee}.Enjoy!')


is_on = True
while is_on:
    choice = input('“What would you like? (espresso/latte/cappuccino):”')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
