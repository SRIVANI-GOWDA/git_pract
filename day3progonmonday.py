# d = {'a':1,'b':2,'c':3}
# for key in d.values():
#     print(key)
# for key in d:
#     print(d[key])
# for key,item in d.items():
#     print(item)
# s =  "hello"
# d = {}
# for char in s:
    # d[char]=ord(char)
    # print(char,d[char])


# sentence = "python is programming language"
# words = sentence.split()
# dict ={}
# l = (4,5,6,7)
# d ={}
# for index,ele in l:
#     print

sentence = " hello hai world hai good morning world hello hello"
words =sentence.split()
#using inbulit method- count()
word_count = {}
for word in words:
    word_count[word] = words.count(word)
print(word_count)