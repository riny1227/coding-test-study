nums = list(map(int, input("정수 리스트를 입력하세요: ").split()))
num_set = set(nums)

def longest_consecutive(num_set):
    longest = 0

    for i in num_set:
        if i - 1 not in num_set:
            length = 1
            while i + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

result = longest_consecutive(num_set)
print(result)