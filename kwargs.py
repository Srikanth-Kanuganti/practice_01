def kwArguments(*ks):
    global total
    total = 0
    for i in ks:
        total = total + i
    
kwArguments(10,20,20)
print('total of the given numbers:',total)