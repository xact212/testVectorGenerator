import sys
import random as rand

#open template file using 
TEMP_FILE_PATH = sys.argv[1]
tempFileH = open(TEMP_FILE_PATH, "r")

#try opening custom output function 
CUST_OUT_DEFINED = True

def custOutputFunc(inputStr, NUM_OUTPUTS, NUM_INPUTS):
    print("curr line before: ", inputStr)
    Alist = []
    Blist = []
    print("A end: ", int((NUM_INPUTS / 2) * 3))
    print("B end: ", int((NUM_INPUTS) * 3))

    for i in range(int((NUM_INPUTS / 2) * 3)):
        if inputStr[i] == "1":
            Alist.append(1)
        elif inputStr[i] == "0":
            Alist.append(0)

    for i in range(int((NUM_INPUTS / 2) * 3), int((NUM_INPUTS) * 3)):
        if inputStr[i] == "1":
            Blist.append(1)
        elif inputStr[i] == "0":
            Blist.append(0)
    print(Alist)
    print(Blist)
    inpSum = []
    carry = 0
    #go through each pair of values, add them together
    for i in reversed(range(0, len(Alist))):
        currSum = Alist[i] + Blist[i] + carry
        carry = 0
        if currSum > 1:
            carry = 1
            if currSum == 2:
                inpSum.append(0)
            elif currSum == 3:
                inpSum.append(1)
            elif currSum == 4:
                inpSum.append(0)
                carry = 2
            currSum = 0
            continue
        inpSum.append(currSum)
        currSum = 0
    inpSum.reverse()
    print(inpSum)
    #add sum to output string
    outStr = inputStr
    for val in inpSum:
        outStr += str(val) + "  "
    return outStr

print("found cust output module: ", CUST_OUT_DEFINED)
NUM_INPUTS = int(sys.argv[2])
NUM_TESTS = int(sys.argv[3])

#weights determine how likely each bit is to be a one or zero
#weight = 1, 1 100% of time, = 0, 0 100% of time 

#generate number of randomly generated tests given by the command line
#check for probability weights in template file
tempText = tempFileH.read()
weights = []
if "weights" in tempText: #if there are custom weights, read them in
    while char in tempText != "\n":
        weights.append(float(char))
else: #if not, assume 50/50 chance for each bit
    prob = 0.5
    weights = [prob] * NUM_INPUTS

#generate tests
tempFileH = open(TEMP_FILE_PATH, "a")
for i in range(NUM_TESTS):
    resStr = ""
    for j in range(NUM_INPUTS):
        randNum = rand.random()
        if randNum >= weights[j]:
            resStr += "1  "
        else:
            resStr += "0  "
    if CUST_OUT_DEFINED:
        resStr = custOutputFunc(resStr, 8, NUM_INPUTS)
    resStr += "\n"
    tempFileH.write(resStr)


