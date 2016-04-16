import sys
from sets import Set
import Queue

__author__ = 'asauceda@ucsd.edu,A10482838,jgl021@ucsd.edu,A11380076'

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

    # Dict to keep track of parent
    # key : val = node : parent
    parent = {}
    path = []

    # Create the queue for bfs
    q = Queue.Queue()
    # Insert the first prime to search from
    q.put(startingPrime)
    seen.add(int(startingPrime))
    parent[int(startingPrime)] = None

    flag = False

    while (q.empty() == False):
        # For each adjacent prime do the bfs stuff
        q_front = q.get()

        # For each adjacent neighbor
        for neighbor in getPossibleActions(q_front):
            # If this not hasn't been seen
            if int(neighbor) not in seen:
                q.put(neighbor)
                seen.add(neighbor)
                parent[int(neighbor)] = int(q_front)

                if(neighbor == finalPrime):
                    flag = True
                    break

        if flag:
            break

    # If the finalPrime isn't in the parent dict then it's unsolvable
    # Can't use print to print because python likes to add stupid newlines at the end of things
    if int(finalPrime) not in parent:
        sys.stdout.write("UNSOLVABLE")
        return
    else:
    # Assign lookUp to finalPrime, loop backwards until we reach the root which
    # has to be the startingPrime
        lookUp = finalPrime
        while(parent[lookUp] is not None):
            path.insert(0, lookUp)
            lookUp = parent[lookUp]
        path.insert(0, lookUp)

    # Print the final list to stdout
    sys.stdout.write(" ".join(repr(e) for e in path))
    return


def main():

    for line in sys.stdin.readlines():
        primes = str(line).split()
        getPath(int(primes[0]), int(primes[1]))
        print ""

if __name__ == '__main__':
    main()
