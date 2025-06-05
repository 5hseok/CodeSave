N = int(input())
a, b, c = map(int, input().split())

def extract_disable_cnt(x):
    local_sum = 0
    if x + 2 < N:
        local_sum += N - (x + 2)
    if x - 2 > 1:
        local_sum += x - 2 - 1
    return local_sum

print(N**3 - (extract_disable_cnt(a) * extract_disable_cnt(b) * extract_disable_cnt(c)))