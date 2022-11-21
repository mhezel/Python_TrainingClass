import math

x = input("Please enter the student Name: ")
math = input("Math: ")
science = input("Science: ")
english = input("English: ")
result = str(round((float(math)+float(science)+float(english))/ 3 ,1))

s = "Subjects: Math {}, Science {}, English {}."
ss = "{} , Congratulations You passed the subjects! with an average score of {}"
sd = "{} , Sorry You failed! with an average score of {}"
s2 = s.format(math,science,english,x,result)
print(s2)

s3 = ss.format(x,result)
s4 = sd.format(x,result)

def checkAverage(average):

    if float(result) >= 80: # CONDITIONAL STATEMENT IF STUDENT PASSES THE PASSING AVERAGE GRADE OF 80 AND ABOVE
        print(s3)
    else:
        print(s4)

checkAverage(result)