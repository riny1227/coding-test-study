num = int(input("리스트의 개수를 입력하세요: "))
 
arr = [0]*num
sum = []

for i in range (num):
    arr[i] = list(map(int, input("리스트 요소를 입력하세요: ").split()))
    sum += arr[i]

print(sum)