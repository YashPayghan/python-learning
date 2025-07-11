
stocks={"reliance pvt.ltd":1059,"hdfc bank":2005,"tcs":3451,"microsoft":2000,"mrf":50000,"bajaj":200,"lic":200}
def your_investment():
    stock_name=input("Which stock you want to buy\n").lower()
    if stock_name not in  stocks:
        print("NO SUCH STOCK EXISTED")
    else:
        print("price of that stock is :",stocks[stock_name])
        quantity=int(input("How many stock you want to buy\n"))
    stock_price=stocks[stock_name]
    investment=stock_price*quantity
    print ("Your Investment is:",investment)
    with open("portfolio.txt","w") as file:
        file.write(f"Stock Name:{stock_name}")
        file.write(f"Stock Price:{stock_price}")
        file.write(f"your investment is :{investment}")

your_investment()
again=input("Do you want to buy another stock (yes/no)").lower()
while again=="yes":
    your_investment()