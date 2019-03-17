#!/usr/bin/env python3
"""
by Richard White https://www.youtube.com/watch?v=wYYzteRKU7U
"""
def main():

	friends = []
	#range(2) 2 friends at a time
	for i in range(2): #2 friends at a time 
		print("Contact manager")
		name = input("Enter name: ")
		phone = input("Enter phone: ")
		email = input("Enter email: ")
		friends.append([name, phone, email])

	for i in range(len(friends)):
		print("Contact info")
		for j in range(len(friends[1])):
			print(friends[i][j])

	




if __name__ == "__main__":
	main()


