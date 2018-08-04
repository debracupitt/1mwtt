# -*- coding: utf-8 -*-

# Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.
class Student():
	students_list = []

	def __init__(self, name, ask_id, fav_food, dream):
		self.name = name
		self.discord_id = ask_id
		self.fav_food = fav_food
		self.dream = dream
		self.students_list.append(self)

s1 = Student("Virginia Balseiro", "yesvirginia [Gold] [Volunteer]", "pasta", "moving to europe and working as a dev in a vegan company")
s2 = Student("Deb", "dcupitt", "Chololate", "gender equity")
s3 = Student("anne niekrenz", "Anne#9969", "icecream", "eating icecream")
s4 = Student("wendy", "alteredco", "SUSHI!", "Eating SUSHI!")
s5 = Student("Farah", "Farah Fl", "french fries", "Eating french fries")
s6 = Student("Sacha Young", "sacha[gold]", "french fries", "to return to research")
s7 = Student("Bituin Callanta", "bituin[gold]", "sashimi", "lessen the gender wage gap")
s8 = Student("t. pospisilova", "[gold]Tatiana BP#9240", "code", "Writing code")
s9 = Student("Cristina", "CristyTarantino[Gold]", "pasta", "being an amazing developer")
s10 = Student("Andreea Visanoiu", "Andreea[Gold]", "wontonmee", "becoming an University teacher")
s11 = Student("Jess", "Jessi_RS [Gold]#7015", "pasta", "work as developer by end of the year")
s12 = Student("Marwa Qabeel", "Marwa Qabeel [Gold]", "food", "Data Analyst")


def my_iter():
	for s in Student.students_list:
	    for attr, value in s.__dict__.items():
	        print("  >>>  " + attr + ": " + value)

my_iter()

# Come up with a whole taxonomy of Classes for 1MWTT

class Person():
    def __init__(self, name, email, country, gender):
        self.name = name
        self.email = email
        self.country = country
        self.gender = gender
        self.species = "human"

    def print_love(self):
        print('I love coding!')

deb = Person("deb", "debracupitt@gmail.com", "Australia", "female")

deb.print_love()
print(deb.name)
print(deb.species)

# for key in deb:
#     print(key)
print(deb.__dict__)

class Student(Person):
    def __init__(self, name, email, country, gender, id, github, level, purpose, subscribe_to, give):
        Person.__init__(self, name, email, country, gender)
        self.id = id
        self.github = github
        self.level = level
        self.purpose = purpose
        self.subscribe_to = subscribe_to
        self.give = give

jess = Student("Jess", "jess.90@gmail.com", "Germany", "female", "123", "github", "beginner", "code life", "all", "volunteer")
print(jess.__dict__)

class Volunteer(Person):
    def __init__(self, name, email, country, gender, level, availability):
        Person.__init__(self, name, email, country, gender)
        self.level = level
        self.avail = availability

harriet = Volunteer("harriet", "harrie-go@gmail.com", "UK", "female", "intermediate", "3 hours / week")
print(harriet.__dict__)
