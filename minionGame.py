def minion_game(string):
    # your code goes here
    i=0
    j=0
    KevScore=0
    StuScore=0
    while i<len(string):
        j=i
        while j<len(string):
            subStr=string[i:j+1]
            firstChar = subStr[0:1]
            if firstChar=='A' or firstChar=='E' or firstChar=='I' or firstChar=='0' or firstChar=='U':
                KevScore+=1
            else:
                StuScore+=1
            j+=1
        i+=1            
    if KevScore>StuScore:
        print('Kevin '+str(KevScore))
    elif StuScore>KevScore:
        print('Stuart '+str(StuScore))
    else: 
        print('Drow')
