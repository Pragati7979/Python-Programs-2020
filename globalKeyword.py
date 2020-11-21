# x = 10  # Global variable


# def fun():
#     x = 20
#     print("Inside fun value of x :", x)  #prints local value of x


# fun()
# print("Outside fun value of x : ", x) #prints global value of x
x = 10

x = 90


def outer():
    x = 20

    def inner():
       # global x   if this works o/p = 20,30 else: 20,90
        x = 30
    inner()
    print(x)


# global keyword gives liablity to change the global variable
outer()
print(x)
