def wrap(string, max_width):
    i=0
    re=''
    while i<len(string):
        print(i,i+max_width)
        a=string[i:i+max_width]
        i=i+max_width
        print(i)
        re=re+a+'\n'
        
    print(re)    

wrap('ABCDEFGHIJKLMNOPQRSTUVWXYZ',4)
