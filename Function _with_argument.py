import time


def function_one(name, weight, height):
    print('Please wait...')
    print('Calculating.')
    for i in range(3):
        print('.')
        time.sleep(1)
    bmi = weight / ((height * 0.01) * (height * 0.01))
    print(f"""
Hi Mr. {name}
Your BMI is:{int(bmi)}
    """)


# ----------------------------Positional Argument---------------------------


print('Start')
Name_input = input('Enter your Name: ')
Weight_input = int(input('Enter Your Weight in Kg: '))
Height_input = int(input('Enter your Height in cm: '))
function_one(Name_input, Weight_input, Height_input)
# def is used to define any function
# function is always need to define before its call
# while using keyword argument with positional argument , Positional-
# argument must be placed before keyword argument
# ----------------------------Keyword+Positional Argument---------------------------


print('Start')
Name_input = input('Enter your Name: ')
Weight_input = int(input('Enter Your Weight in Kg: '))
Height_input = int(input('Enter your Height in cm: '))
function_one(Name_input, weight=Weight_input, height=Height_input)