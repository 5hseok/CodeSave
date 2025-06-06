import sys

ability = list(map(int, input().split()))

global_min = sys.maxsize

for i in range(len(ability)):
    for j in range(i+1, len(ability)):
        sum1 = ability[i] + ability[j]
        for k in range(j+1, len(ability)):
            for p in range(k+1, len(ability)):
                sum2 = ability[k] + ability[p]
                sum3 = sum(ability) - sum2 - sum1

    global_min = min(global_min, max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

print(global_min)