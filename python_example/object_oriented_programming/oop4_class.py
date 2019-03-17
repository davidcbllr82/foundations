#!/usr/bin/env python3
"""
v3 - class
by Richard White https://www.youtube.com/watch?v=wYYzteRKU7U
"""
# Inheritance: Multiple classes than inherit from each other

"""
The person class defines a person in terms of a name, phone and email)
"""
class Person(object):

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

	#Method that returns string
	def __str__(self): 
	# Overriding the method and will return the following string
		return "Person[name=" + self.name + \
			    ",phone=" + self.phone + \
			    ",email=" + self.email + \
			    "]"

def enter_a_friend():
	name = input("Enter the name: ")
	phone = input("Enter phone number: ")
	email = input("Enter email: ")
	return Person(name, phone, email)

def lookup_a_friend():
	found = false
	name = input("Enter a name to lookup: ")
	for friend in friends:
		if name in friend.getName():
			print(friend)
			found = True
	if not found:
		print("No friends match that term")

def show_all_friends(friends):
	print("Showing all your contacts:")
	for friend in friends:
		print(friend)

def main():
	friends = []
	running = True
	while running:
		print("\nContacts Manager")
		print("1) new contact   2) lookup")
		print("3) show all      4) end ")
		option = input("> ")
		if option == "1":
			friends.append(enter_a_friend())
		elif option == "2":
			lookup_a_friend(friends)
		elif option == "3":
			show_all_friends(friends)
		elif option == "4":
			running = false
		else:
			print("Unrecognized input. Please try again.")
	print("Program ending.")

if __name__ == "__main__":
	main()


