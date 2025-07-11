MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
profit=0
is_on=True
def check_item(coeffe):
    if MENU[coeffe]["ingredients"]["water"]<resources["water"] and MENU[coeffe]["ingredients"]["milk"]<resources["milk"] and MENU[coeffe]["ingredients"]["coffee"]<resources["water"]:
        return True
    elif MENU[coeffe]["ingredients"]["water"]>resources["water"]:
        return"water is insufficient"
    elif MENU[coeffe]["ingredients"]["milk"]>resources["milk"]:
        return"milk is insufficient"
    elif MENU[coeffe]["ingredients"]["coffee"]>resources["coffee"]:
        return "coeffe is insufficient"
def reduse_resourses(coeffe):
    resources["water"]=[resources["water"]-MENU[coeffe]["ingredients"]["water"]]
    resources["milk"]=[resources["milk"]-MENU[coeffe]["ingredients"]["milk"]]
    resources["coffee"]=[resources["coffee"]-MENU[coeffe]["ingredients"]["coffee"]]
    print(resources)
def money_calc(coeffe):
    print("enter the money")
    p=int(input("how many penny"))
    d=int(input("how many dine"))
    n=int(input("how many nickle"))
    q=int(input("how many quarter"))
    total=(p*0.01)+(d*0.10)+(n*0.05)+(q*0.25)
    if total>=MENU[coeffe]["cost"]:
        refund=round(total-MENU[coeffe]["cost"],2)
        print(f"${refund}is refunded")
        print("enjoy your coffee")
    elif total<MENU[coeffe]["cost"]:
        print('''not enough money
                money is refunded''')

print("☕")
while is_on:
    choice=input("what woul dyou like?(espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(resources)
    check_item("espresso")
    if check_item("espresso") is True:
        reduse_resourses("espresso")
        money_calc("espresso")
    else:
         print(check_item("espresso"))


