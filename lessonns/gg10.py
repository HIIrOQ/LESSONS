# def my_decorator(func):
#     def wrapper():
#         print('До вызова функции')
        
#         func()
        
#         print('После вызова функции')
        
#     return wrapper
    

# @my_decorator
# def hello():
#     print('Привет, это между вызовами')
    
# hello()

 

# def in_num(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator


# @in_num(10)
# def hello (name):
#     print('hello ',name)
    
    
# hello('dany')

# @classmethod
# @property
# @staticmethod



# def decarator(func) :
#     def wrapper(x,y) :
#         if not isinstance(x,int):
#             print('x не СООТВЕСТВУЕТ, далжно быть число ')
#         else:
#             print('correct')
#         if not isinstance(y,str) :
#             print('y не сооветсвует дожна быть строка ')
#         else :
#             print('correct')
#         return func(x,y)
#     return wrapper
# @decarator 
# def example(x,y):
#     pass
# example(5,'hello')
# example(5,5)

