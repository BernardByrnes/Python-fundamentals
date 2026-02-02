#higher order functions
# def greet(func):
#   func()
  
# def greet2():
#   def func():
#     return 5
#   return func

#~Decorator

def my_decorator(func):
  def wrap_func():
    print('********')
    func()
    print('********')
  return wrap_func

@my_decorator
def hello():
  print("hello bro")


@my_decorator
def bye():
  print('see yah')

hello()
hello()
bye()



def performance(fn):
  def wrapper(*args,):
    result = fn(*args)
    return result
  return wrapper

@performance
def long_time():
  for i in range (1000):
    return i*2
  