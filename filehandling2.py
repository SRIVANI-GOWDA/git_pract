import os


path = r"G:\H drive"
os.chdir(path)


# file = open("sample.txt.txt", "r")
# print(file.read())
# print(file.read(6))
# print(file.readline())
# print(file.readline(4))
# print(file.readlines())
#######################################################################################
# 1)the line with line number
# with open("sample.txt.txt","r")as file:
#     for line in enumerate(file):
#         print(line)

##############################################################################################3
# with open("sample.txt.txt","r")as file:
#     for line in (file):
#         print(line[::-1])
#####################################################################################################
with open("sample.txt.txt","r")as file:
    for line in (file):

            print(line)
