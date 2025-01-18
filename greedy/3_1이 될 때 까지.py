"""
# 그리디
## 1이 될 때까지
- 99p
"""

n, k = map(int, input().split())
print(f"n, k: {n, k}")

cnt = 0
while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    cnt += 1

print(cnt)


def answer(n, k):
    cnt = 0
    while n != 1:
        if n % k == 0:
            n = n / k
        else:
            n = n - 1
        cnt += 1
    return cnt


"""
PASS  
시간 복잡도 설명  
나누기 연산(n / k)은 한 번에 숫자를 크게 줄이므로, 주어진 K가 적절히 작동한다면 O(log N)의 효율적인 풀이를 보입니다.  
최악의 경우, K가 N에 적합하지 않을 때 N - 1 연산이 증가하므로 최대 O(N)까지 소요될 수 있습니다.  
"""
