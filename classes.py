# classes.py
import logging
from abc import ABC, abstractmethod
from exceptions import EventManagementException

# Setting up logging configuration
logging.basicConfig(filename='event_management.log', level=logging.INFO)

# Decorator for logging method calls
def log_method_call(method):
    def wrapper(*args, **kwargs):
        result = method(*args, **kwargs)
        logging.info(f"Method {method.__name__} called with arguments {args} and keyword arguments {kwargs}")
        return result
    return wrapper

# 1st class - EventManager (Parent class)
class EventManager(ABC):
    def __init__(self, event_id, name, date=None, location=None):
        self.__event_id = event_id
        self.__name = name
        self.__date = date
        self.__location = location
        self.__attendees = []

    @abstractmethod
    def display_details(self):
        pass

    def log_event_details(self):
        logging.info(f'ID: {self.__event_id}')
        logging.info(f'Name: {self.__name}')

    def raise_event_management_exception(self, message):
        raise EventManagementException(message)

    def get_event_id(self):
        return self.__event_id

    def set_event_id(self, event_id):
        self.__event_id = event_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_attendees(self):
        return self.__attendees

    def set_attendees(self, attendees):
        self.__attendees.extend(attendees)

# 2nd class - Event (Child class, Inherits from EventManager)
class Event(EventManager):
    def __init__(self, event_id, name, date, location):
        super().__init__(event_id, name, date, location)
        self.__attendees = []

    @log_method_call
    def display_details(self):
        self.log_event_details()
        logging.info(f'Date: {self.get_date()}')
        logging.info(f'Location: {self.get_location()}')
        logging.info('Attendees:')
        for attendee in self.__attendees:
            attendee.display_details()

    @log_method_call
    def edit_details(self, new_name, new_date, new_location):
        self.set_name(new_name)
        self.set_date(new_date)
        self.set_location(new_location)

    @log_method_call
    def add_attendee(self, attendee):
        self.__attendees.append(attendee)

    @log_method_call
    def remove_attendee(self, attendee):
        self.__attendees.remove(attendee)

# 3rd class - Attendee (Child class, Inherits from EventManager)
class Attendee(EventManager):
    def __init__(self, attendee_id, name, phone):
        super().__init__(attendee_id, name)
        self.__phone = phone

    @log_method_call
    def display_details(self):
        self.log_event_details()
        logging.info(f'Phone: {self.__phone}')

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone
