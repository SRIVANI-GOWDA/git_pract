# 1)to merge two lists
# a=['a','s','d','f']
# b = ['j','k','l','m']
# print([*a,*b])
############################################################################################
# 2)remove duplicates from the list
# d =[3,6,4,6,3,8]
# e = set(d)
# print(e)

# r =[]
# for ele in d:
#     if ele not in r:
#         r.append(ele)
# print(r)
####################################################################################################
# 3)in list b and not in list a

# a=[1,2,3]
# b =[1,2,3,4]
# c = []
# for ele2 in b:
#     if ele2 not in [1,2,3]:
#         c.append(ele2)
# print(c)

################################################################################################
# 4)print nos
# a = ['abc','123','hello','23']
# d = ",".join(a)
# e = ",".join(d)
# t = []
# for ele in e:
#     if ord('0')<=ord(ele)<=ord('9'):
#         t +=ele
# print(t)
##############################################################################################################
# 5)alternate characters of string in the form of list

# d = "kijhyt"
# e = []
# i = 0
# while(i<len(d)):
#     if i%2 ==0:
#         e += d[i]
#     i +=1
# print(e)
#############################################################################################################
# 6)new list only items have even no. of characters

# names = ['apple','yahoo','google','gmail','walmart','flipkart','facebook','walmart']
# d = []

# for ele in names:
#     if len(ele)%2==0:
#          d += [ele]
# print(d)

################################################################################################################
# 7)sum of all nos and sum of only internal nos

# l =[[1,2,3],[4,5,6],[7,8,9]]
# u =[]
# for ele1,ele2,ele3 in l[::1]:
#     u =ele1 + ele2 + ele3
#     print(u)

#####################################################################################################################
# 8)reverse the list as below
# words = ['hi','hello','python']
# output = ['ih','olleh','nohtyp']
# r = []
# for items in words:

    # r.append(items[::-1])
########################################################################################################################
# 9)list comprehension to get list of even nos 1to 50

# s = [ele for ele in range(1,50) if ele%2 ==0]
# print(s)
#########################################################################################################
# 10)no of occurence
# names = ['apple','google','apple','yahoo','google']
# p = {}
#
# for word in names:
#     if word not in p:
#         p[word] = 1
#     else:
#         p[word] += 1
# print(p)
############################################################################################
# 10)find duplicate without using inbuilt
# names = ['apple','google','apple','yahoo','google']
# e = {}
# for ele in names:
#     if ele not in e:
#         e[ele] = 1
#     else:
#         e[ele] += 1
# print(e)
# i ={}
# for key,value in e.items():
#     if value >1:
#         i[key]=value
# print(i)
#############################################################################################333
# 12)largest in the list
# numbers = [10,20,30,40,50]
# for _ in range(len(numbers)-1):
#     for i in range(len(numbers)-1):
#         if numbers[i]<numbers[i+1]:
#             numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
# print(numbers[0])
#####################################################################################################
# 13)to find most common word
# words = ['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','not','around','the','eyes','dont','look','around','the','eyes','look','into','my','eyes','around']
# w = {}
# for word in words:
#     w[word] = words.count(word)
# print(w)
# print(max(w[word]))
####################################################################################################
# 15)to print numeric values
# items =['apple','1.2','google','12.6',26,'100']
# a = []
# for index,element in enumerate(items):
#     if isinstance(element,int):
#         a.append(element)
# print(a)
######################################################################################################
# 16)to rotate items in list

# d =[90,80,70,60]
# e = []
# i = 0
# for elements in range(len(d)):
#     values = d.pop()
#     e.append(values)
# print(e)
############################################################################################################
# 17)to rotate characters in a string
# string = 'hello'
# q = string.split()
# a  = []
# for elements in range(len(q)):
#     values = q.pop()
#     a.append(values)
# print(a)
#############################################################################################################
# 18)to get expected output: [1,2]
#                            [3,4]
#                            [5,6]
#                            [7,8]
#                             [9]
# i = 1
# while(i<10):
#     print([i,i+1])
#     i += 2
######################################################################################
# 19)















###########################################################################################
# 19)second list is continuation of first list
# a = [10,12,14,16,18]
# b = [20,22,24,26,28]
# start =18
# num = start + 2
# for elements in b:
#     if (num %2 ==0) :
#         if num == elements:
#             print('as expected')
#     else:
#         print("not as expected")
#     num += 2

#########################################################################################
# 20)sort odd and then followed by even nos
a = [3,4,1,7,2,12,8,6,9,11]
a.sort()
print(a)











