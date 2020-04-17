import random
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(message)s')

logging.debug('Start of program')

guess = ''
logging.debug('Value of guess is %s' % (guess))

while guess not in ('heads', 'tails'):
    logging.debug('Getting the value of guess from the user')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('User guesses the toss to be %s' % (guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('The value of toss as per the random fucntion is %d' % (toss))
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
