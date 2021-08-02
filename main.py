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
    for ingredient in MENU[selection]['ingredients']:
        if resources[ingredient] < MENU[selection]['ingredients'][ingredient]:
            print(f"Sorry, {selection} is currently unavailable.")
            return False
        else:
            if ingredient == "milk":
                milk += MENU[selection]['ingredients'][ingredient]
            elif ingredient == "water":
                water += MENU[selection]['ingredients'][ingredient]
            elif ingredient == "coffee":
                coffee += MENU[selection]['ingredients'][ingredient]
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    print(resources)
    return True


print(make_coffee('latte'))