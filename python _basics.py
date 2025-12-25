# username=input("what is your username")
# password=input("please provide a password")
# passwordHidden = "*" * len(password)

# print(f" hey {username}, your password {passwordHidden} is {len(password)} letters long")

# li = [1,2,3,4,5,6]

# amazon_cart = ["notebooks", "sunglasses", "hats","shoes","basket","bananas","grapes"]
# new_cart = amazon_cart[0:]
# print(amazon_cart)
# new_cart[0]= "gum"
# print(new_cart) 
# print(amazon_cart)
# ~Matrix
# matrix = [
#   [1,2,3],
#   [2,4,6],
#   [3,6,9],
#   [4,8,12],
# ]
# print(matrix[2][2])

#~List Methods

# basket = [1,2,3,4,5]
# basket2 = ["a","b","c","d","e","f","c"]
# print(len(basket))
# basket.append(6)
# basket.insert(4,100)
# new_list = basket[0:]
# print(new_list)
# print(basket)
# # basket.pop()
# man = basket.pop(0)
# print(man)
# basket.extend([100])
# print(basket)

# print(basket.index(3))
# print(basket2.index('d'))
# print("c" in basket2)
# print(basket2.count("c"))
# basket2.sort()
# print(basket2)
# sentence= " ".join(["hi","my","name","is","Bernard"])
# print(sentence)

# #list unpacking

# a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# weapons = None
# weapons=900

# print(weapons)
# #dictionary
# dictionary = {
#   "a":1,
#   "b":2,
#   "x":[5,6,8],
#   "u": True
# }
  
# print(dictionary["x"][2])  

# user = {
#   "basket": [4,8,6],
#   "greet": "hey bro",
#   "age": 20
# }
# user2= dict(name = "mukasa")
# print(user2)
# print(user.get("age",36))

# print("basket" in user)

# print("age" in user.values())
# print(user.update({"age":55}))
# print(user)

# print(user.items())

#Tuple
# my_tuple = (1,2,3,4,5)
# print(my_tuple[2])

# my_set = {1,2,3,4,5,6,6}
# my_set.add(100)
# my_set.add(2)
# print(my_set)

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set)

# print(my_set.difference_update(your_set ))

# is_old = True
# is_licensed = True

# if is_old > 17 and is_licensed:
#   print("u can drive")
# elif is_licensed:
#   print('u have a license')
# else:
#   print("you are not of age")

  #ternary operator // conditional expression

# is_friend = ""
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)

# is_friend = True
# is_user = False

# if is_friend or is_user:
#   print("best friend")

# print(0 != 3)

# print(not(True))

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#   print("you are a master magician")
# elif is_magician and not is_expert:
#   print('you are getting there')
# elif not is_magician:
#   print('You need magic powers')

# for item in {1,2,3,4,5,6}:
#       print(item * 2)


# user = {
#   "name":"Golem",
#   "age": 5006,
#   "can_swim": False
# }
# for item in user.items():
#       print(item)
# for item in user.values():
#       print(item)


# my_list = [1,2,3,4,5,6,7,8,9,10]

# curr_num=0
# for item in my_list:
#       curr_num =curr_num + item
# print(curr_num)

# for item in range(10,0,-1):
#         print(item)

#~ENUMERATE
# fruits = ['apple', 'banana', 'cherry', 'date']
# for i,char in enumerate(fruits):
#         print(i,char)

# numbers = [10, 20, 30, 40, 50]
# for i, num in enumerate(numbers, start=1):
#     print(f"Position {i}: {num}")

# mixed = ['a', 1, 'b', 2, 'c']
# for i, item in enumerate(mixed, start=1):
#     print(f"At {i}: {item} (type: {type(item).__name__})")

#~RANGE

# for i in range(2, 8):  # Outputs: 2 4 6
#     print(i)

# for i,char in enumerate(list(range(10))):
#     print(i,char)
#     if char == 50:
#         print(f"index of 50 is:{i}")

#~while loops
# cows = [1,2,3,4,5,6,7,8,9,10]

# for i in cows:
#       while i < 6:
#             print(i)
#             i += 1

# x= 0
# while x < 50:
#       print(x)
#       x += 1
# else:
#       print("done with this")


# while True:
#       response = input("say something")
#       if (response == "bye"):
#             break

# for item in cows:
#   if item == 2:
#       continue
#   print(item)


# i = 0
# while i < len(cows):
#   print(cows[i])
#   i += 1

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0],
# ]

#iterate over picture
#if its zero print ""
#if its 1 print *

# for row in picture:
#   for pixel in row:
#     if(pixel == 1):
#       print("*",end = "")
#     else:
#       print(" ", end = "")
#   print("")

# some_list = ['a','b','c','b','d','m','n','n']

# duplicates = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in duplicates:
#       duplicates.append(value)

# print(duplicates)

#~FUNCTIONS

# def say_hello():
#   print('hello man')

# say_hello()

# def calling(name = "jack",age = 20):
#   print(f"my name is {name}, so am  {age} years old")

# calling("Ben",30)
# calling("dan",32)
# calling()
 
#~return

# def sum(num1,num2):
#   return num1 + num2

# print(sum(2,3))


# def sumX(num1,num2):
#   def sumY(num1, num2):
#     return num1 + num2
#   return sumY(num1,num2)
# print(sumX(2,5))

#~DOC STRING

# def test(a):
#   '''
# this function is just dope
#   '''
#   print(a)

# test("hey")
# help(test)

# def is_even(num):
#   if num % 2 ==0:
#     return True
#   return False

# print(is_even(51))

#~ARGS
def super_func(*args):
  print(args)
  return sum(args)

print(super_func(1,2,3,4,5))

#~Kwargs

def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 4, num2 = 8))

def man(apples):
  print(apples)