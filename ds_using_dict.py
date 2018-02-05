#dictionry is a kind of datasructure whcich holds the contacts and he numbers, we associate it with the names 
#emails
#here dictionaries are mutable like lists.
ab = {'deepika' : 'deepikasr03@gmail.com',
      'shalini' : 'shallini@hotmail.com',
      'madhu' : 'madhu@outlook.com',
      'srisha':'srisha@gmail.com'
      }
#print(len(ab))
print("total number of contacts in ab dict is" , len(ab))

for name, address in ab.items():
	print("contatct {} at {}" .format(name, address) )

ab['anjali'] = 'anajali@outlook.com'

print("total number of contacts in ab dict is" , len(ab))

ab['srisha'] = 'anjalirajendra@outlook.com'
for name, address in ab.items():
	print("contatct {} at {}" .format(name, address) )

