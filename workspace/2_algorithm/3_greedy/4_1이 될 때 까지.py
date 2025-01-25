"""
# 그리디
## 1이 될 때까지
- 99p
"""
from src.utils import timer

@timer
def answer(n, k):
    cnt = 0
    while n != 1:
        if n % k == 0:
            n = n / k
        else:
            n = n - 1
        cnt += 1
    return cnt

if __name__ == "__main__":
    # 입력
    # n, k = map(int, input().split())
    # print(f"n, k: {n, k}")

    # 실행
    # result = answer(n, k)
    result = answer(25, 5)
    print(result)
