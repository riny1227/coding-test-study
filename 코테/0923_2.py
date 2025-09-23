num = list(map(int, input().split()))
rm = int(input("지우고 싶은 값: "))

while rm in num:
    num.remove(rm)

print(num)