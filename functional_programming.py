#~functions

# pure function returns the same out put on the same statement

#map, filter, zip and reduce

# def multiply_by2(li):
#   new_list=[]
#   for item in li:
#     new_list.append(item*2)
#   return new_list

# print(multiply_by2([1,2,3]))  

#~ MAP(action, iterable)
# def multiply_by2(li):
#   return li*2


# print(map(multiply_by2, [1,2,3,4])) #this returns a map object not a list

# print(list(map(multiply_by2, [1,2,3,4])))

#~FILTER

# def check_odd(item):
#   if(item % 2 == 1):
#     return item
  

# print(list(filter(check_odd,[1,2,3,4,5,5,6,7,8,9])))

# def has_a(name):
#   return "a" in name.lower()

# names = ["Alice", "Bob", "Sarah", "Mike", "Adam"]

# result = list(filter(has_a, names))

# print(result)

#~ZIP

# my_list = [1,2,3]
# your_list = [10,20,30]
# names_of = ["arthur", "charles", "Drake"]

# print(list(zip(my_list,your_list,names_of)))

# #~REDUCE
# from functools import reduce

# numbers = [1, 2, 3, 4]

# def add(acc, item):
#     return acc + item

# result = reduce(add, numbers)

# print(result)
# # 
my_list = [1,2,3]
my_list10=[19,28,23,39,46,42,74,99,26,75,42,31]
my_string = 'welcome'
my_string2 = 'belong to the city'

# def accumulator(acc,item):
#   print(acc,item)
#   return acc + item

# print(reduce(accumulator,my_list,10))

#~LAMBDA
# used for functions u will use once

# lambda param:action(param)
# from functools import reduce
# def multiply_2(item):
#   return item*2

# print(list(map(lambda item: item * 10, my_list)))
# print(list(filter(lambda item: item % 2 !=0, my_list10)))
# print(reduce(lambda acc, item: acc+item, my_list10)) 

# mixed_list = [(0,2),(4,3),(10,-1),(9,9)]
# mixed_list.sort(key=lambda x: x[1])
# print(mixed_list)

#~list,set,dictionary (List COMPREHENSIONS)

for char in "hello":
  my_list.append(char)
  
my_text = [char.upper() for char in 'chameleon']
my_list3 = [num*2 for num in range(0,100)]

print(my_text) 
print(my_list3)

simple_dict = {
  "a":2,
  "b":3
}

my_dict1 = {key:value**2 for key,value in simple_dict.items()}

print(my_dict1)
#exercise 2
my_dict3 = {num:num*2 for num in [1,2,3]}
print(my_dict3)