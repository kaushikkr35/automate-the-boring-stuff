import logging
logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        logging.debug('i is ' + str(i) + ', total is ' + str(fact))
    logging.debug('End of factorial(%s)' % (n))
    return fact

print(factorial(5))
logging.debug('End of program.')
    
