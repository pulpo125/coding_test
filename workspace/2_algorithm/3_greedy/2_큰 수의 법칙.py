"""
# 그리디
## 큰 수의 법칙
- 92p
"""
from src.utils import timer

@timer
def solution(n, m, k, array):
    # 가장 큰 수와 두 번째로 큰 수 찾기
    array.sort(reverse=True)
    first = array[0]
    second = array[1]

    # 가장 큰 수가 연속으로 더해질 수 있는 패턴의 반복 횟수
    first_add_cnt = m // (k + 1) * k
    first_add_cnt += m % (k + 1)

    # 두 번째 큰 수를 더해야 하는 횟수는 남은 횟수
    second_add_cnt = m - first_add_cnt

    return (first * first_add_cnt) + (second * second_add_cnt)



if __name__ == "__main__":
    # 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 가능 횟수 K 입력
    # n, m, k = map(int, input().split())
    # print(f"n, m, k: {n, m, k}")

    # 배열 입력
    # array = list(map(int, input().split()))
    # print(f"array: {array}")

    # 실행
    # result = solution(n, m, k, array)
    # result = solution(5, 8, 3, [2, 4, 5, 4, 6]) # default case
    result = solution(5, 7, 2, [2, 4, 5, 4, 6]) # test case
    print(result)
    print(6+6+5+6+6+5+6)