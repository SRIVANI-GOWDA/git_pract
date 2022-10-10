# d = {}
#

# def sample(func):
#     def wrapper(*args,**kwargs):
#         if func.__name__ not in d :
#             d[func.__name__] =1
#         else:
#             d[func.__name__] += 1
#         func(*args,**kwargs)
#
#     return wrapper
# @sample
# def calls(string):
#     print(string)
#
# calls("hello")
#
#
# @sample
# def datas(words):
#     print(words)
# datas("gm")
#
#
# print(d)

###########################################################################################
# count = 0
# def outer(func):
#     global count
#     count += 1
#
#     def wrapper(*args,**kwargs):
#         print(f"executing {func.__name__} function")
#         func(*args,**kwargs)
#     return wrapper
# @outer
# def add(a,b):
#     print(a+b)
#
# add(9,8)
# add(7,5)
#
# @outer
# def mul(a,b):
#     print(a*b)
# mul(9,7)
# print(count)

########################################################################################################

# count = 0
# def pos(func):
#     def wrapper(*args,**kwargs):
#         global count
#         func(*args,**kwargs)
#         count += 1
#         print(count)
    # return wrapper
#
# @pos
# def add(a,b):
#     print(a+b)
#
# add(9,8)
# add(12,14)
# print(count)

#####################################################################################################

# from time import sleep
#
# def parameter(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             sleep(n)
#             func(*args,**kwargs)
#         return wrapper
#     return outer
# @parameter(2)
# def add (a,b):
#     print(a+b)
# add(9,8)
# add(5,6)
# @parameter(3)
# def sub(a,b):
#     print(a-b)
# sub(9,7)

############################################################################
def parameter(n):
    def outer(func):
        print(f"the function is{func.__name__}")
        def wrapper(*args,**kwargs):
            for i in range(n):
                # print("hello")
                func(*args,**kwargs)
        return wrapper
    return outer
@parameter(2)
def add (a,b):
    print(a+b)
add(9,8)
add(5,6)
@parameter(3)
def sub(a,b):
    print(a-b)
sub(9,7)


