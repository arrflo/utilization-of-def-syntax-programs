
def getMoney():
    _money = float(input("Amount of money you have:"))
    return _money

def getPrice ():
    _applePrice = float (input("Price of apple per piece:"))
    return _applePrice

def getAppleMax ():
    _applemax = money / price
    applerounded = int (_applemax)
    return applerounded

def getChange ():
    ttlPayment = appmax * price
    _change = money - ttlPayment
    return _change

def display (maxNumberApples,change ):
    print(f"You can buy {maxNumberApples} and your change is {change:.2f} pesos.")


money = getMoney ()
price = getPrice ()
appmax = getAppleMax ()
chAnge = getChange ()

display (appmax, chAnge)

