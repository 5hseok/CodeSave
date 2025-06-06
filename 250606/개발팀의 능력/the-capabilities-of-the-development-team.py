import sys

arr = list(map(int, input().split()))
global_min = sys.maxsize

for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            sum1 = arr[i] + arr[j]
            for k in range(len(arr)):
                if k != i and k != j:
                    for p in range(len(arr)):
                        if p != k and p != i and p != j:
                            sum2 = arr[p] + arr[k]
                            sum3 = sum(arr) - sum1 - sum2
                            diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
                            if sum1 != sum2 and sum1 != sum3 and sum2 != sum3:
                                global_min = min(global_min, diff)
if global_min != sys.maxsize:
    print(global_min)
else:
    print(-1)