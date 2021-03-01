# Programme to check whether the person is eligible for loan or not by checking his credit score and income.
Is_income_high = True
Is_cred_score_good = False
print('---------------and Operator------------')
if Is_income_high and Is_cred_score_good:
    print('Hey!, You are eligible for loan...')
else:
    print('Sorry, You are not eligible for loan...')

print('---------------or Operator------------')
if Is_income_high or Is_cred_score_good:
    print('Hey!, You are eligible for loan...')
else:
    print('Sorry, You are not eligible for loan...')
