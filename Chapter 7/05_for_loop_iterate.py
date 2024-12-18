## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)

## For Loop with Dictionary
#Print key
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key) 

#Print value
for value in my_dict.values():
    print(value)  

#Print key and value
for key, value in my_dict.items():
    print(f"{key}: {value}")
