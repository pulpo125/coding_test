"""
# DFS/BFS
# 3) 음료수 얼려 먹기

n * m 얼음 틀이 있다.
0은 구멍, 1은 칸막이 부분이다.
구멍끼리 붙어있는경우에는 서로 붙어있는 것이다.
총 아이스크림의 개수는?

입력)
1. n, m
2. n+1 줄까지 얼음 틀의 형태가 주어진다.

예제 케이스)
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
from src.utils import timer
from collections import deque

@timer
def solution() -> int:
    n, m = map(int, input().split())
    
    # 인접 행렬 만들기
    graph = []
    for _ in range(n):
        graph.append(input().split())

    # visited 만들기
    visited = [False] * n

    # bfs 
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True

        while queue:
            v = queue.popleft()
            print(v, end = " ")
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # 1.(1,1) 부터 시작해서 인접한 거 찾아서 check(True = 1)
    # 2. 찾는게 끝나면 +1
    # 3. 그 다음 0을 찾아서 1, 2번 수행








if __name__ == "__main__":
    n, m = map(int, input().split())