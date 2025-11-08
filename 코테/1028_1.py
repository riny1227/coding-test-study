#K번째 큰 수
from itertools import combinations

n, k = map(int, input("자연수를 입력하세요(3<=n<=100, 1<=k<=50): ").split())
l = list(map(int, input("1부터 100까지의 자연수를 입력해주세요: (n개의 카드값을 각각 입력해주세요.)").split()))

# 숫자 3개를 더한 조합의 합
comb_sum = set()

for c in combinations(l, 3):
    comb_sum.add(sum(c))

result = list(comb_sum)
result.sort(reverse=True)

print(result[k-1])