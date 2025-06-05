import bisect

N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

main_dict = {}

for i in range(N):
    if main_dict.get(pos[i], 0) != 0:
        main_dict[pos[i]] += candy[i]
    else:
        main_dict[pos[i]] = candy[i]

sorted_keys = sorted(main_dict.keys())
global_max = 0

for i in range(sorted_keys[0], sorted_keys[-1] - K):
    local_sum = 0
    for j in range(i, i+2*K+1):
        if main_dict.get(j, 0) != 0:
            local_sum += main_dict[j]
        
    global_max = max(global_max, local_sum)

print(global_max)