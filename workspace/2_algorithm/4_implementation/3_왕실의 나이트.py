"""
# 구현
## 2) 왕실의 나이트
- 115p

문제: 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 구해라.
조건:
8*8 체스판 한 칸에 나이트가 있다.
나이트는 L자 형태로만 이동할 수 있으며 체스판을 벗어날 수 없다.
1. 수평 2칸 이동 후 수직 1칸
2. 수직 2칸 이동 후 수형 1칸

"""
from src.utils import timer

@timer
def solution(knight: str) -> int:
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    knight_col_idx, knight_row_idx = cols.index(knight[0]), rows.index(int(knight[1]))
    knight_position = (knight_col_idx, knight_row_idx)

    move_types = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    cnt = 0
    for mt in move_types:
        new_position = tuple(sum(e) for e in zip(knight_position, mt))
        if new_position[0] >= 0 and new_position[0] <= 7 and new_position[1] >= 0 and new_position[1] <= 7:
            cnt += 1
    
    return cnt




if __name__ == "__main__":
    # knight = input()
    # result = solution(knight)
    # result = solution("a1")
    result = solution("c2")
    print(result)