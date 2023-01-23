enemies = 1


# global scope

def increase_enemies():
    enemies = 2
    # local scope can only be called within the function
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
player_health = 10


# this a global scope can be called anywhere within a function

def game():
    def drink_portion():
        portion_strength = 2
        print(player_health)

    drink_portion()


'''drink_portion()'''
# this function gives an error as it is called outside the function it is created in
print(player_health)
# if you create a variable within a function it is only available within the function
# modifying global scope
enemies = 2


def increase_enemies():
    global enemies
    # this code allows us to modify global scope, but it is not a nice practice
    enemies += 2
    print(f"enemies outside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# rather than the above step we can use the return fun
def increase_enemies():
    print(f"enemies outside function: {enemies}")
    return enemies + 2


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# global constants
