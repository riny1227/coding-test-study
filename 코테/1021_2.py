#K번째 수
t = int(input("테스트 케이스를 입력하세요(1<=T<=10): "))

for i in range(t):
    n, s, e, k = map(int, input("자연수(5<=N<=500)를 입력하세요: ").split())
    my_list = list(map(int, input("숫자를 입력하세요: ").split()))

    ml = my_list[s-1:e]
    ml.sort()

    print(ml[k-1])