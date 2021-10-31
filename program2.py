

#def apples
def getApples():
    _apples = int(input("How many apples do you want to buy?"))
    return _apples

#def oranges
def getOranges():
    _oranges = int(input("How many oranges do you want to buy?"))
    return _oranges

#def compute
def compute():
    ttlApple = aapple * 20                                          
    ttlOrange = oorange * 25                                        
    ttlPrice = ttlApple + ttlOrange
    return ttlPrice                              

#def display
def display(totalPrice):
    print(f"The total amount is {totalPrice} pesos.")

#variable
aapple = getApples()
oorange = getOranges ()
totalprice = compute ()

display (totalprice)
