class A(object):
    def doing(self):
        print('ding this in obj A')

class B(A):
    pass

class C(object):
    def doing(self):
        print('doing this in obj C')

class D(C,B):
    pass

d = D();
d.doing();
print(D.mro())
