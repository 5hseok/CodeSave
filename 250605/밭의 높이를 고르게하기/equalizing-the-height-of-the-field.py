import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

diff_from_H_to_dict = {}

for i in range(N):
    diff_from_H_to_dict[i] = abs(H - arr[i])

global_sum = sys.maxsize

for i in range(N - T + 1):
    local_sum = 0
    for j in range(i, i + T):
        local_sum += diff_from_H_to_dict.get(j, 0)
    global_sum = min(local_sum, global_sum)

print(global_sum)