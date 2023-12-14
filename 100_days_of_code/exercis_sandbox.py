import random

hieght = [151,145,179]

for n in range(0, len(hieght)):
    hieght[n] = int(hieght[n])
    total_hieght = sum(hieght)

total_students = 0

for student in hieght:
    total_students += 1

average = round(total_hieght/total_students)

print(f"Number of students = {total_students}")
print(f"Total hieght of all student combined = {total_hieght}")
print(f"The average hieght is {average}")