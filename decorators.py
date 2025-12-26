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
bye()