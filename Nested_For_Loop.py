# -----------------------Nested_Loop-----------------------------
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')
# ----------------------------------------------------
# Programme to print below output format
"""
*****
**
*****
**
**
"""
Numbers = [5, 2, 5, 2, 2]
for x_count in Numbers:
    output_string = ''
    for x in range(x_count):
        output_string += 'x'
    print(output_string)