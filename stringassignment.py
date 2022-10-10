# s = 'hello world'
# if isinstance(s,str):
#     print('it is a string')
# else:
#     print('it is not a string')

############################################################################################3


# to print elements present in even indices
# a = 'hello hai world'
# i =0
# while i <len(a):
#     if i%2==0 :
#         print(a[i])
#     i += 1

##############################################################################################33

#to print alternate characters

# a ='hai hello world'
# i = 0
# while i <len(a):
#     print(a[i],end = "  ")
#     i +=2

##############################################################################################
# a ='hai hello world'
# for item in a[::-1]:
#     print(item,end = "  ")

###################################################################################################
# a = "hI HELlo WoRLD"
# i = 0
# while i <len(a):
#     if ord('a')<=ord(a[i])<=ord('z'):
#         print(chr(ord(a[i])-32),end = " ")
#         # print(b)
#     else:
#         print(chr(ord(a[i])+32),end = "  ")
#         # print(c)
#     i +=1
######################################################################################################
# a ="hi HElLO WorlD"
# print(a.swapcase())

#########################################################################################################
# extract numeric values
# s ="hi986thiu754nmll66"
# i = 0
# while i<len(s):
#     if ord(s[i]) not in ord('a')<=s[i]
# b = 0
# while i < len(s):
#     if ord('a')<=!ord(a[i])<=!ord('z'):
#     if s[i].isdigit():
#         d =int(s[i])
#         # b = 0
#         b = b+d
#     i += 1
# print(b)

#####################################################################################

# s ="hi986thiu754nmll66"
# i = 0
# # while i<len(s):
# #     if ord(s[i]) not in ord('a')<=s[i]
# b = 0
# while i < len(s):
# #     if ord('a')<=!ord(a[i])<=!ord('z'):
#     if s[i] in '0123456789':
#         d =int(s[i])
#         # b = 0
#         b = b+d
#     i += 1
# print(b)

###########################################################################
#alphabetic values from string
# a = 'asbn345rhty6knj8909'
# i = 0
# b = " "
# while i<len(a):
#     if a[i] not in '0123456789':
#         f = str(a[i])
#         b = b + f
#     i += 1
# print(b)





######################################################################################################

# a = 'hty6knj8909'
# b = " "
# while i<len(a):
#     if a[i].isalpha():
#         # f = str(a[i])
#         b = b + f
#     i += 1
# print(b)


#############################################################################################
# 10) extract alphabetical values from string

# s = "sd34hj67kmn7*+"
# g =[]
# for i in s:
#     if i.isalpha():
#         g +=i
# print(g)

#without using inbuilt
# i =0
# while i<len(s):
#     if(ord('a')<=ord(s[i])<=ord('z')):
#         print(chr(ord(s[i])-32))
#     i += 1

#########################################################################################################
# 11)to extract only special characters from string
# u ="sw56+*mn4@#6gnk"
# q =""
# for item in u:
#     if item.isalnum():
#         # print("not a special character")
#         q +=item
#     else:
#         print(item)

#without using inbuilt functions
# e = ""
# for item in u:
#     if (ord('a')<=ord(item)<=ord('z')) or (ord('A')<=ord(item)<=ord('Z')) or (ord('1')<=ord(item)<=ord('9')):
#         e += item
#     else:
#         print(item)

##############################################################
# 12)alphanumeric characters from the string
# t = "s3k4n67"
# z = ""
# for item in t:
#     if item.isalnum():
#         print(item)

#without using inbuilt method
# for item in t:
#     if (ord('a')<=ord(item)<=ord('z')) or (ord('A')<=ord(item)<=ord('Z')) or (ord('1')<=ord(item)<=ord('9')):
#         print(item)
#     else:
#         item +=t

################################################################################################
# 13)string is palindrome or not with or without using reversed

# string = "hello everyone"
# rev =""
# for item in reversed(string):
#     rev += item
# print(rev)

# without reversed
# for item in string[::-1]:
#     rev += item
# print(rev)

########################################################################################################
# string = "hi how are you"
# res = " "
# res = string.replace('how','who')
# print(res)
# for items in string.split():
#     if items == 'how':
#         res += "who"
#     else:
#         res += items
# print(res)

#############################################################################################################
# 15)all vowel with * in hello world
# s = "hello world"
# l = " "
# for ele in s:
#     if ele in 'aeiou':
#         l += '*'
#     else:
#         l += ele
# print(l)

#################################################################################################################

# 16) repeated alphabets with *
# string = "hello world"
# o = " "
# for ele in string:
#     if string.count(ele)>1:
#         o += '*'
#     else:
#         o +=ele
# print(o)

##################################################################################
# 17)accept filename from the user and print the extension

# a = input()
# b = a.split('.')
# print(b[1])

#####################################################################################
# 18)convert string into list
# string ='hello all good morning'
# a = string.split()
# print(a)
# b = " ".join(a)
# print(b)

#####################################################################################
# 19)hello welcome to python to a comma separated string

# string = 'hello welcome to python'
# b = string.replace(" "," ,")
# print(b)

#######################################################################################
# 20)ASCII values in string

# p = "hello"
# i =
# for char in p:
#     print((ord(char)),end = " ")
# print(i, end = " ")

##################################################################################################
# 21)longest word
# sentence ="hi world welcome to python"
# print(max(sentence.split(),key = len))

######################################################################################
# 22)sum of nos

# a = '98gnjdj5'
# d = 0
# e = 0
# for items in a:
#     if items.isdigit():
#         e = int(items)
#         d = d +e
# print(d)

##############################################################################

# 23)occurence of characters without using inbuilt

# o ="hello"
#
# d = {}
# for i in o:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#####################################################################################################
# 24
# a = "lgghfh"
# l = ''
# count1 = 0
# for ele in a:
#     if a.count(ele)>=2:
#         l += ele
# print(l)

##############################################################################################
# 25
# r = "sfgejrt45"
# s = ""
# i =0
# while i<=len(r):
#     print(r[i])
#     i += 2
##########################################################################################################
# 26
# r = "this is programming language and programming language is fun"
# h = ""
# p = (max(r.split()))
###################################################################################################################
# 27 to count white spaces
# y = "bn hjh 87+-"
# print(y.count(" "))
#######################################################################################################
# 29) non repeated characters

# p = "dfghjhgf"
# r = " "
# for ele in p:
#     if p.count(ele)==1 :
#         r += ele
# print(r)
#################################################################################
# 30)to print only consonants
# s = "optuirsd"
# w = " "
# for ele in s:
#     if ele not in 'aeiou':
#          w +=ele
# print(w)
##################################################################
# 31)count capital letters

# a= "OWEhjY"
# e = ""
# for ele in a:
#     if (ord('A')<=ord(ele)<=ord('Z')):
#         e+=ele
# print(len(e))
###################################################3
# 32)first repeating character
# a = "werefrtff"
# s = ""
# for ele in a:
#     if a.count(ele)>=2:
#         s += ele
# print(s[0])
#################################################################################3
# 35)only nos
# s= "wer45m*/-"
# k = ""
# for ele in s:
#     if ord('0')<=ord(ele)<=ord('9'):
#         k += ele
# print(k)
############################################################################################3