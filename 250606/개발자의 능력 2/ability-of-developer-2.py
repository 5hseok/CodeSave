import sys

ability = list(map(int, input().split()))

global_min = sys.maxsize

for i in range(len(ability)):
    for j in range(len(ability)):
        if j != i:
            sum1 = ability[i] + ability[j]
            for k in range(len(ability)):
                if k != i and k != j:
                    for p in range(len(ability)):
                        if p != i and p != j  and p != k:
                            sum2 = ability[k] + ability[p]
                            sum3 = sum(ability) - sum2 - sum1
                            global_min = min(global_min, max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

print(global_min)