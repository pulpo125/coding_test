"""
# 구현
## 3) 게임 개발

n * m 공간이 있다.
1. 현재 위치에서 현재 방향 기준으로 왼쪽 방향 부터 갈 곳을 정함
2. 왼쪽 방향에 안 가본 칸이 있다면 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진 / 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
3. 네 방향 모두 가본 칸이거나 바다인 경우는 현 방향을 유지한 채 한 칸 뒤로가고 1단계로 돌아감. 단, 뒤쪽이 바다인 경우 움직임을 멈춤
문제: 캐릭터가 방문한 칸의 수를 출력해라
입력조건:
    - 첫째 줄에 n*m 을 공백으로 구분하여 입력
    - 둘째 줄에 캐릭터의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어짐 (0: 북, 1: 동, 2: 남, 3: 서)
    - 셋째 줄에 맵이 육지인지 바다인지에 대한 정보가 주어짐. N개 줄에 북쪽부터 남쪽 순서대로 주어지고,
      각 줄의 데이터는 서->동 순서대로 주어진다. 맵의 외곽은 항상 바다임 (0: 육지, 1: 바다)
    - 캐릭터의 처음위치는 항상 육지이다.
예시:
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
from src.utils import timer

@timer
def solution(n, m, a, b, d, map_array) -> int:
    # 입력
    # n, m = map(int, input().split())
    # a, b, d = map(int, input().split())
    # map_array = []
    # for i in range(n):
    #     map_array.append(map(int, input().split()))

    # 가본 곳을 저장하는 히스토리 배열 생성
    history_array = [[0] * m for _ in range(n)]
    history_array[a][b] = 1

    # 북, 동, 남, 서
    xy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    cnt = 1 # 처음 있는 곳도 가본 곳이므로 1이다.
    turn = 0
    while True:
        # 왼쪽으로 회전
        d -= 1
        if d == -1:
            d = 3
        turn += 1

        # 안가본 칸이면서 육지면 한 칸 이동
        na, nb = a + xy[d][0], b + xy[d][1]
        if history_array[na][nb] == 0 and map_array[na][nb] == 0:
            a, b = na, nb
            cnt += 1
            turn = 0 # turn init
            continue
        else:
            # 가본 칸이면서 바다인 경우 회전한 방향 유지

            # 모든 방향 가본 칸인 경우
            if turn == 4:
                # 한 칸 뒤가 육지면 뒤로 가기
                na, nb = a - xy[d], b - xy[d]
                if map_array[na][nb] == 0:
                    a, b = na, nb
                else:
                    # 한 칸 뒤가 바다라면 종료
                    break
        print(cnt)
    
    return cnt




if __name__ == "__main__":
    # n, m = map(int, input().split())
    # a, b, d = map(int, input().split())
    # map_array = []
    # for i in range(n):
    #     map_array.append(map(int, input().split()))
    n, m = 4, 4
    a, b, d = 1, 1, 0
    map_array = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

    result = solution(n, m, a, b, d, map_array)
    print(result)