n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

global_max = 0

main_dict = {}

for i in range(n):
    main_dict[pos[i]] = alpha[i]

sorted_keys = sorted(main_dict.keys())

new_pos = []
new_alpha = []
for i in range(n):
    new_pos.append(sorted_keys[i])
    new_alpha.append(main_dict[sorted_keys[i]])

print(new_pos)
print(new_alpha)

for i in range(n):
    for j in range(i, n):
        if new_alpha[i:j+1].count('G') == 0 or new_alpha[i:j+1].count('H') == 0 or new_alpha[i:j+1].count('G') == new_alpha[i:j+1].count('H'):
            global_max = max(global_max, max(new_pos[i:j+1]) - min(new_pos[i:j+1]))

print(global_max)