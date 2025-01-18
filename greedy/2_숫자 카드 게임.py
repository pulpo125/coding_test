"""
# 그리디
## 숫자 카드 게임
- 96p

1. 숫자가 쓰인 카드들이 N * M 형태로 있다.
    - N = 행의 개수, M = 열의 개수
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
4. 처음 카드를 골라낼 행 선택 시, 이후에 해당 행에 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있는 전략을 세워야 함
"""

# n은 행의 수, m은 열의 수
n, m = map(int, input().split())

# 각 행에서 가장 작은 수들 중에 큰 수를 출력
min_data = []
for col in range(n):
    row = list(map(int, input().split()))
    row_min = min(row)
    min_data.append(row_min)

print(max(min_data))
