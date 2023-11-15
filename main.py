# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     a = 10
#     print(a)
#     print_hi('PyCharm')
#     a = a * 1

# def my_func(n):
#     c = n ** 2
#     return c
#
#
# a = 10
# print(my_func(10))

# def my_func(n):
#     print('global:', a)
#     c = n ** 2
#     return c
#
#
# a = 10
# my_func(2)

# def my_func(n):
#     a = 5
#     print('local:', a)
#     c = n ** 2
#     return c
#
#
# a = 10
# my_func(2)
# print(a)

# def my_func(n):
#     global a
#     a = 5
#     print('global:', a)
#     c = n ** 2
#     return c
#
#
# a = 10
# my_func(2)
# print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def fun():
#     global a
#     a = 1
#     print(a)
#     return
#
#
# fun()
# print(a)

# print(dir(__builtins__))
# print(dir(__builtins__.str.__module__))

# a = 1
# print(globals())

# def f(x,y):
#     print("start f()")
#     s
#     print(locals())
#     return
#
# s = 1
# f(1,2)
# print(globals())

x = 10


# def outer():
#     x = 1
#
#     def inner(y):
#         nonlocal x
#         x = x + 1
#         print(x)
#         y(inner)
#     inner(inner)
#     print(x)
#
#     def inner2():
#         nonlocal x
#         x = 3
#
#
# outer()


# def outer():
#     x = 1
#
#     def inner(y):
#         nonlocal x
#         x = 2
#         y(inner)
#     inner(inner)
#     print(x)
#
#     def inner2():
#         nonlocal x
#         x = 3
#
#
# outer()

def outer():
    x = 1

    def inner(y):
        nonlocal x
        x = 2
        # y(inner)
    inner(inner)
    print(x)

    def inner2():
        nonlocal x
        x = 3


outer()