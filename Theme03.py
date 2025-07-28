## Theme Search Algorithm
# Sequential Search
from typing import Any, Sequence

def seq_search(a: Sequence, key:Any) -> int:
    i = 0
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

# Sentinel Method (append non-exist data)
from typing import Any, Sequence
import copy

def seq_search2(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i 

# Binary Search
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else: 
            pr = pc - 1
        if pl > pr:
            break
    return -1

## Hashing 
## if) Collision -> chaining or open addressing

#### Chaining
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value:Any, next:Node) -> None:
        self.key = key
        self.value = value
        self.next = next 
        # Self-referencing structure
        # Recur(insertion) != Chain(linking) 
        
class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # Hash Table's capacity
        self.table = [None] * self.capacity # List Array to save hash table
        
    # Hash 값 계산
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    # Hash 값이 같을 경우 : Linked List 이용
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash] # 상위 List
        
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next # hash는 같으나 key가 다를 경우 linked list 따라가기
        return None
    
    # 원소를 추가 
    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
            
        # Adding New Node (named temp)
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    # 원소를 삭제 : 삭제하고싶은 노드의 다음 노드를 Direct로 연결하여 없앰
    # remove는 연결만 끊을 뿐, 메모리를 해제하지는 않음
    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash] # 현재 탐색 중인 노드 (삭제할 노드)
        pp = None # 바로 앞 노드 
        
        while p is not None:
            if p.key == key: # 원하는 노드를 찾았을 경우
                if pp is None: # 삭제하려는 노드가 첫 번째 노드일 경우
                    self.table[hash] = p.next # 다음 노드를 연결해줌으로써 remove
                else: # 첫 번째 노드가 아닐 경우
                    pp.next = p.next  # 해당 자리에 p.next로 연결해서 없애줌
                return True
            pp = p # 이전 노드를 현재 노드로 이동
            p = p.next # 현재 노드를 다음 노드로 이동
        return False
    
    # 해시 테이블의 내용을 통째로 출력
    def dump(self) -> None: 
        for i in range(self.capacity): # 해시 테이블의 크기 == len()
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' ->{p.key} ({p.value})', end='')
                p = p.next
            print()


##### Open Addressing (rehashing)
from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    # 데이터를 실제로 삭제하는게 아닌, status 값만 바꿔줌
    # 메모리는 당장 해제되지는 않음
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료

class Bucket:
    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성
        
    # 새로운 데이터 지정
    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성
        
    # 속성만 바꿈
    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity                 # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 해시 테이블
        
    # Hash 값 구하기
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)% self.capacity)

    # Rehash 값 구하기 ((hash + 1) % capacity)
    def rehash_value(self, key: Any) -> int:
        return(self.hash_value(key) + 1) % self.capacity
    
    # Search Node
    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return None
    
    # Search
    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패

    # Adding
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False             # 이미 등록된 키

        hash = self.hash_value(key)  # 추가하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return False                        # 해시 테이블이 가득 참
    
    # Removing
    def remove(self, key: Any) -> int:
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False           # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True
    
    # Dumping: 내용을 통째로 출력
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')