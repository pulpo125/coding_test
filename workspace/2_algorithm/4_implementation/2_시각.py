"""
# 구현
## 예제 4-2) 시각
- 113p

정수 N이 입력되면 0시0분0초부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성해라.
"""
from src.utils import timer

@timer
def solution(n: int) -> int:
    
    cnt = 0
    # 0시 부터 이므로 n+1 번 진행
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    cnt += 1
    return cnt


if __name__ == "__main__":
    # 입력
    # n = int(input())

    # 실행
    # result = solution(n)
    result = solution(5)
    print(result)
