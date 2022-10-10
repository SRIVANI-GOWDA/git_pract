# names = ['laura','steve','alex','ive','james','bob']
# res =[]
# for item in names:
#     if item[0] in 'aeiouAEIOU':
#         res.append(item)
# print(res)


#####################################################################

# sentence = "python is a programming language"
# d = {}
# words = sentence.split()
# for word in words:
#     d[word]=len(word)
# print(d)

#############################################################################

# d ={'a':1,'b':2,'c':3}
# flip = {}
# for key,value in d.items():
#     flip[value]=key

##################################################################################

# l =['python','java','perl','php','python','js','c++','js','python','ruby']
# p =[]
# for items in l:
#     if items[0] in 'p':
#         p.append(items)
# print(p)
# print()
# o = [items for items in l if items[0] in'p']
# print(o)

#######################################################################################33

# names =['laura','steve','bill','james','bob','greg','scott','alex','ive']
# a = []
# for name in names:
#     if name[0] not in "aeiouAEIOU":
#         a+=  [name]
# print(a)
# print()
# c =[name for name in names if name[0] not in'aeiouAEIOU']
# print(c)

#################################################################################################

names = ['apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram','microsoft']
# s = []
# for items in names:
#     if len(items) < 6:
#         s.append(items)
# print(s)
# print()
# j = [items for items in names if len(items)<6]
# print(j)

####################################################################################################

# r = []
# for element in names:
#     if len(element) %2 ==0:
#         r += [element]
# print(r)
# f = [element for element in names if len(element)%2==0]
# print(f)

#########################################################################################################

# sentence = "python is a programming language"
# words = sentence.split()
# a = []
# for items in words:
#     a.append((items,len(items)))
# print(a)
# print()
# d = [(items,len(items)) for items in words]
# print(d)

####################################################3##########################################################

# w = ['hello','good','morning','have','a','nice','day']
# e = []
# for items in w:
#     if len(items)%2 !=0:
#         e+=[items[::-1]]
#     else:
#         e +=[items]
# print(e)
# z = [items[::-1] if len(items)%2!=0 else items for items in w ]
# print(z)

##############################################################################################################

# d ={'a':1,'b':2,'c':3}
# e ={}
# for key,value in d.items():
#     e[value] = key
# print(e)
#
# q ={value:key for key,value in d.items()}
# print(q)

################################################################################################################

# string = "python"
# e ={}
# for word in string:
#     e[word] = ord(word)
# print(e)
#
# a = {word:ord(word) for word in string}
# print(a)

##################################################################################################3
r = {'a':'880','b':67,'c':'thanks','d':99}
d = {}
for keys,values in r.items():
    if isinstance(values,str):
        d[keys]=values[::-1]
    else:
        d[keys]=values
print(d)








