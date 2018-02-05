#here function called say is defined with paramers called messege and times.If a user doesn't want to specify
#the values for the function,a function is written in such a way that it will take the deault arguments
#here if any time is not mentioned ,time is consideed as 1 as it is assigned to the times.
def say(messege, times = 1):
	print(messege * times)
#say functio n is called here with oly messege argument.it will take the default values as 1 for times
#say function is called here with messege and times arguments also
say("hai")
say("hai",8)