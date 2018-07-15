# 함수 functions
# 입력값 parameters, 변환값 return

def hello_friends(name):
    print("hi, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"
#print("hello, {}".format(name1))
#print("hello, {}".format(name2))
#print("hello, {}".format(name3))
#print("hello, {}".format(name4))
#print("hello, {}".format(name5))
#print("hello, {}".format(name6))
#print("hello, {}".format(name7))
#print("hello, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 1) 입력값 O, 반환값 O
def sum(a, b):
    return a + b

# 2) 입력값 O, 반환값 X
def hello_friends(name):
    print("hello, {}".format(name))

# 3) 입력값 X, 반환값 O
def return_1():
    return 1
# 4) 입력값 X, 반환값 X
def hello_world():
    print("hello_world")

num_1 = return_1()
print(num_1)
