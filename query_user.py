class QueryUser:
    def __init__(self):
        pass

    def display_menu(self):
        print('1. New or 2. delete')
        print('pick a number')

    def get_input(self):
        return input()

    def get_name(self):
        return input('What is the name of the reminder? ')

    def ext_options(self):
        return input('Other Options 1. Date 2. Time 3. Notes 4. Tag 4. Priority 5. Complete 6. Location')

    def get_date(self):
        return input('enter date')


    def get_time(self):
        return input('enter time')

    def get_notes(self):
        return input('enter notes')

    def get_tag(self):
        return input('enter tag')

    def get_priority(self):
        return input('enter priority')

    def get_complete(self):
        return input('enter complete')

    def get_location(self):
        return input('enter location')


    def get_option_awnser(self,option):
        options = {1: self.get_date,
                   2: self.get_time,
                   3: self.get_notes,
                   4: self.get_tag,
                   5: self.get_priority,
                   6: self.get_location}
        return options.get(option)()