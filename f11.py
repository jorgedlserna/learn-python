# The logging module lets you display logging messages
import logging

# Basic configuration for logging module
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling loggings messages
logging.disable(logging.CRITICAL)

logging.debug('Start of the program')

def boxPrint(symbol,width,height):
    if len(symbol) != 1:

        # Raising an exception in case of error
        raise Exception('"symbol" needs to  be 1 character long.')
    
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than or equal to 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width)

boxPrint('*',10,5)

market_2nd={'ns':'green','ew':'red'}

def switchingLights(instersection):
    for key in instersection.keys():
        if instersection[key]=='green':
            instersection[key]='yellow'
        elif instersection[key]=='yellow':
            instersection[key]='red'
        elif instersection[key]=='red':
            instersection[key]='green'

    # Raising an assertion to detect programmer erros
    assert 'red' in instersection.values(), 'Neither light is red!'+ str(instersection)
    # return instersection

switchingLights(market_2nd)
print(market_2nd)

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))

    total=1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of the program')

