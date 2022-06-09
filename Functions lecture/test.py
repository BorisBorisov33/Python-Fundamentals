add_func = lambda a=20: lambda b: a + b

a = add_func()
print(a(30))
