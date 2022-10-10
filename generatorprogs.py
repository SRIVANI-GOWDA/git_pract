l = [1,2,3,4]
# def func(a):
#     for i in (l):
#         yield i**2
# print(list(func(l)))

# res = (i**2 for i in (l))
# print(list(res))
# print(next(res))
# print(next(res))
# print(next(res))

##########################################################################################################
# tuple of only numeric values in list
# items = ['flipkart',2021,'gmail',1.2,[1,2,3],2+3j,True]
# def func(a):
#     for i in a:
#         if isinstance(i,(int,complex,float)):
#             yield i
# print((tuple(func(items))))
# res = (i for i in items if isinstance(i,(int,float,complex)))
# print(next(res))

######################################################################
# only strings of odd length
# names = ['bob','steve','alex','maya','john']
# def func(a):
#     for i in a:
#         if len(i)%2!=0:
#             yield i
# print(list(func(names)))
#
# res = (i for i in names if len(i)%2!=0)
# print(next(res))
########################################################################################
# reverse if it is individual datatype
# items = ['flipkart',2021,'gmail',1.2,[1,2,3],2+3j,True]
# def func(a):
#     for i in a:
#         if isinstance(i,(int,complex,bool,float)):
#             yield str(i)[::-1]
#         else:
#             yield i[::-1]
# print(list(func(items)))

####################################################################################################
#
##############################################################
# list of pi values with increasing decimal point
# import math
# PI =math.pi
# print(PI)
#
# def func(a):
#     for i in range(a):
#         yield(round(PI,i))
#
# print(list(func(8)))

# res = (round(PI,i) for i in range(6))
# print(list(res))
##############################################################################
# generate fibanocci seriestill 10th
# def func(a):
#     num1 = 0
#     num2 = 1
#     for i in range(a):
#         yield(num1)
#         num3 =num1 + num2
#         num1 = num2
#         num2 = num3
#
# print(list(func(8)))

#############################################################################################
# function takes variable no of positional arguments as input
# def func(*args):
#     yield ("positional arguments",len(args))
#
# print(list(func(2,3,4,4)))

######################################################################################
# to checck if the arguments are more than 5

# def func(*args):
#     if len(args)>5:
#         yield ("argumants that are passed is more than 5")
#     else:
#         yield ("argumants that are passed is less than 5")
#
#
# print(list(func(2,3,4)))
#
#####################################################################33
# write a generator prog to print below output
#output RCN
# string = ("TRACXN",0)
# string = "TRACXN"
# def func(strings,b):
#     if b == 1:
#             yield(strings[1::2])
#
# print(list(func(string,1)))

############################################################################################
# TAX
# string = "TRACXN"
# def func(strings,b):
#     if b ==0:
#         yield(strings[::2])
#
# print(list(func(string,0)))
##############################################################################################
# generate a list of names starting with vowels
# names = ['laura','steve','bill','james','greig','scott','alex','ive']
# def func(name):
#     for i in name:
#         if i[0] in 'aeiou':
#             yield i
# print(list(func(names)))

############################################################################3
# to check a given no is fibonacci
# def fibo(no):
#     l = []
#     num1 = 0
#     num2 = 1
#     for i in range(12):
#         num3 = num1 + num2
#         yield(num1)
#         num1 = num2
#         num2 = num3
#         l.append(num1)
#     if no not in l:
#         yield"its not a fibonacci no"
#     else:
#         yield "its a fibonacci no"
#
# print(list(fibo(11)))
# generate expression to sum the factorial of nos 1-5
# def fact(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact * i
#         yield fact
#
# print(sum(list(fact(5))))

####################################################
l = [{"walmart":7,"gmail":3} ,{"google":77,"gmail":1}]
def char(l):
    return l["gmail"]
print(sorted(l,key = char))














# def func(a,findit):
#     num1 = 0
#     num2 = 1
#     for i in range(0,a):
#         yield(num1)
#         num3 =num1 + num2
#         num1 = num2
#         num2 = num3
#
#
# print(list(func(8,11)))