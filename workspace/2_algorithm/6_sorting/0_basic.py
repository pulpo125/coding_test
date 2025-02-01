"""
1. 선택 정렬
- 선택 정렬은 첫 번째 원소를 가장 작은 수와 바꾸고, 두 번째 원소를 두 번째 작은 수와 바꿔나가는 정렬 방법이다.
- 총 N-1 번의 연산을 한다.
- 시간 복잡도는 O(N2) 이다.
"""

def selection_sort(array: list) -> list:
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    return array

"""
2. 삽입 정렬
- 삽입 정렬은 두 번째 원소(인덱스 1) 부터 왼쪽은 정렬되었다는 가정하에 왼쪽 리스트에 올바른 위치에 삽입을 해서 점차 정렬해나가는 정렬 방법이다.
- 왼쪽 리스트에서 더 작은 원소를 만나면 그 자리에 삽입 되면 된다. 
- 시간 복잡도는 O(N2)으로 선택 정렬과 같지만, 이미 어느정도 정렬이 된 리스트에서는 퀵 정렬보다 빠른 속도이다.
"""

def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    selection_sorted_array = selection_sort(array)
    print(f"선택 정렬 결과: {selection_sorted_array}")

    insertion_sorted_array = insertion_sort(array)
    print(f"삽입 정렬 결과: {insertion_sorted_array}")

