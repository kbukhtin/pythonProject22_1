# Операторы. Переменные. Условия.
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
'''
operand1 = float(input())
operand2 = float(input())
_operator = input()
if _operator == "-":
    print(operand1 - operand2)
elif _operator == "+":
    print(operand1 + operand2)
elif _operator == "*":
    print(operand1 * operand2)
elif _operator == "pow":
    print(operand1 ** operand2)
elif _operator == "/" and operand2 != 0:
    print(operand1 / operand2)
elif _operator == "mod" and operand2 != 0:
    print(operand1 % operand2)
elif _operator == "div" and operand2 != 0:
    print(operand1 // operand2)
elif _operator == "/" or _operator == "mod" or _operator == "div" and operand2 == 0:
    print("Деление на 0!")
'''
# Test №9
'''
_type = input()
p = 3.14
if _type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (1 / 2) * (a + b + c)
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if _type == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
if _type == 'круг':
    r = int(input())
    S = p * (r ** 2)
print(S)
'''
# Test №10
'''
a = int(input())
b = int(input())
c = int(input())
if (a >= b and a >= c) and (b >= c):
    print(a)
    print(c)
    print(b)
elif (a >= b and a >= c) and (c >= b):
    print(a)
    print(b)
    print(c)
elif (b >= a and b >= c) and (a >= c):
    print(b)
    print(c)
    print(a)
elif (b >= a and b >= c) and (c >= a):
    print(b)
    print(a)
    print(c)
elif (c >= a and c >= b) and (b >= a):
    print(c)
    print(a)
    print(b)
elif (c >= a and c >= b) and (a >= b):
    print(c)
    print(b)
    print(a)

ALT:
a,b,c=int(input ()),int(input ()),int(input ())
if a<b: a,b=b,a
if a<c: a,c=c,a
if b<c: c,b=b,c
print (a,c,b,sep='\n')
'''
# Test №11
'''
a = int(input())
b = 'программист'
if a % 10 == 1 and a % 100 != 11:
    с = str(a) + ' ' + b
elif (a % 10 == 2 and a % 100 != 12) or (a % 10 == 3 and a % 100 != 13) or (a % 10 == 4 and a % 100 != 14):
    с = str(a) + ' ' + b + 'а'
else:
    с = str(a) + ' ' + b + 'ов'
print(с)
'''
# Test №12
'''
num = int(input())
a = num // 100000
b = (num // 10000) % 10
c = (num //1000) % 10
d = (num // 100) % 10
e = (num // 10) % 10
f = num % 10
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
'''
#Циклы. Строки. Списки
# Test №12
