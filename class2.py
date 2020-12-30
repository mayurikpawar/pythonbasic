class Parrot:
	# class attribute
	species = "Bird"
	# instance attribute
	def __init__(self,name,age):
		self.name = name
		self.age = age
# instantiate the parrot class
blu = Parrot("blu",10)
woo = Parrot("woo",15)
# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))
#access the instance attributes
print("{} is years old".format(blu.name,blu.age))
print("{} is years old".format(woo.name,woo.age))


