import random

def guessing_game():
    answer = random.randint(0,100)

    while True:
        input_str = input('輸入')
        
        if input_str.isdigit():
            user_guess = int(input_str)
            
            if user_guess == answer:
                print('yes ',answer)
                break
            elif user_guess>answer:
                print('big')
            else:
                print('small')

        else:
            print('輸入')
            

guessing_game()