def continueOrNo():
    while True:
        continue_Or_NO = input("Do you want to do this one more? (Yes or No): ").strip().lower()
        if continue_Or_NO == 'yes':
            return True  # 다시 실행
        elif continue_Or_NO == 'no':
            return False # 종료
        else:
            print('Please type a valid word(yes or no).')