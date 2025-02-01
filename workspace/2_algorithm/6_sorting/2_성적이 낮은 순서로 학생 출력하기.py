"""
6. 정렬
3) 성적이 낮은 순서로 학생 출력하기

N명의 학생 정보가 있다.
학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생으 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

입력)
- 첫째 줄: 학생의 수 N (1<=N,+100,000)
- 둘째 줄-N+1 줄: 학생 이름 문자열 A와 학생 성적 정수 B가 공백으로 구분되어 입력(len(A), b <= 100)

출력)
- 모든 학생의 이름을 성적이 낮은 순대로 출력
- 성적이 동일한 경우 자유

lambda 매개변수 : 결과
"""

def solution(n: int, array: list) -> None:
    # 입력
    # n = int(input())
    # array = []
    # for _ in range(n):
    #     data = list(input().split())
    #     array.append([data[0], int(data[1])]) # [[이름, 점수], ...]

    # 성적을 기준으로 오름차순
    sorted_array = sorted(array, key = lambda x : x[1])

    # 출력
    for x in sorted_array:
        print(x[0], end=" ")


if __name__ == "__main__":
    n = 2
    array = [["홍길동", 95], ["이순신", 77]]
    solution(n, array)