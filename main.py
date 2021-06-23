from reminders import Reminders
reminders_list = []

if __name__ == '__main__':
    while True:
        option = input('1. New '
                      '2. delete')
        print(reminders_list)
        if option == '1':
            first = Reminders()
            first.name()
            reminders_list.append(first)
