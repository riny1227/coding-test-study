# 딕셔너리 사용해서 해결

nums = list(map(int, input("정수 리스트를 입력하세요: ").split()))
target = int(input("목표값을 입력하세요: "))

def two_sum(nums, target):
    index = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in index:
            return [index[need], i]
        index[num] = i

result = two_sum(nums, target)
print(result)