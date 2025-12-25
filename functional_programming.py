#~functions

# pure function returns the same out put on the same statement

#map, filter, zip and reduce

# def multiply_by2(li):
#   new_list=[]
#   for item in li:
#     new_list.append(item*2)
#   return new_list

# print(multiply_by2([1,2,3]))  

#~ map(action, iterable)
def multiply_by2(li):
  return li*2


print(map(multiply_by2, [1,2,3,4])) #this returns a map object not a list

print(list(map(multiply_by2, [1,2,3,4])))

#~Filter

def check_odd(item):
  if(item % 2 == 1):
    return item
  

print(list(filter(check_odd,[1,2,3,4,5,5,6,7,8,9])))

def has_a(name):
  return "a" in name.lower()

names = ["Alice", "Bob", "Sarah", "Mike", "Adam"]

result = list(filter(has_a, names))

print(result)

#~ZIP

my_list = [1,2,3]
your_list = [10,20,30]
names_of = ["arthur", "charles", "Drake"]

print(list(zip(my_list,your_list,names_of)))