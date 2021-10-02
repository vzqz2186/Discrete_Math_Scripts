"""
	  Program: prigram_v1.04.py
	   Author: Daniel Vazquez
		 Date: 02/12/2018

	Objective: This program has two objectives:
			1) Determine if a number is prime or not. (WORKS v1.00)
			2) Find the Greatest Common Denominator using Euclid's Method.
			   (WORKS v1.03)

  Execute via: python prigram_v1.04.py

Sample Output:  Press 1 for Prime Number, 2 for GCD. 1
				
				Number: 11
				Prime

				Number of calculations:  9
				02/12/2018 12:26:14

				--or--
				
				Press 1 for Prime Number, 2 for GCD. 2
				
				First Number: 15
				Second Number: 45

				GCD =  15
				Number of calculations:  2
				02/12/2018 12:35:59

		  Log:
			**v1.00**
				- Program to check if a number is prime or not. (WORKS)
				- Some formating.
				- Added comments.
			**v1.01**
				- Removed the SysInfo and progName functions since they never
				  worked.
			**v1.02**
				- Included function to calculate the Greatest Common
				  Denominator of two numbers. (DOES NOT WORK) 
				- Moved the Prime Number calculations to its own function
				  (primeNum).
				- Organized the main function to let the user choose between
				  prime number or GCD.
				- Added comments.
			***v1.03**
				- Included function to calculate the Greatest Common
				  Denominator of two numbers. (WORKS)
				- Added comments.
			**v1.04**
				- Modified header format.
				- Added comments.
				- Added sample output to header.

**  			 Header based on Dr. Nichols program template.				  **
"""
#-----------------------------------------------------------------------------80

import time # Used to get current time and the timer for the program
import math

def main():
	counter = 0 # Counter initializer.

	prob = int(input("Press 1 for Prime Number, 2 for GCD. ")) # Choice
					# If user types 1, then the program will evaluate for prime
	if (prob == 1): # number.
		n = int(input("\nNumber: "))
		primeNum(n, counter)
					
	if (prob == 2): # If user types 2, then the program will evaluate GCD.
		x = int(input("\nFirst Number: "))
		y = int(input("Second Number: "))
		gcd(x, y, counter)
		
	disDate() # Prints current date and time.

# Curent Date Function ------------------------------------------------------80
# Source:
#   https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M:%S'))

# Prime Number Fuction ------------------------------------------------------80
def primeNum(n, counter):
	pNum = 1
    
	start = time.time() # Starts timer.
	if(n == 1):
		print("Not Prime") # 1 is not prime.
	if(n > 1):
		for y in range(2,n):
			counter = counter + 1 # Counter of operations.
			if n % y == 0: # If the remainder of n/y is 0, then it's not prime.
				pNum = 0
				break
	end = time.time() # Ends timer.
	timepo = (end - start) * 1000 # Formats timer for printing.
	
	if (pNum == 1):
		print("Prime \n")
	if (pNum == 0):
		print("Not Prime \n")
		
	print("Number of calculations: ", counter) # Prints counter.
	print("Time: ",tiempo, "ms") # Prints timer.
	
# GDC Function --------------------------------------------------------------80
# Source:
#   https://stackoverflow.com/questions/11175131/code-for-greatest-common-
#   divisor-in-python
def gcd(x, y, counter):
	
	start = time.time() # Starts timer.
	while (y != 0):
	
		(x, y) = (y, x % y)
		counter = counter + 1 # Counter of operations.
		
	end = time.time() # Ends timer.
	tiempo = (end - start) * 1000 # Formats timer for printing.
	
	print("\nGCD = ",x) # Prints GCD for x and y.
	print("Number of calculations: ", counter) # Prints counter.
	print("Time :", tiempo, "ms") # Prints timer.

# Call Main -----------------------------------------------------------------80
main()