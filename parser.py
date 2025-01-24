import os

print(f'Дорогой пользователь, пожалуйста пиши все названия директорий папок и т.д без ошибое, т.к из-за этого могут быть ошибки.\n')

what = input('Вы готовы начать работу? (да/нет)? ').lower()

def parsing_manager(target_list):
    for i in range(len(target_list)):
        if key_word in target_list[i]:
            result.append(target_list[i])
def finder(folder):
    if folder != None:
        folder_list.append(folder)
    list = os.listdir(f'{directory}/{folder}')
    parsing_manager(list)

    return list

def main():
    for i in range(amount_promt):
        if amount_promt > 0:
            folder_directory = input('Введите название папки: ')
            try:
                list = finder(folder_directory)
            except:
                pass
        else:
            try:
                list = finder(None)
            except:
                pass

        print(f'Вы выбрали папку {folder_list[i]}, работа с папкой проведена.')
    print(f'Результат работы:\n{result}')

if __name__ == '__main__':
    while what != 'off':
        if what == 'да':
            directory = input('Введите директорию для работы: ')
            key_word = input('Введите ключевое слово, по которому программа будет искать: ')
            amount_promt = int(input('Введите кол-во папок (0 если нет): '))

            folder_list = []
            result = []

            main()
        else:
            raise SystemExit

        what = input('Вы хотите продолжить (да/нет)? ').lower()