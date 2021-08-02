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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def coffee_prompt():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    return choice


def process_payment(price):
    payment = 0
    while price > payment:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        payment += (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
        if payment < price:
            print(f"More funds required! {round((price - payment),2)}")
    if payment > price:
        print(f"Your change is ${round((payment - price), 2)}")
        return True
    else:
        return True


def make_coffee(selection):
    water = 0
    milk = 0
    coffee = 0
    for ingredient in selection['ingredients']:
        if resources[ingredient] < selection['ingredients'][ingredient]:
            return False
        else:
            if ingredient == "milk":
                milk += selection['ingredients'][ingredient]
            elif ingredient == "water":
                water += selection['ingredients'][ingredient]
            elif ingredient == "coffee":
                coffee += selection['ingredients'][ingredient]
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    return True


def report():
    for item in resources:
        print(f"{item} : {resources[item]}")


def machine():
    off = False
    while not off:
        selection = input("What would you like? (espresso/latte/cappuccino):")
        if selection == 'off':
            off = True
            print("powering down...")
        elif selection == "report":
            report()
        elif selection not in MENU:
            print('not a valid selection')
        else:
            process = MENU[selection]
            payment = process_payment(process['cost'])
            if payment:
                coffee = make_coffee(process)
                if not coffee:
                    print(f"Sorry, {selection} is currently unavailable.")
                    print('returning your payment...')
                else:
                    resources['money'] += process['cost']
                    print("Here's your coffee!")

machine()