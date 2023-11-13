#find e to the nth digits

#first we put the equation to e

# we print instrucctions to the console
print("enter the number to be used as the nth digit to calculate e")

#take the inputted number using python built in functions
input_number_str = input()

#we cast the input (because python parses all inputs as strings) to a number
input_number_int = int(input_number_str)

n = input_number_int

#it only approximates e, it does not give nth digits...
#n = input_number_int
#e = (1+1/n)**n
#print(e)

#lambda n:`(100**n+1)**100**n`[n]

#https://codegolf.stackexchange.com/questions/204718/find-the-nth-digit-of-eulers-number
#does work but it's terriby slow
print((100**n+1)**100**n/(100**n)**100**n)