class Reminder:
    def __init__(self):
        pass

    def name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_tag(self, tag):
        self.tag = tag

    def set_notes(self, notes):
        self.notes = notes

    def set_priority(self, priority):
        self.priority = priority

    def set_complete(self, complete):
        self.complete = complete

    def set_location(self, location):
        self.location = location

    def repeat(self):
        pass

    def set_atribute(self, atribute, data):
        atributes = {1: self.set_date}
        atributes.get(atribute)(data)