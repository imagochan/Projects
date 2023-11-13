#**Find PI to the Nth Digit** - 
#Enter a number and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go.

# we print instrucctions to the console
print("enter the number to be used as the nth digit to calculate pi")

#take the inputted number using python built in functions
input_number_str = input()

#to check we print data type
#print(type(input_number_str))
#print(input_number_str)

#we cast the input (because python parses all inputs as strings) to a number
input_number_int = int(input_number_str)

#to check we print data type
#print(type(input_number_int))
#print(input_number_int)

# Bailey–Borwein–Plouffe formula attempt

#pi = sum((k**2) for k in range(1,11))
#we do input_number+1 because end parameter in range function is exclusive
#pi = sum((k**2) for k in range(0,input_number+1))

#we calculate pi
pi = sum( (1/16**k * ( 4/(8*k+1) -  2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6) )) for k in range(input_number_int+1) )

#print(pi)

#we format to n decimals
print(float(str(pi)[:input_number_int+2]))