N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def get_valid_num(x):
    return {(x + i - 1) % N + 1 for i in range(-2, 3)}


comb1 = set((i, j, k) for i in get_valid_num(a1)
                       for j in get_valid_num(b1)
                       for k in get_valid_num(c1))

comb2 = set((i, j, k) for i in get_valid_num(a2)
                       for j in get_valid_num(b2)
                       for k in get_valid_num(c2))

print(len(comb1 | comb2))