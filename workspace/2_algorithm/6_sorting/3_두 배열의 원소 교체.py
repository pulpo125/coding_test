"""
6. 정렬
4) 두 배열의 원소 교체

동빈이는 두 개의 배열 A, B를 가지고 있다.
두 배열은 N개의 원소로 구성되어 있다. (배열 원소는 자연수)
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있다.
바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 바꾸는 것이다.
N, K, 배열 A, B 가 있을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력하는 프로그램을 작성해라.

입력)
- 첫 번째 줄: N, K 가 공백으로 구분되어 입력 (1<=N<=100,000,0, 0<=K<=N)
- 두 번쨰 줄: A의 원소가 공백으로 구분되어 입력 (원소 < 10,000,000)
- 세 번째 줄: B의 원소가 공백으로 구분되어 입력 (원소 < 10,000,000)
"""

def solution(n: int, k: int, a: list, b: list) -> None:
    # 입력
    # n, k = map(int, input())
    # a = list(input().split())
    # b = list(input().split())

    # 정렬
    a.sort()
    b.sort(reverse=True)

    # 바꿔치기
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break 
    
    print(a)

    # 배열 A의 모든 원소의 합의 최댓값 출력
    print(sum(a))

    return None


if __name__ == "__main__":
    n, k = 5, 3
    a = [1, 2, 5, 4, 3]
    b = [5, 5, 6, 6, 5]
    solution(n, k, a, b)