"""
# DFS/BFS
# 4) 미로탈출

n * m 크기의 미로가 있다.
- 동빈이 위치: (1, 1)
- 출구 위치: (N, M)
- 한 번에 한 칸 이동
- 괴물 있으면 0, 없으면 1
- 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수

입력)
첫째 줄: n, m
n개 줄: 각각 m 개의 정수로 미로 맵 
- 시작과 마지막 칸은 무조건 1
"""
from src.utils import timer
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 상하좌우
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while queue:
        # 큐에서 하나의 좌표를 뽑는다
        x, y = queue.popleft()
        
        for i in range(4): # 모든 방향 확인
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            
            # 미로를 벗어나는 지 확인
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            
            # 0 인지 확인
            if graph[nx][ny] == 0:
                continue

            # 1인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


@timer
def solution(n, m, graph) -> int:
    # n, m = map(int, input().split())

    # graph = []
    # for _ in range(n):
        # graph.append(input().split())

    result = bfs(0, 0)
    
    return result


if __name__ == "__main__":
    # n, m = map(int, input().split())

    # graph = []
    # for _ in range(n):
        # graph.append(input().split())
    
    n, m = 3, 3
    graph = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1],
    ]
    result = solution(n, m, graph)
    print(f"정답: {result}")