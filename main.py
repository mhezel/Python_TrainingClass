import math

#hours = int(input("hour: "))
#rate = float(input("rate: "))

#pay = hours * rate

#print(pay)
#print(round(pay,1))
#print(math.floor(pay))
#print(math.ceil(pay))

#name = input("Name: ")  #0
#food = input("Food: ")  #1
#game = input("Game: ")  #2

#s1 = "My name is {} i love {} and playing {}"
#s2 = s1.format(name,food,game)  #PLACEHOLDERS

#s1 = "My name is {2} i love {0} and playing {1}" #CHANGING ORDERS OF THE PLACEHOLDERS
#s2 = s1.format(name,food,game)  #PLACEHOLDERS

#s1 = "My name is {newname} i love {newfood} and playing {newgame}" #VARIABLES
#s2 = s1.format(newname=name,newfood=food,newgame=game)

#item = input("Item: ")
#price = float(input("Price: "))

#s1 = "The product is %s costs %.2f" %(item,price) #PLACEHOLDERS { %s - string, (%(x)f)-float, (x = decimal place) || (%i)-int }
#print(s1)


#fruit = 'banana'
#print(fruit[2])

#n=3
#w=fruit[n-1]
#print(w)
#print(len(fruit))

#index = 0            #Needs to declare a counter
#while index<len(fruit):
    #print(fruit[0 + index])
    #index = index + 1

#for index in fruit:  #Counter is already inside the loop
    #print(index)

#counter = 0
#for index in fruit:
    #if index == 'a': #Counter is use to count how many times a character is display in the string text
        #counter = counter + 1
#print(counter)

#for letter in fruit: #Iteration Variable = letter
    #print(letter)


#s = 'Ferdy Python'
#print(s[0:4])  #Ferd
#print(s[6:7])  #P
#print(s[6:12]) #Python

#print(s[:2])  #Fe
#print(s[8:])  #Thon
#print(s[:])   #Ferdy Python

#FORMAT

#b = 'Platinum'
#a = 5
#s = "%s is one of %i shiny metals" %(b,a)
#print(s)

import math
def displayGrades():
    getAverage()

def getAverage():
    average = round((int(math) + int(science) + int(english))/3, 1)
    if average >= 80:
        print("You Passed " + '' + str(average))
    else:
        print("You failed " + '' + str(average))

print("****** Average Computing App ******")
name = input("Name: ")
math = input("Math: ")
science = input("Science: ")
english = input("English: ")
displayGrades()

