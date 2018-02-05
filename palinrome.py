def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)
something = input("enter text:")
if is_palindrome(something):
	print("yes its a palindrome")
else:
	print("its not")