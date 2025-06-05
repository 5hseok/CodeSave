N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def extract_duplication_combination(x, y):
    high_num = max(x,y)
    low_num = min(x,y)

    x_list = []
    y_list = []

    x_list.append(i for i in range(x-2,x+3))
    y_list.append(i for i in range(y-2,y+3))

    result = []
    for x in x_list:
        if x in y_list:
            result.append(x)
    return len(result) if len(result) != 0 else N - 9

print(5**3 * 2 - (extract_duplication_combination(a1, a2) * extract_duplication_combination(b1, b2) * extract_duplication_combination(c1, c2)))