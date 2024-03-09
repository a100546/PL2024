import sys
import re

regex = r'(ON)|(OFF)|([\-|\+]*\d+)|(=)'

def sumOnOff(lines):
    canSum = True
    sum = 0

    for line in lines:
        match = re.findall(regex,line,flags=re.I.IGNORECASE)
        for m in match:
            if m[0]:
                canSum = True
            elif m[1]:
                canSum = False
            elif m[2]:
                if canSum:
                    sum += int(m[2])
            elif m[3]:
                print("Sum = " + str(sum))

def main():
    sumOnOff(sys.stdin)

if __name__ == "__main__":
    main()