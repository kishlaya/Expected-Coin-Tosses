import toss
import random

nTrials = 10000
nLength = 6

def simulate():
    randPattern = ''.join([random.choice('HT') for _ in range(nLength)])
    # print(randPattern)
    count = 0
    for _ in range(nTrials):
        innerCounter = 0
        soFar = ""
        while soFar[-nLength:] != randPattern:
            soFar = (soFar + random.choice('HT'))[-nLength:]
            innerCounter += 1
            # print(soFar)
        count += innerCounter
        # print("success")
    average = count/nTrials
    expectation = toss.markovChain(randPattern)
    print("Pattern:", randPattern)
    print("Simulated Average:", average)
    print("Calculated Expectation:", expectation)

if __name__ == "__main__":
    simulate()
