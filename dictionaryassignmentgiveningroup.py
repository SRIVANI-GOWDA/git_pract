# 1)sentence = "hello world welcome to python programming hi there"
# output = {'h':['hello','hi'],'w':['world','welcome'],'t':['to','there'],'p':['python','programming']}
# words = sentence.split()
# output = {}
# a = sorted(words)
# for key,value in enumerate(a):
#     if value[0] not in output:
#         output[value[0]] =[value]
#     else:
#         output[value[0]].append(value)
# print(output)

###############################################################################################################
# 2)reverse dictionary if value is string
# d = {'a':'hello','b':100,'c':10.1,'d':'world'}
# e = {}
# for key,value in d.items():
#     if isinstance(value,str) :
#         e[key]=value[::-1]
#     else:
#         e[key]=value
# print(e)

####################################################################################################
# 3)number of occurence of characters
# s = "helloworld"
# d = {}
# for items in s:
#     if items not in d:
#         d[items]=s.count(items)
# print(d)

###################################################################################################
# 4)print repeated characters and count the same
# s = 'helloworld'
# d = {}
# for items in s:
#     if s.count(items)>1:
#         d[items] = s.count(items)
# print(d)

#########################################################################################################
# 5)replace value present in nested dictionary - nose with net
# d = {'a':100,'b':{'m':'man','n':'nose','o':'ox','c':'cat'}}
# for key,values in d.items():
#     d['b']['n']=['net']
# print(d)

########################################################################################
# 6)no. of occurence without using builtin
# names =['apple','google','apple','yahoo','google','facebook','gmail','yahoo']
# d = {}
# for items in names:
#     if items not in d:
#         d[items]=1
#     else:
#         d[items]+=1
# print(d)

##########################################################################
# 7)most common word
# words = ['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','the','eyes','not','around','the','eyes','dont','look','around','the','eyes','look','into','my','eyes','youre','under']
# d = {}
# for items in words:
#     if items not in d:
#         d[items]=1
#     else:
#         d[items] += 1
# a= max(d.values())
# print(a)
###################################################################################
# 8)duplicate items and no.of items its repeated
# names = ['apple','google','apple','yahoo','yahoo','facebook','apple','gmail','gmail','gmail','gmail']
# d = {}
# for items in names:
#     if names.count(items)>1:
#         d[items] = names.count(items)
# print(d)

########################################################################################
# 9)mapping products
# all_products = ['iphone','mac','gmail','maps','iwatch','windows','ios','google drive','one drive']
# apple_products = {}
# google_products = {}
# msft_products = {}
# for items in all_products :
#     if items[0] in 'i':
#         apple_products=(items)
#         if all_products.count(items)>1:
#             apple_products .append(items)
#     elif items[0] in 'g,m':
#         apple_products=(items)
#         if all_products.count(items)>1:
#             apple_products .append(items)
#     else:
#         msft_products=(items)
# print(apple_products,google_products,msft_products)

#######################################################################################
# 10)grouping flowers and animals
items = ['lotus-flower','lily-flower','cat-animal','sunflower-flower','dog-animal']
d = {'flower','animal'}
items.sort()
a = {}
for value in items:
    if value in 'flower':
        a['flower'].extend(value)
    # else:
        # a['animal'].extend(value)
print(a)
