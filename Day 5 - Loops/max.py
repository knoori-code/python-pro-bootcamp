student_scores = [2, 5, 65, 99, 57, 3232, 12, 14, 65252, 4542, 542, 665, 33, 87, 99]

max = 0
for score in student_scores:
    if score > max:
        max = score

print(max)