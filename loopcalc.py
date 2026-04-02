while True:
    print('1. 더하기')
    print('2. 빼기')
    print('3. 곱하기')
    print('4. 나누기')
    print('5. 끝내기')
    choice = input('번호를 고르세요: ')
    if choice == '5':
        print('계산기를 끝냅니다')
        break
    num1 = int(input('첫 번째 숫자: '))
    num2 = int(input('두 번째 숫자: '))
    if choice == '1':
        print('결과:', num1 + num2)
    elif choice == '2':
        print('결과:', num1 - num2)
    elif choice == '3':
        print('결과:', num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print('0으로는 나눌 수 없어요')
        else:
            print('결과:', num1 / num2)
    else:
        print('잘못된 번호예요')
    print('')
