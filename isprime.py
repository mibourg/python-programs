def isPrime(number):
    quotients = []
    if number > 1:
        for x in range(2, number-1):
            quotients.append(number % x)
        if int > 0 in quotients:
            return False
        else: 
            return True
    else:
        return True

print isPrime(81)