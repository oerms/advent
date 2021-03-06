#!/usr/bin/env python3

# advent of code, day2
# oerms

def splitline(fileLine):
    """split line from file to appropriate values
    returns list [int first, int second, str letter, str PW]"""
    [firstNum, secondNum, letter,PW] = ((fileLine.replace('-',' ')).replace(':','')).split()
    return [int(firstNum), int(secondNum), letter, PW ]

# function to evaluate database line
def isValidPW(minOccur,maxOccur,letter,PW):
    """evaluate line whether it is a valid password
    input: a split line from the PW file
    Return: 1 if password is valid, 0 else"""
    if PW.count(letter) < minOccur or PW.count(letter) > maxOccur:
        return 0
    else:
        return 1

def isValidPWnew(pos1,pos2,letter,PW):
    """evaluate line whether it is a valid password NEW POLICY
    input: a split line from the PW file
    Return: 1 if password is valid, 0 else"""
    if (PW[pos1-1] == letter) != (PW[pos2-1] == letter):
        return 1
    else:
        return 0

# result variables
[validPWs, validPWsnew] = [0,0]

# file handler
infileH = open("input2","r")
while True:
    try:
        newline = infileH.readline()
        validPWs += isValidPW(*splitline(newline))
        validPWsnew += isValidPWnew(*splitline(newline))
    except:
        # after last line
        infileH.close()
        print("valid PWs old policy: ", validPWs)
        print("valid PWs new policy: ", validPWsnew)
        break

