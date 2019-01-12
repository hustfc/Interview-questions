def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} hello {1}".format(key, value))
greet_me(acd='abs')
