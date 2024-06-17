list1 = ['my', 'name']
list2 = ['is','jhone']
print(' ' . join(list1))
list3 =[]
# expected results are my name is jhone
list3 = list1+list2
print(list3)
# by using extend keyword
list1.extend(list2)
print(list1)
print(' ' . join(list1))