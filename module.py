'''file = open('1.txt','wb')

print('file name: '+file.name)
print('file closed: ',file.closed)
print('file mode: '+file.mode)'''


file2 = open('1.txt','r+')

word = file2.read(10)
print('--------------------')
print(word)
print('--------------------')
position = file2.tell()
print(position)
