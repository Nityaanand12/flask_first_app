# import sys
# grades = [10,2,3,34,6]
# tup_grades = (10,2,3,34,6)
# set_grade = {10,2,3,34,6}
# print(set_grade)
# tup = tup_grades + (10,)
# print(set_grade)

## set operations

# set_one = {1,2,3,3,6}
# set_two = {2,3,5,7,8}
# import copy

# def abcdd():
#     a = {"1":2,"2":3}
#     b = {"1":2,"2":3}
#     return a, b


# import sys
# print(sys.getsizeof(abcdd()))



# user_wants_number = True 
# while user_wants_number == True:
#     user_input = input("should we print again? y/n")
#     if user_input == "n":
#         user_wants_number = False

# print(set_one.intersection(set_two))
# print(set_one.union(set_two))
# print(set_one ^ set_two)

# should_continue = True
# if should_continue == True:
#     print("Hello")

# Known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know")

# if person in Known_people:
#     print("you know this {}".format(person))
# else:
#     print("you don't know this {}".format(person))

# numbers = [1,2,3,4,5,6,7,8,9]

# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number%2 == 0:
#             evens.append(number)
#     return evens

# def user_menu(choice):
#     if choice == "q":
#         return "Quit"
#     elif choice == "a":
#         return "Add"

# def who_do_you_know():
#     people = input("Enter the people you know, separated by comma")
#     known_people = people.split(",")
#     people_without_spaces = []
#     for person in Known_people:
#         people_without_spaces.append(person.strip())
#     return people_without_spaces

# def ask_user():
#     name = input("Enter your name")
#     if name in who_do_you_know():
#         print("you know {}".format(name))

# my_list = [0, 1, 2, 3, 4]
# an_equal_list = [x for x in range(5) if x%2 == 0]

# [person.strip().lower() for person in people_you_know]


# student = {"name": "Ravi", "school": "srk", "grades": (90,93,95,98,99,100)}
# def average_grade(data):
#     grades = data["grades"]
#     return sum(grades)/len(grades)

# def average_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total += sum(student["grades"])
#         count += len(student["grades"])
#     average = total/count
#     return average    
    

# class LotterPlayer:

#     def __init__(self, name, numbers):
#         print("init called")
#         self.name = name
#         self.numbers = numbers
    
#     def total(self):
#         return sum(self.numbers)

# player_one = LotterPlayer("abcd",(1,2,34))
# player_two = LotterPlayer("xya",(1,2,3))
# print(player_one == player_two)


# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []
    
#     def average(self):
#         return sum(self.marks)/len(self.marks)

# anna = Student("Anna", "MIT")
# anna.marks.append(56)
# print(anna.average())

# class Store:
#     def __init__(self, name):
#         self.name = name 
#         self.items = []
#     def add_item(self, name, price):
#         dictionary = {"name": name, "price": price}
#         self.items.append(dictionary)
#     def stock_price(self):
#         return sum([item['price'] for item in self.items()])
#         total = 0   
#         for item in self.items:
#             total += item["price"]
#         return total 

# student_attendance = {"rolf": 78, "Anna": 60}
# for name, attendance in student_attendance.items():
#     print(f"{name}, {attendance}")

# for name, age, gender in [("a", 1, "Male")]:
#     print(f"{name}, {age}, {gender}")

# *head, tail = [1,2,3]
# print(head, tail)


# def user_age_in_seconds():
#     age = int(input("Enter your age: "))
#     age_in_seconds = age * 365 * 24 * 60 * 60
#     return age_in_seconds

# print(user_age_in_seconds())


# add = lambda x, y: x + y
# # print((lambda x, y: x+ y)(3,5))
# # print(list(map((lambda x: x*2),[1,2,3])))

# double = lambda x: x*2 
# sequence = [1, 2, 3, 4]
# doubled_list = [double(x) for x in sequence]
# doubled = list(map(double, sequence))

# users = [
#     (0, "Bob", "password"),
#     (1, "Ravi", "Ravi1234")
#     ]

# username_mapping = {user[1]: user for user in users}
# print(username_mapping["Bob"])

# username_input = input("Enter your name")
# password_input = input("Enter your password")
# _, usernanme, password = username_mapping[username_input]
# if password_input == password:
#     print("Your details are correct")
# else:
#     print("your details are incorrect")

# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total *= arg 
#     return total

# print(multiply(1, 2, 3, 4))

# def add(x, y):
#     return x + y 

# num = [5, 6]
# print(add(*num))

# def add(x, y):
#     return x + y

# nums = {"x": 15, "y": 20, "z": 30}
# print(add(**nums))

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "no valid operator applied"

# def named(**kwargs):
#     print(kwargs)

# named(name="Ravi", age=25)

# def named(*args, data=None,**kwargs):
#     print(args, data, kwargs)

# named_args = {"name": "Ravi", "age": 25}
# nums = [1,2,3]
# named(*nums,data="abcd", **named_args)

# class Student:

#     def __new__(cls, name, grades):
#         print(cls, name, grades)
#         return cls.__init__(name, grades)

#     def __init__(self, name, grades):
#         print("init called")
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades)/len(self.grades)

# Rolf = Student("Rolf", (1,2,3,4,5))
# # print(Rolf.average())

# class Test:

#     @classmethod
#     def class_method(cls):
#         print(f"called method {cls}")
    
# Test.class_method(Test)


# class Book:
#     TYPES = ("HANDOVER", "PAPERBACK")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight
    
#     def __repr__(self):
#         return f"<book {self.name}>"
    
#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, Book.TYPES[0], page_weight+100)
    
#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, Book.TYPES[1], page_weight+100)

# book = Book.hardcover("harycover", 1500)
# light = Book.paperback("apm", 166)
# print(book)
# print(light)

# print(apply(1,2,3,4, operator="*"))

# class Store:

#     def __init__(self, name):
#         self.name = name
#         self.items = []
    
#     def add_item(self, name, price):
#         self.items.append({
#             "name": name,
#             "price": price
#         })

#     def __str__(self):
#         return f"{self.name}"

#     def stock_price(self):
#         return sum([item["price"] for item in self.items])

#     @classmethod
#     def franchise(cls, store):
#         return cls(store.name +" - franchise")

#     @staticmethod
#     def store_details(store):
#         return "{} total stock price: {}".format(store.name, int(store.stock_price()))

# store = Store("Test")
# store2 = Store("Amazon")
# store2.add_item("keyboard", 160)

# print(Store.franchise(store))
# print(Store.franchise(store2))

# print(Store.store_details(store))
# print(Store.store_details(store2))

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")


# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
#     def print(self, pages):
#         if not self.connected:
#             print("you're device is not connected")
#             return None
#         print(f"printing {pages} pages.")
#         self.remaining_pages -= pages
        

# # printer = Device("printer", "USB")
# # print(printer)
# # printer.disconnect()

# printer = Printer("printer", "USB", 500)
# print(printer)
# printer.print(300)
# printer.disconnect()
# printer.print(100)


# class Bookshelf:
     
#     def __init__(self, *books):
#         self.books = books
#         print(len(self.books))
    
#     def __str__(self):
#         return f"Book self contians {len(self.books)} books"

# class Book:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"book name is {self.name}" 

# book1 = Book("harry")
# book2 = Book("potter")

# bookshelf = Bookshelf(book1, book2)
# print(bookshelf)

# from typing import List

# def list_avg(sequence: List) -> float:
#     return sum(sequence)/len(sequence)

# # list_avg(123)

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisonError("Divisor cannot be 0")
#     return dividend/divisor

# def calculate(*values, operator):
#     return operator(*values)

# result = calculate(1,2,operator=divide)
# print(result)

# from operator import itemgetter

# def search(sequence, expected, finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f"could not find {expected} in sequence")

# friends =[
#     {"name":"Ravi", "age": 20},
#     {"name": "Anand", "age": 30}
#     ]

# print(search(friends, "Ravi", itemgetter("name")))

# import functools
# user = {"username":"John", "access_level":"guest"}

# def check_access(func):
#     @functools.wraps(func)
#     def inner():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permission for {user['username']}"
#     return inner

# @check_access
# def get_admin_password():
#     return "1234"

# #get_admin_password = check_access(get_admin_password)

# print(get_admin_password())

# import functools
# user = {"username":"John", "access_level":"guest"}

# def check_access(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         if user["access_level"] == "admin":
#             return func(*args, **kwargs)
#         else:
#             return f"No admin permission for {user['username']}"
#     return inner

# @check_access
# def get_password(panel):
#     if panel == "admin":
#         return "1234"
#     elif panel == "billing":
#         return "super_password"


# #get_admin_password = check_access(get_admin_password)

# print(get_password("billin"))



import functools
user = {"username":"John", "access_level":"guest"}

def make_secure(access_level):
    def check_access(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permission for {user['username']}"
        return inner
    return check_access

@make_secure("guest")
def get_admin_password():
    return "guest: 1234"

@make_secure("admin")
def get_db_password():
    return "admin: 1234"

#get_admin_password = check_access(get_admin_password)

print(get_admin_password())
print(get_db_password())































































