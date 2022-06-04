import random
import math

def answer_is_valid(r_border):
    while True:
        num_answer = input(f'Угадай число от 1 до {r_border}:\n')
        if num_answer.isdigit() and 1 <= int(num_answer) <=100:
            int_answer = int(num_answer)
            return int_answer
        else:
            print(random.choice([f'А может быть все-таки введем целое число от 1 до {r_border}?', f'Попробуйте ввести целое число от 1 до {r_border}', 'Что-то не то, повторите ввод', f'Ошибка, нужно ввести число от 1 до {r_border}']))
def border_is_valid():
    while True:
        right_border = input('Какая будет правая граница чисел? \nот 1 до ... ')
        if right_border.isdigit():
            return int(right_border)        
        else:
            print('Это не целое число, попробуй еще.')
def attempts_is_valid(rig_bor):         
    while True:        
        max_attempts = math.ceil(math.log(rig_bor, 2))
        attempts = input(f'Сколько попыток ты себе дашь?\n(максимум допустимо: {max_attempts})\n:')
        if attempts.isdigit() and int(attempts) <= max_attempts:
            return int(attempts)
        else:
            print(f'Это не целое число или оно больше {max_attempts}.')

def main_game():

    int_right_border = border_is_valid()
    int_attempts = attempts_is_valid(int_right_border)
    ran_num = random.randint(1,int_right_border)
    counter = int_attempts
    while True:
        var_num = answer_is_valid(int_right_border)
        counter -= 1
        if var_num == ran_num:
            print('--------------------------------------\n       Поздравляю, вы угадали!!!       \n--------------------------------------')
            break          
        elif counter == 0:
            print(f'Вы проиграли, попытки закончились :(\nЗагаданоое число было: {ran_num}')
            break
        elif var_num < ran_num:
            print(f'Ваше число меньше загаданного, попробуйте еще раз. Попыток осталось: {counter}')
        else:
            print(f'Ваше число больше загаданного, попробуйте еще раз. Попыток осталось: {counter}')

    if input('\nХотите сыграть еще раз, введите "y": ') == 'y':
        print('\n')
        print('--------------------------------------\n Рады снова видеть в числовой угадайке \n--------------------------------------\n\nДавай установим пару правил.')      
        main_game()
    else:
        print('\nСпасибо, что играли в числовую угадайку. Увидимся еще!')

print('--------------------------------------\n Добро пожаловать в числовую угадайку \n--------------------------------------\n\n----- Давай установим пару правил ----')
main_game()
