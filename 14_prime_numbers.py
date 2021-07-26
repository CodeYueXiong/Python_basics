# Write a program to generate a list of all prime numbers less than 20
class PrimeNumbers:
    """a class which returns the corresponding prime numbers less than 20"""

    def __init__(self, range):
        self.range = range

    def prime_detect(self):
        primeList = []
        for possiblePrime in range(2, self.range + 1):
            PrimeFlag = True
            for num in range(2, possiblePrime):  # int(possiblePrime**0.5)
                if possiblePrime % num == 0:
                    PrimeFlag = False
            if PrimeFlag:
                primeList.append(possiblePrime)
        return primeList


primeSolution = PrimeNumbers(range=20)
print(primeSolution.prime_detect())
