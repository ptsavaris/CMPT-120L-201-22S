
professor_tells_good_joke = True
if professor_tells_good_joke:
    print ("haha")

professor_tells_good_joke = False
if professor_tells_good_joke:
    print ("haha")
else:
    print ("silence")

professor_gives_exam = False
class_likes_professor = True
professor_brings_pizza = True

if professor_gives_exam:
    print ("you suck")
elif professor_brings_pizza and class_likes_professor:
    print ("the class loves professor Kip")
else:
    print ("no comment")

integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for item in integers:
    print (item)

arr = ["blue", "yellow", "red", "green", "purple", "magenta", "lilac"]
for value in range (7):
    print (arr[value])
    print (value)

from ast import Num
from random import randint
from ssl import PEM_FOOTER
from unicodedata import name
ticket_prize = randint(0,6)
position = 0
while position != ticket_prize:
    print("You get more tickets!")
    position += 1
print ("Correct ticket prize!")

input1 = 8
input2 = 29
print (input1 + input2)

input3 = 4
input4 = 6
print (input3 + input4)

input5 = 299
input6 = .99
print (input5 + input6)

num = int(input("Enter number:"))
if (num % 2) == 0:
    print("Number is even")
else:
    print("Number is odd")

class Lizard(object):
    def __init__(self, name, height, weight): 
        self.name = name
        self.height = height
        self.weight = weight

    def info(self):
        print("Name:", self.name)
        print("Weight:", str(self.weight) + " Pounds")
        print("Height:", str(self.height) + " Inches")

x = Lizard("John", 150, 40)
x.info()    