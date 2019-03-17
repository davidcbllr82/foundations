#!/usr/bin/env python3
"""
v3 - class
by Richard White https://www.youtube.com/watch?v=wYYzteRKU7U
"""
# Inheritance: Multiple classes than inherit from each other
class Person(object):
	"""
	The person class defines a person in terms of a name, phone and email)
	"""

	#Constructor
	def __init__(self, theName, thePhone, theEmail):
		self.name = theName
		self.phone = thePhone
		self.email = theEmail
	#Accesor Methods (getters)
	def getName(self):
		return self.name

	def getPhone(self):
		return self.phone

	def getEmail(self):
		return self.email

	#Mutator Methods (setters)
	def setPhone(self, newPhoneNumber):
		self.phone = newPhoneNumber

	def setEmail(self, newEmail):
		self.email = newEmail

	def __str__(self): #Method that returns string
	# Overriding the method and will return the following string
		return "Person[name=" + self.name + \
			    ",phone=" + self.phone + \
			    ",email=" + self.email + \
			    "]"
		


def main():

	friend1 = Person("Jill", "555-1234", "jbush@gmail.org")
	print(friend1.getEmail())
	friend1.setEmail("jbush@hotmail.com")
	print(friend1)


	



if __name__ == "__main__":
	main()


