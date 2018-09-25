import urllib.request as r

'''
with open('pap.txt') as book:
    for line in book:
        print(line)
'''

'''
filename = 'pap.txt'
book = open(filename)
lines = book.readlines()
book.close()

for line in lines:
    print(line)
'''


'''
url = 'http://meadoweast.com/csci133/hf.txt'
book = r.urlopen(url)
lines = book.readlines()
book.close()

#for line in lines:
#    print(line)

print(lines[124].decode())
'''

url = 'http://meadoweast.com/csci133/hf.txt'
book = r.urlopen(url)
lines = book.readlines()
book.close()

index = 0
for line in lines:
    line = line.decode()[:-1]
    if '***' in line:
        print(index, line)
    index +=1

finallines=[]
lines = lines[21:11381]
for line in lines:
    line = line.decode()[:-2]
    finallines.append(line)
print(finallines)

    

