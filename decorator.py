def func(x):
    def add(y):
        return x+y
    return add
addition = func(35)
print('sum of two numbers:',addition(10))