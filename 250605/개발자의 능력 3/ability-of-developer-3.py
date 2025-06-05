import sys

abilities = list(map(int, input().split()))

def diff_from_x_to_y_and_z(x, y, z):
    global abilities
    sum1 = abilities[x] + abilities[y] + abilities[z]
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

global_min = sys.maxsize

for i in range(len(abilities) - 2):
    for j in range(i+1,len(abilities)-1):
        for k in range(j+1, len(abilities)):
            global_min = min(global_min, diff_from_x_to_y_and_z(i, j, k))
print(global_min)
