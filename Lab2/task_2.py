lesson_number = int(input())

total_minutes = (lesson_number - 1) * 45 + (lesson_number // 2) * 5 + ((lesson_number - 1) // 2) * 15

hours = 9 + total_minutes // 60
minutes = total_minutes % 60

print(hours, minutes)
