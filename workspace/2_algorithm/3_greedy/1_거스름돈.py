"""
# 그리디
## 예제 3-1) 거스름돈
- 87p

n원일 때 거슬러줘야 할 동전의 최소 개수
"""
from src.utils import timer

@timer
def solution(n: int) -> int:
    coin_list = [500, 100, 50, 10]

    cnt = 0
    for coin in coin_list:
        cnt += n // coin
        n %= coin
    
    return cnt

if __name__ == "__main__":
    # n = int(input())
    # print(f"n: {n}")

    # result = solution(n)
    result = solution(1260)
    print(result)
