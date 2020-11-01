# # Generate a random number.

# # random is a module in a package;
# # there are different packages in the standard library
# import random	
				
# # randint is a function of random
# r = random.randint(1, 100)	#Scope:1 ~ 100
# print(r)

# Practice:  Guess a number.  猜對：“恭喜。”猜錯：告訴他是比答案大/小。
import random
# Add a funciton2: allow the user to determine the scope of numbers
start = input('Please enter the start value: ')
end = input('Please enter the end value: ')
start = int(start)
end = int(end)
number = random.randint(start, end)
# Add a new function: count how many tries so far.
count = 0
while True:
	count += 1
	num = input('Please enter your guess: ')
	num = int(num)
	if num == number:
		print('Congradulations! You got it.')
		print('This is the', count, 'time of tries.')
		break
	else:
		if num > number:
			print('Should be smaller.')
		else:
			print('Should be larger.')
	print('This is the', count, 'time of tries.')
