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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("please insert coins")
    total=int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.10
    total+=int(input("how many nickels?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def is_transaction_successfull(money_recieved,drink_cost):
    """Return True when payment is accepted and False is money is insuffiicient"""
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(order_ingredients,drink_name):
    """Deducts the required ingredients from the resouces"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Cofee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


