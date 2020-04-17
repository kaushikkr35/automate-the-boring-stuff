while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a numeric value for your age')

while True:
    print('Select a new password (letters & numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Please enter a password containing letters & numbers only')
