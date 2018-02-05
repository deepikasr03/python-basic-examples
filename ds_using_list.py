#list a structure that holds the odered colection of items.
# here i creatd a list of items to be urchases by name shoplist
#list is denoted by colsed square brackets
#as the list is mutable that means any cahnges can be made , operations like append , del is performed on the list.


shop_list = ["wheat", "utensils", "coffee", "vegetables"]
print(shop_list)
print("totla number of items in my shoplist is", len(shop_list))
for item in shop_list:
	print(item)

print("i have to buy rice aslo")
shop_list.append("rice")
print("now my shoplist will be",shop_list)

print("the first element of my shoplist is", shop_list[0])
print( "i purchased the first element ", shop_list[0])
del shop_list[0]
print("now my shoplist is ",shop_list)