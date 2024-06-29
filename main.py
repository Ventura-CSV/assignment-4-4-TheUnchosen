def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    num1 = int(input('enter your number: '))
    numbers.append(num1)
    maxval = num1
    minval = num1

    num2 = int(input('enter your number: '))
    numbers.append(num2)
    if num2 > maxval:
        maxval = num2
    if num2 < minval:
        minval = num2

    num3 = int(input('enter your number: '))
    numbers.append(num3)
    if num2 > maxval:
        maxval = num3
    if num2 < minval:
        minval = num3

    num4 = int(input('enter your number: '))
    numbers.append(num4)
    if num2 > maxval:
        maxval = num4
    if num2 < minval:
        minval = num4

    num5 = int(input('enter your number: '))
    numbers.append(num5)
    if num2 > maxval:
        maxval = num5
    if num2 < minval:
        minval = num5



    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
