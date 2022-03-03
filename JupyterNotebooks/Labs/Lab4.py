

my_string = "I love TO program"
print(my_string.swapcase())
print(my_string.center(70,"-"))
print(my_string.partition("v"))

input1 = 3
input2 = 5
print(input1 ** input2)

arr = [1,2,2,2,2,2,3,3,3,4,5]
def getcount(arr,value):
    return arr.count(value)
print(getcount(arr,5))

x1 = 2
y1 = 5
x2 = 4
y2 = 10

def division(x, y):
    return x / y
def subtraction(x, y):
    return x - y
def returnSlope(x1,x2,y1,y2):
    return division(subtraction(y2,y1),subtraction(x2,x1))
print(returnSlope(x1,x2,y1,y2))

def addition(x,y):
    return x + y
def division(x,y):
    return x/y
def returnDistance(x1,x2,y1,y2):
    return(((x2 - x1)^2 + (y2 - y1)^2))
print(returnDistance(x1,x2,y1,y2))