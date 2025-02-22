# 이진 탐색


## 1. 순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 사용: 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
- 특징: 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 함
- 시간복잡도: 최대 O(N)

```python 
def sequential_search(n, target,array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 이므로 1 더하기)
    
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0]) # 원소의 개수
    target = input_data[1] # 찾고자 하는 문자열

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = input().split()

    # 결과
    print(sequential_search(n, target, array))
```

## 2. 이진 탐색
- 개념: 시작점, 끝점, 중간점, 3개의 변수(index 값이다.)를 사용하여 목표 데이터와 중간점 데이터를 반복적으로 비교해서 데이터를 찾는 방법
- 원리
    1. 시작점, 끝점을 확인 후 중간점을 정한다. (중간점이 실수인 경우 소수점 이하를 버린다.)
    2. 목표 데이터와 중간점의 데이터를 비교한다. 
        a. 중간점 데이터 > 목표 데이터 이면, 끝점을 중간점 이전 인덱스로 옮긴다.
        b. 중간점 데이터 < 목표 데이터 이면, 시작점을 중간점 다음 인덱스로 옮긴다.
    3. 목표 데이터를 찾을 때까지 1, 2를 실행한다.
- 사용: 정렬되어 있어야만 사용 가능
- 특징: 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하여 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다. 코딩 테스트에서 자주 출제되는 개념이므로 암기 필수!
- 시간복잡도: O(logN)

```python
# 구현 방법은 재귀 함수를 이용하거나 반복문을 이용한다.
# 1. 재귀 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, 둥)

n, target = list(map(int, input()).split()) # 원소의 개수 n, 목표값 target 
array = list(map(int, input()).split())

result = binary_search(array, tartget, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 2. 반복문
def binary_search(array, target, start, end):
    while start >= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            return mid + 1
        return None

n, target = list(map(int, input()).split()) # 원소의 개수 n, 목표값 target 
array = list(map(int, input()).split())

result = binary_search(array, tartget, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

## 3. 트리 자료구조
- 데이터베이스는 트리 자료구조로 저장하여 빠른 탐색이 가능하도록 한다.
- 특징
    - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
    - 트리의 최상단 노드를 루트 노드라고 한다.
    - 트리의 최하단 노드를 단말 노드라고 한다.
    - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
    - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

## 4. 이진 탐색 트리
- 원리
    1. 루트 노드(부모 노드)와 목표값을 비교
        a. 부모 노드 < 목표값: 왼쪽 자식 노드 배제
        b. 부모 노드 > 목표값: 오른쪽 자식 노드 배제
- 특징
    - 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
    - 구현은 자료 구조에 가깝고, 문제 출제 빈도는 낮은 편

## 5. 빠르게 입력 받기
- 데이터 개수가 1,000만 개 이상, 탐색 범위 크기가 1,000억 이산인 경우 이진 탐색 알고리즘을 의심해보자.
- 빠르게 입력 받기 위해 sys 라이브러리의 readline() 함수를 이용하자.

```python
import sys

input_data = sys.stdin.readline().rstrip()
```


