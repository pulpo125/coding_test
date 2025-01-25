"""
# 구현
## 예제 4-1) 상하좌우
- 110p

n * n 정사각형 공간에서 가장 왼쪽 위 좌표는 (1,1) 이며 가장 오른쪽 아래 좌표는 (n,n) 이다.
L, R, U, D 중 하나의 문자가 반복적으로 적혀있다. 그 문자대로 움직였을 때 마지막 여행가A의 위치 좌표를 출력하라.
단, n * n 의 공간을 넘어가면 무시된다.
"""
from src.utils import timer

@timer
def solution(n: int, plans: list):
    x, y = 1, 1
    movement_types = ["L", "R", "U", "D"]
    x_movements = [0, 0, -1, 1]
    y_movements = [-1, 1, 0, 0]

    for plan in plans:
        for i in range(len(movement_types)):
            # 이동할 좌표 구하기
            if plan == movement_types[i]:
                a_x, a_y = x + x_movements[i], y + y_movements[i]
        
        # 공간을 넘어가면 이동하지 않음
        if a_x < 1 or a_x > n or a_y < 1 or a_y > n:
            continue
        
        # 이동
        x, y = a_x, a_y

    return x, y


if __name__ == "__main__":
    # 입력
    # n = int(input())
    # plans = input().split()
    # print(f"n, plan: {n, plans}")

    # 실행
    # x, y = solution(n, plans)
    x, y = solution(5, ["R", "R", "R", "U", "D", "D"])
    print(x, y)
