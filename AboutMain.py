def hello():
    print("Hello I'm from main")


def add(a, b):
    return a+b+9


print(f"I'm getting called from {__name__}")

if __name__ == '__main__':
    hello()
    print(add(1, 2))
