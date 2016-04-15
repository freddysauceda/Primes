__author__ = 'asauceda@ucsd.edu,A10482838,jgl021@ucsd.edu,A11380076'
import sys
from sets import Set
import Queue

# List to keep track of seen primes
seen = Set()

def checkPrime(numToCheck):
  # Function checks if a number is a prime
    numToCheck *= 1.0
    if numToCheck%2==0 and numToCheck!=2:
        return False
    for divisor in range(3,int(numToCheck**0.5)+1,2):
        if numToCheck%divisor==0:
            return False
    return True

def hammingDistance(start, end):
    # Function to check the hamming distance of two numbers for the heuristic
    # Returns maxint if unsolvable, hamming distance if otherwise
    if (len(str(start)) != len(str(end))):
        return sys.maxint

    # Variables to keep track of index of string and the distance
    i = 0
    count = 0
    for digit in str(start):
        if digit != str(end)[i]:
            count += 1
        i += 1

    # Return the Hamming Distance
    return count

def getPossibleActions(currentPrime):
  # This method would return the list of prime
  # numbers reachable from the current prime.
  # Note - this should not include the prime numbers
  # which have already been processed, either in the
  # frontier or in the closed list.
    global seen
    listOfPrimes = []

    # Remember to add yourself
    # listOfPrimes.append(currentPrime)

    # Convert currentPrime to string to check primes reachable
    primeString = str(currentPrime)

    # Some dumb logic because I don't know how to start something at 0
    # in python in a for loop
    primeStringIndex = 0

    # Loop through primeString to find reachable primes
    for digit in primeString:

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

        # Increment primeStringIndex to change the right digit
        primeStringIndex += 1

    return listOfPrimes

def getPath(startingPrime,finalPrime):
    global seen

    path = []

    # Create a prio queue for A*
    queue = Queue.PriorityQueue()
    # Put in the starting prime
    queue.put(startingPrime,0)
    # Dicts to keep track of where we are
    parent= {}
    cost_from= {}
    # Remember to add the startingPrime
    parent[startingPrime] = None
    cost_from[startingPrime] = 0

    # Algorithm
    while not queue.empty():
        current = queue.get()
        first = False

        if current == finalPrime:
            break

        for next in getPossibleActions(current):
            new_cost = cost_from[current] + 1
            if next not in cost_from or new_cost < cost_from[next]:
                cost_from[next] = new_cost
                priority = new_cost + hammingDistance(finalPrime, next)
                queue.put(next, priority)
                parent[next] = current

    # Print statements, should match perfectly with what code says
    if int(finalPrime) not in parent:
        sys.stdout.write("UNSOLVABLE")
        return
    else:
        lookUp = finalPrime
        while(parent[lookUp] is not None):
            path.insert(0,lookUp)
            lookUp = parent[lookUp]
        path.insert(0,lookUp)

    sys.stdout.write(" ".join(repr(e) for e in path))
    return



def main():

    primes = str(sys.stdin.readline()).split()
    getPath(int(primes[0]), int(primes[1]))

if __name__ == '__main__':
    main()
