try:
    age = int(input('Enter your age: '))
    income = 20000
    risk = income / age
    print(f'Age :{age} and Risk: {int(risk)}')
except ZeroDivisionError:
    print('Age cannot be 0.')  # if someone enters 0 which give us an error in our condition
except ValueError:
    print('Invalid Entry..')  # if Someone enters a string instead of integer
