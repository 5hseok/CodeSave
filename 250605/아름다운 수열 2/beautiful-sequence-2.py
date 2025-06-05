from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

b_count = Counter(B)
global_cnt = 0

for i in range(N - M + 1):
    tmp_cnt = Counter(A[i:i+M])
    if tmp_cnt == b_count:
        global_cnt += 1

print(global_cnt)