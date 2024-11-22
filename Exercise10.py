#Exercise 10: Is it even
def getusernumber():
    return int(input("Please enter your number: "))

def display_result(is_even):
    if is_even:
        print("This value is even")
    else:
        print("This value is odd")

def checknum(num):
    return num % 2 == 0  

def mymainfunction():
    num = getusernumber()
    is_even = checknum(num)
    display_result(is_even)

mymainfunction()