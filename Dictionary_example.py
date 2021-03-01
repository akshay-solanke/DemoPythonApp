# Write a programme to convert input digit into words

Numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",

}

while True:
    Value = input("Enter any Number To Convert Tnto Text > ")
    if Value == "Quit":
        break
    output = ""
    for bit in Value:
        output += " " + Numbers[bit]
    print(output)
print('Session Ended, Thanks')