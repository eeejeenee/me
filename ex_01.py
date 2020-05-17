while True :

    while True:
        tmp = input("첫번째 수 입력:")

        if tmp.isdigit():
            num = int(tmp)
            break
        else:
            print("정수를 입력해주세요.")

    while True:
        tmp = input("두번째 수 입력:")

        if tmp.isdigit():
            num2 = int(tmp)
            break
        else:
            print("정수를 입력해주세요.")
            

    while True:

        oper = input("연산자를 입력해주세요:")

        if oper == '-' or oper == '+' or oper == '*' or oper == '/' or oper == 'q' or oper == 'Q' :
            break
        else :
            print("+,-,*,/,Q또는 q만 입력 가능 합니다.")
            
    if oper == "Q" or oper == "q":
        print("계산기가 종료되었습니다.")
    elif oper == "-":
        print("%d - %d = %d" % (num, num2, num-num2))
    elif oper == "+":
        print("%d + %d = %d" % (num, num2, num+num2))
    elif oper == "*" :
        print("%d * %d = %d" % (num, num2, num*num2))
    elif oper == "/" :
        print("%d / %d = %d" % (num, num2, num/num2))
    
