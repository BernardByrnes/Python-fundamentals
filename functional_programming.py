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
