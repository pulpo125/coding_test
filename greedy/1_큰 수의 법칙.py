"""
# 그리디
## 큰 수의 법칙
- 92p

[아이디어]  
가장 큰 수를 연속 가능 횟수 만큼 더하고, 그 다음에 두 번째 큰 수를 한번 더하는 방법을 반복하면 된다.  
가장 큰 수 * 연속 가능 횟수가 더해질 수 있는 만큼은 숫자가 더해지는 횟수에서 연속 가능 횟수를 나눈 몫이며,  
두 번째 큰 수가 더해지는 횟수는 숫자가 더해지는 횟수에서 연속 가능한 횟수를 나눈 나머지 이다.  
때문에, 숫자가 더해지는 횟수를 M, 연속 가능 횟수를 K, 가장 큰 수를 first, 두 번째로 큰 수를 second라고 할 경우 식은 다음과 같다.  
`first * k * (m // k) + second * (m % k)`

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 가능 횟수 K 입력
n, m, k = map(int, input().split())
print(f"n, m, k: {n, m, k}")

# 배열 입력
array = list(map(int, input().split()))
print(f"array: {array}")

# 가장 큰 수와 두 번째로 큰 수 찾기
array.sort(reverse=True)
first = array[0]
second = array[1]

# 가장 큰 수의 연속 가능 횟수만큼 더한 값을 최대로 더할 수 있는 횟수
first_cnt = m // k

# 두 번째 큰 수를 더해야 하는 횟수
second_cnt = m % k

result = (first * k * first_cnt) + (second * second_cnt)
print(result)

"""


def solution(n, m, k, array):
    # 가장 큰 수와 두 번째로 큰 수 찾기
    array.sort(reverse=True)
    first = array[0]
    second = array[1]

    # 가장 큰 수가 연속으로 더해질 수 있는 패턴의 반복 횟수
    first_pattern_cnt = m // k

    # 두 번째 큰 수를 더해야 하는 횟수는 남은 횟수
    second_cnt = m % k

    return (first * k * first_pattern_cnt) + (second * second_cnt)


solution(5, 8, 3, [2, 4, 5, 4, 6])

"""
시간 복잡도:

배열 정렬: 
𝑂(𝑁log𝑁)

가장 큰 수와 두 번째 큰 수 찾기: 
𝑂(1)

최종 결과 계산: 
𝑂(1)

총 시간 복잡도: 
𝑂(𝑁log)
"""
