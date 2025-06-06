from itertools import permutations

n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# a, b, c 튜플을 b가 많고, b가 같으면 c가 많은 순으로 정렬해서 
# 가장 위에 있는 원소를 기준으로 반복 필터링 

zip_data = list(zip(a,b,c))

zip_data.sort(key=lambda x: (-x[1], -x[2]))

candidates = [''.join(p) for p in permutations('123456789', 3)]

def get_score(candidate, target):
    strike = sum(c1 == c2 for c1, c2 in zip(candidate, str(target)))
    ball = sum((candidate.count(x) > 0) for x in str(target)) - strike
    return strike, ball

# 가장 신뢰도 높은 질문부터 후보를 필터링
for question, strike, ball in zip_data:
    new_candidates = []
    for cand in candidates:
        s, b = get_score(cand, question)
        if s == strike and b == ball:
            new_candidates.append(cand)
    candidates = new_candidates

print(len(candidates))