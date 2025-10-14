# class students:
#     def setData(self, name, age , grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display(self):
#         print(f"student name is {self.name} \n age is {self.age} \n and grade is {self.grade}")
# a = students()
# a.setData("ani", 10, "A")
# a.display()

# class rectangle:
#     def setValues(self, length , breadth):
#         self.length = length
#         self. breadth = breadth

#     def area(self):
#         print("area is", self.length * self.breadth)

#     def parameter(self):
#         print("parameter is",2 * (self.length + self.breadth))



# res = rectangle()

# res.setValues(8, 4)

# res.area()
# res.parameter()

# class calculator:
#     def setValues(self, a, b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         print("sum is ", self.a + self.b)
#     def subtract(self):
#         print("sbtract is ", self.a - self.b)

#     def multiply(self):
#         print("multiply is ", self.a * self.b)

#     def divide(self):
#         print("divide is ", self.a / self.b)

# res = calculator()
# res.setValues(8,4)
# res.sum()        
# res.subtract()        
# res.multiply()        
# res.divide()        




# class employ_salary:
#     def setDetails(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def increment(self , increment):
#         self.increment = increment 
    
#     def display(self):
#         print("updated salary is ", self.salary + self.increment)

# res = employ_salary()
# res.setDetails("aniket", 20000)
# res.increment(2000)
# res.display()



# class bank:
#     def setDetails(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposite(self, amount):
#         self.balance += amount
#         print(self.balance)

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#             print("withdraw is sucessfull remaining balance is :" , self.balance)
#         else:
#             print("insufficient balance :", self.balance)


# res = bank()
# res.setDetails("aniket", 1000)
# res.deposite(5000)
# res.withdraw(400)




# class marks:
#     def setMarks(self, m1 ,m2 , m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avgMarks(self ):
#         self.avg = (self.m1 + self.m2 + self.m3)/3
#         print(self.avg)
    
#     def display(self):
#         print(f"m1 = {self.m1}\nm2 = {self.m2}\nm3 = {self.m3}\nand average of marks is {self.avg}")


# res = marks()
# res.setMarks(10,20,30)
# res.avgMarks()
# res.display()

# class book:
#     def setInfo(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def details(self):
#         print(f"Book name is :{self.title} \nauthor name is :{self.author} \nPrice for book is :{self.price}")

# res = book()
# res.setInfo("Peace", "Denver", 499)
# res.details()


# class vote:
#     def setAge(self, age):
#         self.age = age

#     def chekEligibility(self):
#         if self.age >= 18:
#             print("person can vote ")
#         else:
#             print("person age is less than 18 cannot vote")

# res = vote()
# res.setAge(10)
# res.chekEligibility()

# class produc:
#     def setDetails(self, name, price):
#         self.name = name
#         self.price = price
#     def discount(self , percentage):
#         self.price -=  (percentage/100)*self.price
#         print("discounted price ", self.price)

# res = produc()
# res.setDetails("aniket", 2000)
# res.discount(20) 
#Create a class Movie with constructor arguments name, director, and rating.
# Add a method is_hit() that prints “Hit Movie” if rating > 8, otherwise “Average Movie”.

# class movie:
#     def __init__(self, name, director, rating):
#         self.name = name
#         self.director = director
#         self.rating = rating

#     def is_hit(self):
#         if self.rating > 8:
#             print("Movie is a hit")
#         else:
#             print("average movie")


# res = movie("kantara", "karan johar", 10)
# res.is_hit()

# Create a class ShoppingCart where items are stored in a list.
# Use the constructor to initialize an empty list and add methods to:

# class shopping_cart:
#     def __init__(self):
#         # self.item = item
#         self.lst = []

#     def add_item(self, item):
#         self.lst.append(item)

#     def remove_item(self, item):
#         self.lst.remove(item)
    
#     def display_cart(self):
#         print(self.lst)

# res = shopping_cart()
# res.add_item("apple")
# res.add_item("banana")
# res.add_item("grape")
# res.add_item("litchi")

# res.remove_item("litchi")
# res.display_cart()

# Create a class Teacher with constructor parameters name, subject, and experience.
# Add a method that gives bonus marks based on experience (>10 years = 10 marks, else 5 marks).

# class teacher:
#     def __init__(self, name, subject, exp):
#         self.name = name
#         self.subject = subject
#         self.exp = exp

#     def method(self):
#         if self.exp > 10:
#             print(f"based on {self.exp} yearss of exp {self.name} got bonus of 5 marks total 10 marks")
#         else:
#             print(f"based on {self.exp} years of exp {self.name} got 5 marks")


# res = teacher("ani", "maths", 20)
# res.method()