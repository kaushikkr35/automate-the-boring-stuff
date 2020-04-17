def collatz(number):
    try:
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except ValueError:
        print('Error. You did not type a number')        

print('Type in a number: ')
mynum = int(input())
res = collatz(mynum)
while res!= 1:
    res = collatz(res)
print(res)
