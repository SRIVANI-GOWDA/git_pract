# s = 'abracadabraca'
# # a = s.split()
# d = {}
# for item in s:
#     count1=s.count(item)
#     d[item] = count1
# print(d)

# s = 'hello world'
# d = {}
# for item in s:
#     if item in "aeiouAEIOU":
#         count1 = s.count(item)
#         d[item] = count1
# print(d)
# a =[1,2,3,4]
# b = [5,6,7,8]
# d = []
# for item1,item2 in zip(a,b):
#     d = item1 + item2
#     # d = a+b
#     # d[] = count_
#     print(d)

# names =['apple','google','apple','yahoo','yahoo','facebook','apple','gmail','gmail','gmail','gmail']
# d = {}
# for item in names:
#     if names.count(item)>1:
#         counta = names.count(item)
#         d[item] = counta
# print(d)

names =['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
d = {}
for index,value in enumerate(names):
    if value not in d:
        d[value] = [index]
    else:
        d[value].append(index)
print(d)



