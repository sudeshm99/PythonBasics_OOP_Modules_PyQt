'''class myclass:
    def test():
        print('fun')
        

this = myclass()
this.test()
print('-----')
print(this)


class classVal:
    class_Val = 'class_Val'

x = classVal();
print(x.class_Val)
x.class_Val='new Val'
print(x.class_Val)
del x.class_Val
print(x.class_Val)'''

import __builtin__

t = (1,2,3)
val = __builtin__.hash(t)
print(val)
