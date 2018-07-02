def parity(num):
    result = num & 1
    if result == 0:
        return 'Even'
    else:
        return 'Odd'


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Input number (enter '0' for exit): \n"))
            if number == 0:
                print('exit')
                break
            print(parity(number))
        except:
            print('You input not integer number')