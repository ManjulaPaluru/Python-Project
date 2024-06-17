#slicing
# str[start:stop:step]
str = 'India'
print(str[-1])
print(str[-3])
print(str[3])
print(str[0])
print(str[:-1]) # : slicing operator it will omit the -1 value ' a'  and print remaining vale  'indi'
print(str[::-1]) # it will print reverse order of string  aidnI
print(str[::-2])
str1 = "hello World"
print(str1[:3])  #hel
print(str1[::3]) #hlwl
print(str1[3:]) #lo World
print(str1[1:5:1]) #ello
