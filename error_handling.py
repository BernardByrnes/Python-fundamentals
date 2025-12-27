#~eRRORS

# while True:
#     try:
#         age = int(input("what is your age?"))
#         print(age)
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter a number')
#     else:
#         print('thank you')
#         break

#Example 2

# def sum(num1,num2):
#     return num1 + num2

# print(sum("1","2"))
# =========================
# def sum(num1,num2):
#   try:
#     return num1 + num2
#   # except TypeError as err:
#   except (TypeError,ZeroDivisionError) as err:
#     print(f'please enter number {err}')

# print(sum(2,"2"))

#~Generators

# print(list(range(100)))

def make_list(num):
  result =[]
  for i in range(1,num):
    result.append(i*2)
  return result

my_crazy_list = make_list(10)

print(my_crazy_list)

# def generator_function(num):
#   for i in range(num):
#     yield i

# for item in generator_function(20):
#   print(list(item))
#~Yield
def generator_function(num):
  for i in range(num):
    yield i

g = generator_function(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))