N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

diff_from_H_to_Arr = []

for num in arr:
    diff_from_H_to_Arr.append(abs(H-num))

print(sum(sorted(diff_from_H_to_Arr)[:T]))