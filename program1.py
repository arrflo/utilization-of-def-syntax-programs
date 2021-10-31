def getName():
    _name = input("Your name:")
    return _name

def getAge():
    _age = input("Your age:")
    return _age

def getAddress():
    _address = input ("Your address:")
    return _address

def display(nAme,aGe,aDdress):
    print(f"Hi, my name is {nAme}. I am {aGe} years old and I live in {aDdress}.")

#program

name = getName()
age = getAge()
address = getAddress()

display(name, age, address)
