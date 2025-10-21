# 이중 반복문으로 해결

nums = list(map(int, input("정수 리스트를 입력하세요: ").split()))
target = int(input("목표값을 입력하세요: "))

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
result = two_sum(nums, target)
print(result)