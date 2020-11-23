def fun(*args):
    for i in args:
        print(i)


# *args taked multiple non keyworded arguments
ls = [1, 2, 3, 4, 5]
fun(*ls)


def fun2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")


fun2(**{1: 'a', 2: 'j'})
