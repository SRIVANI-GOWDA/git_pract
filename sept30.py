# string ='hello world'
# for i in range(len(string)):
    # print(i,string[i])
# for i in enumerate(string):
#     print(i)
# d ={'a':2,'b':7,'d':5}
# o ={}
# for items in d:
#     o[items]=ord(items)
# print(o)
# a = "python is a programming language"
# b ={}
# s = a.split()
# for items in s:
#     b[items] = len(items)
# print(b)
# string = "helloworld"
# i = {}
# for item0,item1 in enumerate(string):
#     i[item0]=[item1]
# print([i])
# s = 'abracadabra'
# d ={}
# for i in s:
#     d[i]= s.count(i)
# print(d)
# for t in s:
#     if t not in d:
#         d[t]=1
#     else:
#         d[t] += 1
# print(d)
# a =[1,2,3,4]
# b = [6,7,8,9]
# o = []
# for i,j in zip(a,b):
#     o = i+j
#     print(o)
# names = ['apple','apple','banana','banana','pineapple']
# d ={}
# for i in names:
#     if names.count(i)>1:
#         d[i] = names.count(i)
# print(d)
# input_ = ['apple','google','flipkart','apple','amazon']
# p = {}
# for i,j  in enumerate(input_):
#     if j not in p:
#         p[j] = i
#     else:
#         p[j].append(i)
# print(p)
# l = [1,2,3,4]
# r = []
# for items in l:
#     r.append(items**2)
# print(r)
# g = ['bob','jin','adam']
# p = []
# for i in g:
#     p.append((i,len(i)))
# print(p)
# l = 'hello'
# y = []
# for i,r in enumerate(l):
#     y.append((r,i))
# print(y)
# num = 1
# for i in range(0,50):
#     print(num)
#     num +=2
# r = ['apple','google','flipkart','amazon']
# u = []
# for name in r:
#     if len(name)%2!=0:
#         u.append(name[::-1])
#     else:
#         u.append(name)
# print(u)
# element = ['alex',795,1.2,'5.6',[9,6,7]]
# list1 = []
# for item in element:
#     if isinstance(item,int):
#         value = str(item)[::-1]
#         list1.append(int(value))
#     else:
#         list1.append(item)
# print(list1)
# d = {'a':90,'b':66,'r':75}
# q = {}
# for key,value in d.items() :
#     q[value]=key
# print(q)
