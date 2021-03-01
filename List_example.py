# Write a programme to remove the duplicates in a list
Numbers = [2, 3, 2, 3, 7, 9, 10, 22, 88]
# ------------------------------------------------------
unique = []
for number in Numbers:
    if number not in unique:
        unique.append(number)
print(unique)
