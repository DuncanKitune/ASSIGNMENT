my_list=[]
print('List is empty', my_list)
#append these elements to my_list (10,20,30,40)
my_list.extend([10,20,30,40])

#insert the value 15 at the second position of the list
my_list.insert(2,15)
print('List after inserting 15',my_list)

#Remove the last element from my_list
my_list.remove(40)
print('List after removing the last item',my_list)

#Sort my_list in ascending order
print('List sorted in ascending order', sorted(my_list)) 

#Find and print the index of value 30 in my_list
print('List index of 30', my_list.index('30'))
