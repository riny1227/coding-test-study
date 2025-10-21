# K번째 약수

n, k = map(int, input("두 개의 자연수 N과 K를 입력해주세요: ").split())
arr = []

for i in range(1, n+1) :
    if n % i == 0 :
        arr.append(i)

if len(arr) < k :
    print(0)
else :
    print(arr[k-1])