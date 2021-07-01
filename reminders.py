from query_user import QueryUser
from one_reminder import Reminder

class Reminders:
    def __init__(self):
        self.list_of_reminders = []

    def execute(self):
        user = QueryUser()
        user.display_menu()
        awnser = user.get_input()
        print(awnser)
        if awnser == '1':
            name = user.get_name()
            entry = Reminder()
            entry.name(name)
            print(entry.name)
            option = user.ext_options()
            option = int(option)
            awnser = user.get_option_awnser(option)
            print(awnser)
            entry.set_atribute(option, awnser)
            print(f'date {entry.date}')
            self.list_of_reminders[1] = awnser
            print(self.list_of_reminders)
        elif awnser == '2':
            input('Name of reminder')

if __name__ == '__main__':
    reminders = Reminders()
    reminders.execute()
