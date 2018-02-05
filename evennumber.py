def unique_list(l):
	x =[]
	for i in l:
		if i % 2 == 0 :
			x.append(i)
	return x

print(unique_list([1,2,3,4,5,6,7,8,9]))