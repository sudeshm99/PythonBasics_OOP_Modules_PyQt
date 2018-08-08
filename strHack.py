number=17
i=1
tempVal= "{0:b}".format(19)
print(tempVal)
while i<=number:
    #d = Decimal(i)
    o = oct(i)
    oNew = o[1:]
    h = hex(i)
    hNew=h[2:]
    temp=5
    #"{0:b}".format(37)
    b = "{0:b}".format(i)
    print('%5s' % o)
    i+=1
    
