N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def extract_duplication_combination(x, y):
    high_num = max(x,y)
    low_num = min(x,y)

    x_list = set()
    y_list = set()

    for i in range(x-2, x+3):
        if i < 1:
            x_list.add(i + N)
        if i > N:
            x_list.add(i - N)
        else:
            x_list.add(i)

    for i in range(y-2,y+3):
        if i < 1:
            y_list.add(i + N)
        if i > N:
            y_list.add(i - N)
        else:
            y_list.add(i)

    result = []
    for num in range(N):
        if num not in x_list | y_list:
            result.append(num)
    return len(result) if len(result) != 0 else N

print(5**3 * 2 - (extract_duplication_combination(a1, a2) * extract_duplication_combination(b1, b2) * extract_duplication_combination(c1, c2)))