"""
7. 이진 탐색
2) 부품 찾기

손님이 요청한 부품이 있는지 확인해 부품이 있으면 yes, 없으면 no를 출력하는 프로그램을 만드시오. 구분은 공백으로 한다.
"""


def binary_search(array: list, target: int, start: int, end: int) -> str:
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"


def solution(n: int, array: list, m: int, target_array: list) -> None:
    array.sort()
    for target in target_array:
        result = binary_search(array, target, 0, n - 1)
        print(result, end=" ")


if __name__ == "__main__":
    n = 5
    array = [8, 3, 7, 9, 2]
    m = 3
    target_array = [5, 7, 9]
    solution(n, array, m, target_array)
