import math
#x = input("Please enter the hours")
#y = input("Please enter the rate per hour")

#pay = int(x) * float(y)
#print(pay)

#STRING MANIPULATION

def stringBreak(fruit):
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(index, letter)
        index = index + 1

stringBreak("Strawberries")

def stringCount(fruit):
#word = 'banana'
    count = 0
    for letter in fruit :
        if letter =='a':  #comparing values from the given index (IF STATEMENTS REQUIRED ":" )
            count = count + 1
    print(count)

stringCount("Banana")

#Slicing the Strings

text = 'Phython Programming'
print(text[0:4])
print(text[10:11])
print(text[6:9])

print(text[8:])
print(text[:])

#Strings Concatenation "+"
#Strings Placeholders "{} % F"

name="Mhezel"
food="Spaghetti"
game="basketball"

#sampleText = "My name is {} i love {} and my favorite sport is {}"

sampleText = "{} {} {}"
sample = sampleText.format(name,food,game)
print(sample)

name="Sheena"
sample = sampleText.format(food,name,game)
print(sample)

game="Football"
sample = sampleText.format(game,game,game)
print(sample)

b = "Gold"
print("%s is a metal" % b)

b="Platinum"
a=5
s="%sis one of %s shiny metal" %(b,a)
print(s)

item="milk"
price=42.50
s="The product %s cost %.2f" %(item,price)
print(s)

greetings = "Hello Bob!"
newstring = greetings.replace('Bob','Mhezel')
print(newstring)
