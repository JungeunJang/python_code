
#return 연습
d = dict(a=1, b=3, c=5)
print(d)
print(type(d))

color = {'apple':'red', 'banana':'yellow'}
print(color)
color['apple']
color['cherry'] = 'red'
print(color)
color['apple'] = 'green'
print(color)

# 예제 4-1-1
score = int(input(('input Score: ')))
if 90 <= score <=100:
    grade = 'A'
elif 80 <= score <= 90:
    grade = 'B'
elif 70 <= score <= 80:
    grade = 'C'
elif 60 <= score <= 70:
    grade = 'D'
else:
    grade = "F"

print("Grade is "+ grade)


#예제 4-4
L = [1,2,3,4,5,6,7,8,9,10]
for i in L:
    if i % 2 == 0:
        continue
    print("Item: {0}".format(i))
else:
    print("Exit ")

import time
l = range(1000)

t =time.mktime(time.localtime())
for i in l:
    print(i,)
t1 = time.mktime(time.localtime())

