def find_average(exam_score):
    return sum(exam_score) / len(exam_score)


score = []
for count in range(10):
    exam_score = int(input("Enter scores: "))
    score.append(exam_score)

print(find_average(score))
