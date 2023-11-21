# Making my classes

# 1st class
# creating a parent class for common attributes shared by the Event and Attndees class
class EventManager:
    def __init__(self, event_id, name, date=None, location=None):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.attendees = []

    # A method (operate within the class)
    def display_details(self):
        print(f'ID: {self.event_id}')
        print(f'Name: {self.name}')

# 2nd class - Event
# it inherites from my EventManager parent class
class Event(EventManager):
    def __init__(self, event_id, name, date, location):
        super().__init__(event_id, name, date, location)
        # super() function is what allows the child class to inherit all the properties of the parent class

    def display_details(self):
        super().display_details()
        print(f'Date: {self.date}')
        print(f'Location: {self.location}')
        print('Attendees:')
        for attendee in self.attendees:
            attendee.display_details()

    def edit_details(self, new_name, new_date, new_location):
        # method to edit events details
        self.name = new_name
        self.date = new_date
        self.location = new_location

    def add_attendee(self, attendee):
        #Add an Attendee to the Events list
        self.attendees.append(attendee)

    def remove_attendee(self, attendee):
        # remove an attendee from the Events list
        self.attendees.remove(attendee)

# 3rd class
class Attendee(EventManager):
    def __init__(self, attendee_id, name, phone):
        # calling the blueprint of the base class
        super().__init__(attendee_id, name)
        # additional attributes specific to Attendee class
        self.phone = phone

    def display_details(self):
        # displaying detail of an Attendee
        super().display_details()
        print(f'Phone: {self.phone}')



