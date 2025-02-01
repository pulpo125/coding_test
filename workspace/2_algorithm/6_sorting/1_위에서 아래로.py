"""
6. 정렬
2) 위에서 아래로

수열을 내림차순으로 정렬하는 프로그램을 만드시오.

입력)
- 첫째 줄: 수열에 속해 있는 수의 개수 N(1<=N<=500)
- 둘째 줄 - N+1 번째 줄: 수 (1<=수<=100,000)

출력)
- 정렬 결과를 공백으로 구분하여 출력
"""

def solution(n: int, array: list) -> None:
    # 입력
    # n = int(input())
    # array = []
    # for _ in range(n):
    #     array.append(int(input()))

    array.sort(reverse=True)

    for i in array:
        print(i, end=" ")    


if __name__ == "__main__":
    n = 3
    array = [15, 27, 12]
    solution(n, array)