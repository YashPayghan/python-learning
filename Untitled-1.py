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
def is_sufficient(order_ingridient):
    for item in order_ingridient:
        if order_ingridient[item]>=resources[item]:
            print(f"there is not enough {item}")
            return False
    return True
def process_coin():
    print("pls enter coin")
    total=int(input("how many quarters?"))*0.25
    total+=int(input("how many dimes?"))*0.1
    total+=int(input("how many nickles?"))*0.05
    total+=int(input("how many cents?"))*0.01
    return total

def transition_succesful(recied_money,drink_cost):
    if recied_money>=drink_cost:
        change=round(recied_money-drink_cost,2)
        print(f"here is change ${change}")
        global profit
        profit+=drink_cost
        return True
    else:
        return False

def make_coffee(drink_name,order_ingridient):
    for item in order_ingridient:
        resources[item]-=order_ingridient[item]
    print(f"here is your drink{drink_name}")

profit=0
is_on=True
while is_on:
    choice=input("what would you like?(espresso/latte/cappuccino)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}") 
        print(f"profit:${profit}")
    else:
        drink=MENU[choice]
        if is_sufficient( drink["ingredients"]):
            payment=process_coin()
            if transition_succesful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

