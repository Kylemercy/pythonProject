def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
    # tittle case converts only thf first letter to capital letter


format_name('ANDY', 'MIKE')


# using return function
def full_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Result {formated_f_name} {formated_l_name} '


print(full_name(input('Whats your first name: '), input('Whats your last name: ')))
