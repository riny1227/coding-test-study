# 대표값

n = int(input("학생수를 입력해주세요: "))
scores = list(map(int, input("학생들의 수학점수를 각각 입력해주세요: ").split()))

# 학생들의 점수 평균
avg = round(sum(scores) / n)

# 평균과의 차이 계산
diff_list = [abs(score - avg) for score in scores]

# 가장 작은 차이 찾기
min_diff = min(diff_list)

# 평균과 가장 가까운 점수 중 가장 높은 점수 찾기
best_score = max([score for score in scores if abs(score - avg) == min_diff])

# 해당 학생의 번호
student_num = scores.index(best_score) + 1

print(avg, student_num)