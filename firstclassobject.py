def spam():
    print("in spam")
print(spam)
display = spam
print(display)
print(spam)
print(display)
print()
def add(a,b):
    print(a+b)
    return add

res = add(8,9)
print(res)
print(add)
print()
def demo():
    print("in demo")
def sample(func):
    print("in sample")
    print(func)
    func()
sample(demo)