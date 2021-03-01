string = 'HI THERE, "EVERYONE"'
    #     0123456789
print(string)
string1 = string[:]                  # copy string to string1
print(string1)
string2 = string1[0:4]               # concating string from index 0 to 4(except fourth index character)
print(string2)
print(string1.upper())               # converts string1 into upper case
print(string1.lower())               # converts string1 into lower case
print(string1.islower())             # detect string1 is in lower case or not
print(string1.isupper())             # detect string1 is in upper case or not
print(string1.title())               # converts string1 into title format
print(string1.replace('HI','HEY'))   # replaces particular char or group of char
#-------------------------------------
#string = "Hi there, isn't it right?"
#print(string)
#-------------------------------------
#string = '''
#Hey there,
#thank's for coming
#to my place...!
#"Enjoy the Evening."

#Your Friend
#-Akshay
#        '''
#print(string)
#-------------------------------------