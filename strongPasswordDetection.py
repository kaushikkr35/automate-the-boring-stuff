# Must be 8 characters long
# Contains uppercase & lowercase characters
# At least one digit

import re

# Check if it is atleast 8 characters long
len_regex = re.compile(r'(\S{8,})')

# Upper & Lower case compulsory
low_regex = re.compile(r'[a-z]+')
upp_regex = re.compile(r'[A-Z]+')
dig_regex = re.compile(r'[0-9]+')

print('Enter your password: ')
password = input()

len_test = len_regex.search(password)
low_test = low_regex.search(password)
upp_test = upp_regex.search(password)
dig_test = dig_regex.search(password)

if len_test != None:
    if low_test !=None:
        if upp_test != None:
            if dig_test != None:
                print('Your password is strong enough.')
            else:
                print('Your password needs to contain at least 1 numeric character.')
        else:
            print('Your password must include an uppercase character')
    else:
        print('Your password must include at least 1 lowercase & 1 uppercase character.')
else:
    print('Your password must be at least 8 characters long.')
