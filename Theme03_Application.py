### Baekjoon 1654
# Using Binary Search
# mid(answer), left, right => Find the max of mid value
k, n = map(int,input().split())
table =[]
for i in range(k):
    table.append(int(input()))

left = 1
right = max(table) # 자를 수 있는 최대 길이
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in table) # mid 값으로 잘랐을 때 나오는 랜선의 개수
    
    if count >= n: # 조건 만족할 경우 저장
        answer = mid
        left = mid + 1 # left 옮김
    else:
        right = mid - 1 # 불만족 left 내림
print(answer)


### Baekjoon 2805
n,m = map(int, input().split())
table = list(map(int, input().split()))

answer = 0
left = 1
right = max(table)

# Using Binary Search
while left <= right:
    mid = (left + right) // 2
    # 핵심 구문: 나무 길이가 mid 보다 큰 값만 자름
    count = sum((x - mid) for x in table if x >= mid)
    if count >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)


### Baekjoon 2512
n = int(input())
table = list(map(int,input().split()))
m = int(input())

left = 1
right = max(table)
answer = 0

# Using Binary Search
while left <= right:
    mid = (left + right) // 2
    count = sum(min(x,mid) for x in table) 
    if count <= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)


### Baekjoon 2110
n, c = map(int, input().split())
table = []
for i in range(n):
    table.append(int(input()))
table.sort() # 오름차순 정렬

answer = 0
left = 1 # 공유기 사이의 최소 거리
right = table[n-1] - table[0] # 공유기 사이의 최대 거리

# Using Binary Search
while left <= right:
    mid = (left + right) // 2 
    count = 1 # 공유기 설치 개수 (첫 번째 집엔 항상 공유기 설치)
    last = table[0] # 인접한 공유기 거리 계산용 변수

    for i in range(1, n):
        if table[i] - last >= mid:
            count += 1
            last = table[i]
            
    if count >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
