# s = 'good morning'
# for items in range(len(s)):
#     print(s[items])

#####################################################

# s = {12,13,14,25}
# for items in s:
#     print((items))

##################################################

# a ={'a':1,'s':9,"h":7}
# for keys in range(len(a)):
#     print(a[keys])

############################################################3

# q = "hello world"
# for items in reversed(q):
#     print(items)


# for items in q[::-1]:
#     print(items)

######################################################################

# string = "hello world"
# for items in range(len(string)):
#     print(items ,string[items],end = "  ")

# for items in enumerate(string):
    # print(items)

# for items in enumerate(string):
    # print(items[0])

# for index,items in enumerate(string):
#     print(index)
#######################################################################################3

# l =[1,2,3,4,5]
# res =[]
# for items in l:
#     res.append(items**2)
    # res[items]=l**2
# print(res)
###################################################################################
# names = ['steve','jone','adam']
# res = []
# for index,item in enumerate(names):
#     res.append((index,item))
# print(res)
##########################################################################################
# l = ['bob','alex']
# res = []
# for ele in l:
#     res.extend(ele*2)
# print(res)
############################################################################################3
# l = [1,2,3,5]
# res = []
# for ele in l:
#     res.append((ele,ele**2))
# print(res)
#####################################################################################################
# s = "hello"
# r = []
# for index,item in enumerate(s):
#     r.append((index,item))
# print(r)
#######################################################################################
# res = []
# for ele in range(50):
#     if ele%2==0:
#         res.append(ele)
# print(res)
#########################################################################
# names = ['laura','bob','clara','ive','ors']
# res = []
# for ele in names:
#     if ele[0] not in 'aeiou':
#         res.append(ele)
# print(res)
# o = [ele for ele in names if ele[0] in 'aeiou']
# print(o)
#####################################################################
# languages = ['pi','python','php','java']
# r = []
# for ele in languages:
#     if ele[0] in 'p':
#         r.append(ele)
# print(r)
#############################################################################
# a = ['laurence','apie','bob','steven']
# res = []
# for ele in a:
#     if len(ele)<6:
#         res +=[ele]
# print(res)
#############################################################################
# names = ['apple','banana','carrot','grape']
# res = []
# for ele in names:
#     if len(ele)%2!=0:
#         res.append(str(ele)[::-1])
#     else:
#         res.append(ele)
# print(res)


# e = [str(ele)[::-1] if len(ele)%2!=0 else ele for ele in names]
# print(e)
#########################################################################################
# elements = ['alex',12,'13.1',19.5,'90',[1,2,3]]
# list1 = []
# for ele in elements:
#     if isinstance(ele,int):
#         value = str(ele)[::-1]
#         list1.append(value)
#     else:
#         list1.append(ele)
# print(list1)
#######################################################################################
# num = 9
# for ele in range(2,num):
#     if ele %2==0:
#         print("not a prime")
#         break
# else:
#     print("a prime")
#############################################################################
# num =21
# res = []
# for num in range(2,num):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num,end = " ")
#             res.append(num)
# print(res)
############################################################################################
# s = "good day"
# e = {}
# for ele in s:
#     if s.count(ele)>1:
#         e[ele] = s.count(ele)
# print(e)
###########################################################################
# sent = "python is a programming language"
# d = {}
# words = sent.split()
# for index,ele in enumerate(words):
#     if index%2==0:
#         d[ele] = ele[::-1]
#     else:
#         d[ele] = ele
# print(d)
#####################################################################################
# s = "python is a programming language"
# e = []
# words = s.split()
# for ele in words:
#     e.append((ele,s.count(ele)))
# print(e)
# r = [(ele,s.count(ele)) for ele in words]
# print(r)
#############################################################################################
# w = ['hello','good','morning','have','a','good','day']
# q = []
# for ele in w :
#     if len(ele)%2==0:
#         q.append(ele)
#     else:
#         q.append(ele[::-1])
# print(q)
#############################################################################
# d = {'a':1,'b':2}
# w = {}
# for key,value in d.items():
#     w[value]=key
# print(w)
############################################################################
# s = "python"
# e = {}
# for ele in s:
#     e[ele]=ord(ele)
# print(e)
###########################################################################
# r = {'a':'hello','b':67,'c':'hi','d':21}
# e = {}
# for key,value in r.items():
#     if isinstance(value,str):
#         e[key]= value[::-1]
#     else:
#         e[key] = value
# print(e)
##########################################################################
s = "GOODDAY"
# for ele in s:
# if isinstance(s,str):
#     print("yes")
# else:
#      print("no")
###################################################################################
# for index,ele in enumerate(s):
#     if index%2==0:
#         print(ele,end = " ")
# for ele in s:
# print(s[::3])
# print(s[::-1])
# a = s.upper()
# print(a)
# for ele in s:
#     if ord('a')<ord(ele)<ord('z'):
#         print(chr(ord(ele)-32),end = " ")
# print(s.lower())
# for ele in s:
#     if ord('A')<ord(ele)<ord('Z'):
#         print(chr(ord(ele)+32),end = " ")
############################################
# a = "GooDdAY"
# for ele in a:
#     if ord('a')<ord(ele)<ord('z'):
#         print(chr(ord(ele)-32),end = " ")
    # else:
        # print(chr(ord(ele)+32),end = " ")
   #####     #############################################
# q = 'wedc*-84'
# r =" "
# for ele in q:
#     if ele.isalpha():
#         print(ele)
# t = "9omdm"
# for ele in t:
#     if ele in '0123456789':
#         print(ele)
# e = "akdm986+*sm"
# for ele in e:
#     if ele.isalnum():
#         print(ele,end = " ")
#########################################
# w = "madam"
# for ele in w:
#     if w[::1]==w[::-1]:
#         print("it is a palindrome")
#         break
#     else:
#         print("it is not a palindrome")
#######################################################
# string = "hi how are you"
# stri = string.replace("how","who")
# print(stri)
#############################################################
# res = " "
# for ele in string.split():
#     if ele == "how":
#         res += "what"
#     else:
#         res += ele
# print(res,end = " ")
#########################################################################
# s = "helloworld"
# t = " "
# w = s.split()
# for ele in s:
#     if ele in 'aeiou':
        # print(ele)
        # t += '*'
    # else:
    #     t += ele
# print(t)
 # for ele in s:
#     if ele in 'aeiou':
#         l += '*'
#     else:
#         l += ele
# print(l)
####################################################################################
# s = "helloworld"
# o = " "
# for ele in s:
#     if s.count(ele)>1:
#         o += "*"
#     else:
#         o += ele
# print(o)
####################################################################################
# filename_ = "abc.java"
# w = filename_.split('.')
# print(w[-1])
############################################################################33
# a = "hello"
# print(type(a.split()))
######################################################################
# st = "welcome to python"
# a = st.replace(" ",",")
# print(a)
# s = st.split()
# print(s)
######################################################################

