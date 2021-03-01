# Programme to check whether the person is eligible for loan or not by checking his credit score and income.
min_income = 30000
min_cred_score = 700  # _850 is max
income = int(input('Type your monthly income:'))
credit_score = int(input('Type your credit score:'))
if (income > min_income) and (credit_score > min_cred_score):
    print('Hey!, You are eligible for loan...')
else:
    print('Sorry, You are not eligible for loan...')
