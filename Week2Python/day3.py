my_dict = {
    "a": 3500,
    "b": 8000,
    "c": 832
}

print(my_dict)

# access
print(my_dict["a"])

# add
my_dict["Rocio"] = "pretty"
print(my_dict)

# modify
my_dict["a"] = 50

# delete
del(my_dict["a"])
print(my_dict)
print(len(my_dict))

# delete dictionary
del(my_dict)
print(my_dict)

# ------------- Classes ------------ #
	# create 'property' = 'value' pairs
class Student():
	students_list = []

	def __init__(self, name, ask_id, fav_food, dream):
		self.name = name
		self.discord_id = ask_id
		self.fav_food = fav_food
		self.dream = dream
		self.students_list.append(self)

	# def my_print(self):
	# 	# for s in Student.students_list:
	# 	# 	print(s.name)
	# 	for attr, value in Student.__dict__.iteritems():
	# 	    print attr, value

# instantiate with constructor function
s1 = Student("Virginia Balseiro", "yesvirginia [Gold] [Volunteer]", "pasta", "moving to Europe")
s2 = Student("Deb Cupitt", "dcupitt", "Chololate!", "gender equity")
s3 = Student("Tim Lindley", "tl90", "Pho", "photography")



def my_iter():
	for s in Student.students_list:
	  for attr, value in s.__dict__.items():
	      print(attr, value)

my_iter()


# Is it possible to iterate through all objects that have the same parent class?
