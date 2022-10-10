# import time
# def execution_time(func):
#     def wrapper(*args,**kwargs):
#         start =time.perf_counter_ns()
#         print(start)
#         res = func(*args,**kwargs)
#         end =time.perf_counter_ns()
#         print(end)
#         res = start - end
#         return f"result is {res} "
#     return wrapper
# @execution_time
# def difference(a,b):
#     return a-b
# print(difference)
#
# (9,5))

####################################################################################
# def pos(func):
#     def wrapper(*args,**kwargs):
#         rs =func(*args,**kwargs)
#         return abs(rs)
#     return wrapper
# @pos
# def num(a,b):
#     return (a-b)
# print(num(40,90))

#######################################################################################
# def pos(func):
#     def wrapper(*args,**kwargs):
#         for i in range(0,3):
#             func(*args,**kwargs)

#     return wrapper
# @pos
# def char(a):
#     print(a)
# char("hello")

##################################################################################
def pos(func):
    def wrapper(*args,**kwargs):
        i =0
        while(i>2):
            func(*args,**kwargs)
            i += 1
            print(i)
    return wrapper
@pos
def char(a):
    print(a)
char("hello")