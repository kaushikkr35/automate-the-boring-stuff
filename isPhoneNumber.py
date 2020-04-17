def is_phone_number(num):
    if len(num) != 12:
        return False
    for i in range(0,3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
        return False
    for i in range(4,7):
        if not num[i].isdecimal():
            return False
    if num[7] != '-':
        return False
    for i in range(-1, -4):
        if not num[i].isdecimal():
            return False
    return True

print("Enter the number that you would like to verify: ")
phone_number = input()

if is_phone_number(phone_number) is True:
    print("The number is indeed valid! Hooray!")
else:
    print("The number is not in the correct format :(")
    
