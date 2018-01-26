"""
YAHOO - 電子商務工程師面試參考題

1. 給你任意位數，將位數拆開後相加，請用遞迴

例：
    給 1367 ，答案為 1+3+6+7 = 17
"""

def getPointSum(number, sumAnswer = 0):
    point = number % 10
    sumAnswer += point
    nextNumber = int(number / 10)
    if (nextNumber == 0) :
        print (sumAnswer)
        exit()
    getPointSum(nextNumber, sumAnswer)

"""
2. 給你一個純正整數陣列取出第二大的數字，不能用內建 sort

例：
    [1, 3, 2, 10, 9]
    答案為 9
"""

def getSecondNumber(questionArray):
    firstNumber = 0;
    secondNumber = 0;

    for val in questionArray:
        if (val > firstNumber):
            secondNumber = firstNumber
            firstNumber = val
        if (val < firstNumber and val > secondNumber):
            secondNumber = val

    print(secondNumber)

getPointSum(1376)