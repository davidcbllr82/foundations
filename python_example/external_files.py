#!/usr/local/bin/python3

"""
contacts.py

Python program to manage contacts
and creates txt file and maintains persistent
data with CSV(comma sepparated values)
Credit to:Richard White

"""
def main():
	print("Contacts Manager")

	#initialize friend list
	#use of try/except. eg. if txt file gets deleted
	try:
		friends = []
		infile = open("contacts.txt", "r") #r for reading info from our contacts file
		#this will allow read the contacts in our terminal program
		line = infile.readline()
		while line:
			friends.append(line.rstrip("\n").split(",")) #it takes the "comma" out and makes the list again
			line = infile.readline()
		infile.close()
	except FileNotFoundError:
			print("Contacts.txt file not found")
			print("Starting new address book.")
			friends = []

	choice = 0

	while choice != 4:
		print("1) Add friend")
		print("2) Find friend")
		print("3) Display friend info")
		print("4) Exit program")

		choice = eval(input()) #Converts string to a numeric value 

		if choice == 1:
			print("Adding a friend")
			name = input("Enter name: ")
			email = input("Enter email: ")
			phone = input("Enter phone: ")
			friends.append([name, email, phone]) #This will append to empty list friends

		elif choice == 2:
			print("Finding friend")
			keyword = input("Look for your friends info: ")
			for friend in friends:
				if keyword in friend:
					print(friend)
			
		elif choice == 3:
			print("Displaying all friends")
			for i in range(len(friends)):
				print(friends[1])

		elif choice == 4:
			print("Quitting program. Bye! ")
		else:
			print("Invalid choice")
    # creates external file to send data to.
    # Takes the list with values(name,email,phone) and format as CSV data
	outfile = open("contacts.txt", "w") #w for write
	for friend in friends:
		outfile.write(",".join(friend) + "\n") 

main()

		
