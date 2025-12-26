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
def sum(num1,num2):
  try:
    return num1 + num2
  # except TypeError as err:
  except (TypeError,ZeroDivisionError) as err:
    print(f'please enter number {err}')

print(sum(2,"2"))