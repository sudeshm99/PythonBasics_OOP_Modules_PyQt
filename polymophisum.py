class Animal(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print('[0] eat {1}'.format(self.name,food))


class Dog(Animal):
    def fatch(self,thing):
        print('{0} run after {1}'.format(self.name,thing))

    def show_affection(self):
        print('{0} dog wags tail'.format(self.name))

class Cat(Animal):
    def swatstring(self):
        print('{0} sqatstring fun'.format(self.name))

    def show_affection(self):
        print('{0} cat wags tail'.format(self.name))


for a in (Dog('dogA'),Cat('catA'),Cat('catB'),Dog('dogB')):
    print(a)
    a.show_affection()
    print('-----------------')
    
