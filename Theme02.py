## Theme 02 Basic Data Structures and Arrays
# list [], tuple(), dictionary {}
# Scan
def maxof(a):
    maximum = a[0]
    for i in range(1,len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum

t = (4,7,5.6,2,3.14,1)
print(f'{maxof(t)}')
print(max(t))

# List Scan
x = ['Liam', 'Noel', 'Oasis', 'Wonderwall']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
print()

for (i, name) in enumerate(x):
    print(f'x[{i}] = {name}')
    
print()

for (i, name) in enumerate(x,1):
    print(f'{i}번째 = {name}')
    
print()

for i in x:
    print(i)

# Reverse
from typing import MutableSequence
def reverse (a:MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i] # swap simultaniously
        
x = [1,2,3,4,5,6]
reverse(x)
print(x)

x.reverse() 
print(x)

# binary conversion
# 정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환
def bconv(x:int, r:int) -> str: 
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while x > 0:
        d += dchar[x % r]
        x //= r # x = x // r
    return d[::-1]


# (1) Enumerate all prime nunmbers below 1000
counter = 0

for n in range(2,1001):
    for i in range(2,n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)

print(f'나눗셈을 실행한 횟수: {counter}')

# (2) Enumerate all prime nunmbers below 1000
counter = 0 # 나눗셈 횟수 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2 # 2는 소수이므로 초기값으로 지정
ptr += 1 

for n in range(3, 1001, 2): # 홀수만을 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        # 1부터 ptr-1 까지인 이유: prime[0]=2로 짝수는 제외했으므로 계산x
        # prime[ptr] 또한 자기 자신이므로 제외
        counter += 1
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
            break
    else:
        prime[ptr] = n  # 소수로 배열에 등록
        ptr += 1

for i in range(ptr): # ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')


# (3) Enumerate all prime nunmbers below 1000
counter = 0 # 나눗셈 횟수 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2 # 2는 소수이므로 초기값으로 지정
ptr += 1 

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2): # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n: # 제곱 수 보다 커지게 되면 계산할 필요없이 소수로 판별 가능
        counter += 2
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
            break
        i += 1
    else: # 끝까지 나누어 떨어지지 않으면 소수로 등록
        prime[ptr] = n
        ptr += 1
        counter += 1
        
for i in range(ptr): # ptr의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

# m과 n사이 소수 구하기 Baekjoon 1929, 시간복잡도 해결은 C++로...
m = int(input())
n = int(input())

for i in range(m,n+1):
    if i < 2:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

# Deep Copy vs Shallow Copy
x = [[1,2,3],[4,5,6]]
y = x.copy() # Shallow Copy
y[0][1] = 9
print(y)
print(x)

import copy
z = [[1,2,3],[4,5,6]]
w = copy.deepcopy(z)
w[0][1] = 9
print(z)
print(w)
