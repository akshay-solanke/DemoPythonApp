# names = ['Akshay', 'Nikhil', 'ketan', 'Chetan', 'Kiran']
# print(names[0])
# print(names[2:])
# print(names[2:4])
# print(names[-4:-2])
# print(names[-2])
# Write a programme to find the largest number in the list
List = [199, 122, 5, 23, 45, 76, 89, 22, 45, 90]
Largest_number = 0
for number in List:
    if Largest_number < number:
        Largest_number = number
print("Largest Number:", Largest_number)
