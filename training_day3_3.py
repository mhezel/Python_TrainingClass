#---------------------------OOP PYTHON---------------------------------#
#STATE - PROPERTIES
#BEHAVIOR - METHODS

#class Car:
    #counter=0
    #def __init__(self, color, model, manufacturer):
        #self.color = color
        #self.model = model
        #self.manufacturer = manufacturer
    #def display_car(self):
         #print(self.color, self.model, self.manufacturer)
    #def car_count(self):
        #print(Car.counter)

#car = Car("blue", "civic", "honda")
#car.display_car()

#car2 = Car("red", "elantra", "nissan")
#car2.display_car()

#car3 = Car("black", "montero", "mitsubishi")
#car3.display_car()

#class Dog:
    #def __greet(): #private
        #print('hello')
    #def _greet2(): #protected
        #print('hello2')
    #def greet3():  # public
            #print('hello3')

#puppy = Dog
#puppy.greet3()#-->public
#puppy._greet2() #-->protected
#puppy._greet()#-->unable to call outside the class-->private


###########################INHERITANCE########################################
#class Mother:
    #mother_name = ""
    #def mother(self):
        #print(self.mother_name)
#class Father:
    #father_name = ""
    #def father(self):
        #print(self.father_name)
#class Son(Mother, Father):
    #def parents(self):
        #print(self.father_name)
        #print(self.mother_name)

#mhezel = Son()
#mhezel.father_name = "Wasif"
#mhezel.mother_name = "Selma"
#mhezel.parents()

###########################MULTI-LEVEL INHERITANCE############################
class Students:
    def __init__(self, student_name, math_grade, science_grade, english_grade):
        self.student_name = student_name
        self.math_grade = math_grade
        self.science_grade = science_grade
        self.english_grade = english_grade

    def compute_average(self):
        # print(self.mathgrade, self.sciencegrade, self.englishgrade)
        ave = round((float(self.math_grade) + float(self.science_grade) + float(self.english_grade)) / 3)
        result = ""
        if ave >= 80:
            result = "(Passed)"
        else:
            result = "(Failed)"
        return str(ave) + result

    def displayAll(self):
        print("****STUDENT GRADES RESULT****")
        print('Name: ', self.student_name)
        print('Math: ', self.math_grade)
        print('Science: ', self.science_grade)
        print('English: ', self.english_grade)
        print('Average: ', self.compute_average())

mhezel = Students(input("Name: "),input("Math: "),input("Science: "),input("English: "))
mhezel.compute_average()
mhezel.displayAll()

