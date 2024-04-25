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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report():
    for item in resources:
        unit = "ml" if item in ["water", "milk"] else "g"
        print(f"{item.title()}: {resources[item]}{unit}")
    print("Money: $" + "{:.2f}".format(money))


def check_ingredients(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def process_coins():
    total = 0
    print("Please insert coins:")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennys?: ")) * 0.01
    return total


def transaction_successful(price):
    price_payed = process_coins()

    if price_payed >= price:
        if price_payed > price:
            print(
                "Here is $"
                + "{:.2f}".format(price_payed - price)
                + " dollars in change"
            )
        return True

    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(coffee, ingredients, price):
    global resources
    global money

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    money += price

    print(f"Here is your {coffee}. Enjoy!")


def process_coffee(coffee):
    ingredients = MENU[coffee]["ingredients"]
    price = MENU[coffee]["cost"]

    if not check_ingredients(ingredients):
        return False

    if not transaction_successful(price):
        return False

    make_coffee(coffee, ingredients, price)


money = 0.0

turn_off = False
command = ""

while not turn_off:
    command = input("What would you like? (espresso/latte/cappuccino): ")

    if command == "off":
        turn_off = True
    elif command == "report":
        generate_report()
    elif command in MENU:
        process_coffee(command)
    else:
        print("Wrong input!")
