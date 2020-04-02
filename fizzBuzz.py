def isPrime(n):
    divisable = []
    for i in range(1, n+1):
        if n%i == 0:
            divisable.append(i)
    if len(divisable) == 2:
        return True
    return False

def fizzBuzz(n):
    for i in range(1,n+1):
        if isPrime(i):
            print('Prime')
        else:
            if i%3 == 0 and i%5 == 0:
                print('FizzBuzz')
            elif i%3 == 0:
                print('Fizz')
            elif i%5 == 0:
                print('Buzz')
            print(i)

fizzBuzz(100)
