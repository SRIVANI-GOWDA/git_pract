# def nums(a,b):
#     print(a+b)
#
# nums(9,8)
##########################################################################
# res = lambda num:(num**2,num**3)
# print(res(9))
##############################################################################
# value_ = lambda num:num%2==0
# print(value_(8))
#############################################################################
# palindrome = lambda no :no ==no[::-1]
# print("palindrome")
# print(palindrome("hello"))
#############################################################################33
# palindrome = lambda no:("palindrome" if no==no[::-1] else "not a palindrome")

# print(palindrome("people"))
####################################################################################
# ele = lambda w: w[0]
# print(ele("rten"))
#####################################################################################
# leng = lambda iter :len(iter)
# print(leng((12,13,14,14)))
############################################################################
# num = lambda no :abs(no)
# print(num(-99))
###############################################################################
# d = {'a':5,'bat':9}
# keys_ =lambda dict_ :dict_.keys()
# print(keys_(d))
# keys_ = lambda g:[keys for keys in g]
# print(keys_(d))
################################################################################
# string = "hello"
# l = list(string)
# n = 2
# for ele in range(n):
#     value =l.pop()
#     l.insert(0,value)
# print("".join(l))
# string = "people"
# p = list(string)
# n = 3
# for ele in range(n):
#     value = p.pop()
#     p.insert(0,value)
# print("".join(p))
##########################################################################################
sent = "python is a programming language"
words = sent.split()
n =3
for ele in range(n):
    value = words.pop()
    words.insert(0,value)
print("".join(words))
