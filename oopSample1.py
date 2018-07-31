class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        print('Welcome {} to python'.format(name))

    def addMarks(self, mark):
        self.marks.append(mark)
        print(mark)

    def avg(self):
        return sum(self.marks)/len(self.marks)


s = student('sudesh');
print('------------------')
s.addMarks(12)
s.addMarks(6)
print('------------------')
print(s.avg())
