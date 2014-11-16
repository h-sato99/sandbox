#coding:utf-8

f = open('file/sample.txt')
data = f.read()
f.close()

lines = data.split()
array = []
result = 0

for line in lines:
    result = result + len([x for x in array if x > line])
    array.append(line)

print str(result)

