class animal(object):
    def __init__(self,name):
        self.name=name
        print('animal name is {}'.format(name))

    def eat(self,food):
        self.food=food
        print('animal {} eat food {}'.format(self.name,food))


class dog(animal):
    def fetch(self, thing):
        self.thing=thing
        print('{} get the {}'.format(self.name,thing))

class cat(animal):
    def cat_eat(self):
        print('{} eating food'.format(self.name)
