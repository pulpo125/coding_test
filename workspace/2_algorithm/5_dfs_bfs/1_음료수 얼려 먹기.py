"""
# DFS/BFS
# 3) 음료수 얼려 먹기

n * m 얼음 틀이 있다.
0은 구멍, 1은 칸막이 부분이다.
구멍끼리 붙어있는 경우에는 서로 붙어있는 것이다.
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

아이디어)
1. 0 이면 상하좌우에 0이 있는지 체크
2. 상하좌우 중 0이 있으면 그 위치에서 또 상하좌우에 0이 있는지 체크
- 0 을 찾으면 1로 바꾸고 상하좌우에 0이 있는지 다 체크해서 1로 바꿔버리고 결국 카운트는 1만 플러스 함.

코멘트)
- 상하좌우 체크하는 로직과 dfs 가 필요하다는 것을 떠올렸으나 카운트 하는 시점(True, False)이 헷갈려서 결국 답지 확인 후 해답을 찾음.
"""
from src.utils import timer

def dfs(x, y):
    print(graph)
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y) # 상
        dfs(x-1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

@timer
def solution(n, m, graph) -> int:
    # n, m = map(int, input().split())

    # graph = []
    # for _ in range(n):
        # graph.append(input().split())

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                print(i, j)
                cnt += 1
    
    return cnt


if __name__ == "__main__":
    # n, m = map(int, input().split())
    # n, m = 4, 5
    # graph = [
    #     [0, 0, 1, 1, 0],
    #     [0, 0, 0, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [0, 0, 0, 0, 0],
    # ]
    n, m = 3, 3
    graph = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    print(solution(n, m, graph))