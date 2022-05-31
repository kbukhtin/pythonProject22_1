#Task №1
'''
x = int(input())
y = int(input())
print(x * 60 + y)
'''
#Task №2
'''
Y = int(input())
X = Y // 60
y = Y % 60
print(X)
print(y)
'''
#Task №3
'''
x = int(input())
h = int(input())
m = int(input())
hour = (h * 60 + m + x) // 60
minutes = (h * 60 + m + x) % 60
print(hour)
print(minutes)
'''
#Task №4
'''
A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print('Это нормально')
elif A > H:
    print('Недосып')
elif B < H:
    print('Пересып')
'''
#Task №5
'''
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
'''
#Task №6
'''
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p -c)) ** 0.5
print(S)
'''
#Task №7
'''
x = int(input())
if (-15 < x <= 12) or (14 < x < 17) or (19 <= x):
    print('True')
else:
    print('False')
'''
#Task №8