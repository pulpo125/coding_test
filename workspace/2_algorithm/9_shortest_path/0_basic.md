# 최단 경로 알고리즘 정리

## 최단 경로란?
최단 경로(Shortest Path)는 그래프에서 가장 짧은 경로를 찾는 알고리즘으로, '길 찾기' 문제라고도 불림. 그래프에서 각 지점은 '노드'로, 지점 간 연결된 도로는 '간선'으로 표현됨. 다양한 상황에 맞는 효율적인 알고리즘이 개발되어 있음.

최단 경로 알고리즘은 크게 두 가지 상황에서 사용됨:
- 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 경우

## 다익스트라(Dijkstra) 최단 경로 알고리즘

### 개념
- 특정 노드에서 출발하여 다른 모든 노드로 가는 각각의 최단 경로를 구하는 알고리즘
- 음의 간선(가중치가 음수인 간선)이 없을 때만 정상 작동
- 그리디 알고리즘으로 분류됨 (매번 '가장 비용이 적은 노드' 선택)
- GPS 소프트웨어의 기본 알고리즘으로 자주 활용됨

### 동작 원리
1. 출발 노드 설정
2. 최단 거리 테이블 초기화 (출발 노드 외 모든 노드까지의 거리를 무한으로 설정)
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3번과 4번 과정 반복

### 구현 방법 1: 간단한 다익스트라 알고리즘
```python
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결된 노드 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 방문 여부 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)
```

#### 시간 복잡도
- O(V²) (V: 노드의 개수)
- 노드가 5,000개 이하인 문제에 적합
- 노드가 10,000개 이상이면 개선된 알고리즘 필요

### 구현 방법 2: 개선된 다익스트라 알고리즘 (우선순위 큐 활용)
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결된 노드 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
```

#### 시간 복잡도
- O(ElogV) (E: 간선의 개수, V: 노드의 개수)
- 노드와 간선의 개수가 많은 문제에 적합
- 우선순위 큐를 활용해 로그 시간으로 가장 짧은 노드 찾기 가능

## 플로이드 워셜(Floyd-Warshall) 알고리즘

### 개념
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
- 다이나믹 프로그래밍 기법을 활용함
- 2차원 리스트에 최단 거리 정보를 저장
- 점화식에 따라 단계적으로 거쳐 가는 노드를 고려하여 테이블 갱신

### 동작 원리
- 각 단계마다 특정 노드를 거쳐 가는 경우를 고려하여 최단 거리 갱신
- n개의 노드에 대해 각각 거쳐가는 경우를 계산 (총 n단계)
- 각 단계에서 O(n²)의 연산 수행

### 플로이드 워셜 알고리즘 구현
```python
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```

#### 시간 복잡도
- O(n³) (n: 노드의 개수)
- 노드의 개수가 적은 문제에 적합 (약 500개 이하)

## 알고리즘 선택 기준
1. **다익스트라 알고리즘**: 
   - 한 지점에서 다른 모든 지점까지의 최단 경로
   - 음의 간선이 없는 경우
   - 노드 수가 많은 경우 개선된 다익스트라(우선순위 큐) 사용

2. **플로이드 워셜 알고리즘**:
   - 모든 지점에서 모든 지점까지의 최단 경로
   - 노드 수가 적은 경우(500개 이하)
   - 구현이 상대적으로 간단하나 시간 복잡도가 높음

## 주요 개념 정리

1. **최단 거리 테이블**: 각 노드까지의 최단 거리를 저장하는 배열
2. **무한(INF)**: 연결되지 않은 노드 간 거리, 보통 매우 큰 값(10억 등)으로 초기화
3. **우선순위 큐**: 가장 비용이 적은 노드를 빠르게 찾기 위한 자료구조
4. **점화식**: 플로이드 워셜에서 `D[a][b] = min(D[a][b], D[a][k] + D[k][b])`

최단 경로 알고리즘은 경로 탐색, 네트워크 라우팅, GPS 네비게이션 등 다양한 실생활 문제에 적용됨. 문제 상황에 맞는 알고리즘을 선택하고 효율적으로 구현하는 능력이 중요함.