import sys

__author__ = 'asauceda@ucsd.edu,A10482838,jgl021@ucsd.edu,A11380076'

# Dict to keep track of seen primes
seen = {}

def checkPrime(numToCheck):
  # Function checks if a number is a prime
    numToCheck *= 1.0
    if numToCheck%2==0 and numToCheck!=2:
        return False
    for divisor in range(3,int(numToCheck**0.5)+1,2):
        if numToCheck%divisor==0:
            return False
    return True

def getPossibleActions(currentPrime):
  # This method would return the list of prime
  # numbers reachable from the current prime.
  # Note - this should not include the prime numbers
  # which have already been processed, either in the
  # frontier or in the closed list.
    global seen
    listOfPrimes = []

    # Remember to add yourself
    listOfPrimes.append(currentPrime)

    # Convert currentPrime to string to check primes reachable
    primeString = str(currentPrime)

    # Some dumb logic because I don't know how to start something at 0
    # in python in a for loop
    firstRun = True
    primeStringIndex = 0

    # Loop through primeString to find reachable primes
    for digit in primeString:

        if(firstRun!=True):
            primeStringIndex += 1

        # save digit to check later
        save_i = int(digit)

        # cast to int to add, logic only works if we add
        # mod to keep between 0-9
        digit_i = (save_i+1)%10

        # loop through while digit is not the same as it was before
        while(digit_i!=save_i):

            # Get rid of leading zeroes, using a continue statement like a noob
            if(primeStringIndex == 0 and digit_i == 0):
                digit_i = (digit_i+1)%10
                continue

            # Strings are immutable in python apparently, convert to list
            primeStringList = list(primeString)
            # Change the digit of the number according to the index
            primeStringList[primeStringIndex] = str(digit_i)

            # Check if the new number is prime, add to list if not already in
            if(checkPrime(int(''.join(primeStringList)))):
                if not int(''.join(primeStringList)) in listOfPrimes:
                    listOfPrimes.append(int(''.join(primeStringList)))

            # Increment digit correctly
            digit_i = (digit_i+1)%10

    return listOfPrimes

def getPath(startingPrime,finalPrime):
    # check if the number of digits are the same, can't find a path if they're not
    if(len(str(startingPrime)) != len(str(finalPrime))):
        return "UNSOLVABLE"

    global seen
    return path

def main():

    print(getPossibleActions(11))

    #primes = str(sys.stdin.readline()).split()
    #print(getPath(primes[0],primes[1]))

if __name__ == '__main__':
    main()
