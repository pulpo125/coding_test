"""
# 그리디
## 1이 될 때까지
- 99p

n이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행.
1. n-1
2. n / k (나누어 떨어지는 경우에만 수행 가능)
"""
from src.utils import timer

@timer
def solution(n, k):
    cnt = 0
    while True:
        # 나누어 떨어지는 수 만들기
        target_num = (n // k) * k
        cnt += n - target_num
        n = target_num 

        if n < k:
            break
        else:
            # 1이 될때까지 나누기
            cnt += 1
            n //= k
            print(n)
    return cnt

if __name__ == "__main__":
    # 입력
    # n, k = map(int, input().split())
    # print(f"n, k: {n, k}")

    # 실행
    # result = solution(n, k)
    result = solution(25, 3)
    print(result)
