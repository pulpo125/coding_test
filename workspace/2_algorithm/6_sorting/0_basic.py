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
- 시간 복잡도는 최악에 경우에는 O(N2)으로 선택 정렬과 같지만, 이미 어느정도 정렬이 된 리스트에서는 O(N)으로 퀵 정렬보다 빠른 속도이다.
"""

def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


"""
3. 퀵 정렬
- 퀵 정렬은 피벗이라는 기준점을 정하고 왼쪽에서 부터 피벗보다 큰 데이터를 찾고, 오른쪽에서 부터는 피벗보다 작은 데이터를 찾아 두 수의 위치를 변경하여,
  결국 피벗 왼쪽에는 피벗보다 작은 수를, 오른쪽에는 피벗보다 큰 수를 위치시켜 계속 퀵 정렬을 해나가는 정렬 방법이다. 
- 만약, 왼쪽에 작은 수가 있고 오른쪽에 큰 수가 있으면 작은 수와 피벗의 위치를 변경시켜 피벗 왼쪽 리스트, 오른쪽 리스트를 각각 퀵 정렬을 다시 수행한다.
- 시간 복잡도는 O(nlogn) 이다.
"""

def tranditional_quick_sort(array: list, start: int, end: int) -> list:

    # 원소가 한 개인 경우 종료
    if start >= end:
        return array
    
    # pivot, left, right
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        
        # pivot 보다 큰 left 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # pivot 보다 작은 right 찾기
        while right > start and array[right] >= array[pivot]:
            right += -1
        
        # 만약 작은 수와 큰 수의 위치가 바뀌었으면 pivot 과 작은 수의 위치를 바꾼다.
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            # 만약 작은 수, 큰 수 위치가 바뀌지 않았다면 두 수를 바꾼다.
            array[left], array[right] = array[right], array[left]
        
        # 재귀로 윈쪽, 오른쪽 리스트 다시 퀵 정렬 시행
        tranditional_quick_sort(array, start, right-1)
        tranditional_quick_sort(array, right+1, end)
    
    return array

def light_quick_sort(array: list) -> list:

    # 만약 리스트 원소가 한개면 종료
    if len(array) <= 1:
        return array
    
    # pivot, 정렬을 수행할 리스트
    pivot = array[0]
    processing_list = array[1:]

    left_list = [i for i in processing_list if pivot >= i]
    right_list = [i for i in processing_list if pivot < i]

    # 왼쪽 오른쪽 리스트에 대해서도 퀵 정렬 수행
    return light_quick_sort(left_list) + [pivot] + light_quick_sort(right_list)


def quick_sort(array: list) -> list:
    # return tranditional_quick_sort(array, 0, len(array)-1)
    return light_quick_sort(array)


"""
4. 계수 정렬
- 계수 정렬은 리스트의 모든 원소들을 카운트 할 수 있는 리스트를 정의해놓고, 카운트 리스트에 정보를 읽어 정렬하는 방법이다.
- 먼저, 최댓값 + 1 크기의 리스트를 0으로 초기화해놓고, 리스트 인덱스에 해당하는 값이 있을때 카운트를 센다.
- 카운트 리스트를 순회하며 각 정보를 읽는다.
- 시간복잡도는 O(N+K) 이다. 하지만, 공간복잡도의 문제가 있기 때문에 1,000,000 개 이하일때만 사용할 수 있다.
"""

def count_sort(array):

    # 카운트 리스트 초기화
    count_list = [0] * (max(array) + 1)

    # 카운트
    for i in range(len(count_list)):
        count_list[i] = array.count(i)
    
    # 카운트 리스트 읽기
    result = []
    for i, k in enumerate(count_list):
        result += [i] * k

    return result
    

if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    selection_sorted_array = selection_sort(array)
    print(f"선택 정렬 결과: {selection_sorted_array}")

    insertion_sorted_array = insertion_sort(array)
    print(f"삽입 정렬 결과: {insertion_sorted_array}")

    quick_sorted_array = quick_sort(array)
    print(f"퀵 정렬 결과: {quick_sorted_array}")

    array_2 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    count_sorted_array = count_sort(array_2)
    print(f"계수 정렬 결과: {count_sorted_array}")

