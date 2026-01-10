# 정다면체

n, m = map(int, input("n, m을 입력해주세요.(자연수 4, 6, 8, 12, 20 중의 하나): ").split())

# 딕셔너리 사용
count = {}

for i in range(1, n + 1):   # 정n면체 주사위
    for j in range(1, m + 1):   #정m면체 주사위
        s = i + j   # 두 눈의 합 계산
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

max_count = max(count.values())

for s in sorted(count.keys()):
    if count[s] == max_count:
        print(s, end=' ')