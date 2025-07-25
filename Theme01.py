### Theme Fundamental Algorithm
## 중앙값 구하기
def med3(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

## ***** 구하기 
n = int(input())
w = int(input())

for i in range(n//w):
    print('*'*w)
rest = n%w
if rest:
    print('*'*rest)

## 직사각형 변의 길이 구하기
s = int(input())

for i in range(1,s+1):
    if i*i > s:
        break
    # 직사각형 넓이가 나누어 떨어지지 않을경우 print 건너뜀
    if s%i: 
        continue 
    print(f'{i} x {s//i}')


## 난수 생성
import random

n = int(input())
for i in range(n):
    r = random.randint(1,100)
    print(r,end=' ')

## 직각 이등변 삼각형
n = int(input())
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

