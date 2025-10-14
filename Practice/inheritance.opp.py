# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyota(car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)


# car1 = toyota("pirus", "petrol")
# print(car1.type)
# Create a base class Animal with a method speak(). Create a derived class Dog that inherits from Animal and overrides speak() to print "Dog barks".

# class Animal:
#     def speak(self):
#         return ("dogs bark")

# class dog(Animal):
#     pass

# a = dog()
# print(a.speak())


# Create a multi-level inheritance where:
# Person has attributes name and age.
# Employee inherits from Person and adds salary.
# Manager inherits from Employee and adds department.
# Each class should have a method show_details().

# class person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def show_details(self):
#         print(f"name = {self.name}\nage = {self.age}")

# class Employee(person):
#     def __init__(self,name, age,  salary):
#         super().__init__(name, age)
#         self.salary = salary
#     def show_details(self):
#         super().show_details()
#         print(f"salary = {self.salary}")
        
# class manager(Employee):
#     def __init__(self, name, age, salary, dept):
#         super().__init__(name, age, salary)
#         self.dept = dept

#     def show_details(self):
#         super().show_details()
#         print(f"department = {self.dept}")
        

# res = manager("aniekt" ,22 ,20000 ,"Operations")
# res.show_details()

# Create a base class Vehicle with attributes brand and model.
# Create two derived classes:

# Car with an additional attribute fuel_type

# Bike with an additional attribute engine_capacity.

# Each should have a show_info() method.

# class vehicle:
#     def __init__(self ,brand ,model):
#         self.brnad = brand 
#         self.model = model
#     def show_info(self):
#         print("--Information--")
#         print(f"brand: {self.brnad} \nmodel: {self.model}")
# class car(vehicle):
#     def __init__(self, brand, model , fuel_type):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
#     def show_info(self):
#         super().show_info()
#         print(f"fuel_type: {self.fuel_type}")
# class bike(vehicle):
#     def __init__(self, brand, model, engine_capacity):
#         super().__init__(brand, model)
#         self.engine_capacity = engine_capacity
#     def show_info(self):
#         super().show_info()
#         print(f"engine_capacity: {self.engine_capacity}")
# car = car("tata", "nexon", "electric")
# bike = bike("bajaj", "pulsar180", "petrol")
# car.show_info()
# bike.show_info()

# Create a class Parent1 with a method feature1(),
#  and another class Parent2 with a method feature2().
# Create a child class Child that inherits from both and calls both methods.

# class parent1:
#     def feature1(self):
#         print("cooking")

# class parent2:
#     def feature2(self):
#         print("dancing")

# class child(parent1, parent2):
#     def show(self):
#         print("children")

# obj = child()
# obj.feature1()
# obj.feature2()

#  Create a hybrid inheritance structure:

# Base class has a method show().

# ClassA and ClassB inherit from Base.

# ClassC inherits from both ClassA and ClassB.

# class base:
#     def show(self):
#         print("working")

# class A(base):
#     pass

# class B(base):
#     pass

# class C ( A, B):
#     pass

# res = C()
# res.show()