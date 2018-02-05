#the first time we print the value of the name x with the first line in the funtction's body, python uses the value
#of the parameter declared in the main block, above the function definition.
#x is definie globally
x = 50;

def func(x):
	print("x is", x)
	#x is defined locally
	x = 2
	print("changing local x to ", x)

#when we call the function x it will take the global value of x only(main block x value is oly printed)
func(x)
print('x is still', x)