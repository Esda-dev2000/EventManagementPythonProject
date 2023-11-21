# Making my function
import csv
from classes import *

# base/parent class
class EventManager:
    def __init__(self, event_id, name):
        # initilising common attributes for all classes
        self.event_id = event_id
        self.name = name

# creating a method for displaying the details of this base class
    # methods operate within a class
    def display_details(self):
        pass

# a function = operates OUTSIDE a class
# function to create a new event
def create_event(events, Event):
    try:
        event_id = int(input(f'Enter {Event.__name__} ID: '))
        name = input(f'Enter {Event.__name__} Name: ')
        date = input(f'Enter {Event.__name__} Date (YYYY-MM-DD): ')
        location = input(f'Enter {Event.__name__} Lcation: ')

        # checking if the event ID already exits
        if any(event.event_id == event_id for event in events):
            print(f'{Event.__name__} ID already exist. Please choose a different ID.')
            return

        # instance of the Event class and adds it to the list
        event = Event(event_id, name, date, location)
        events.append(event)
        print(f'{Event.__name__} created successfully.')
    except ValueError:
        print('Invalid input. Please enter valid values.')


# this function lists details of all events
def list_all_events(events):
    for event in events:
        event.display_details() #calling

# function to list details of an indvidual event by ID
def list_individual_event(event_id, events):
    # Find and display details of an individual event by ID
    for event in events:
        if event.event_id == event_id:
            event.display_details()
            break
    else:
        print(f'Event with ID {event_id} not found.')

# function to edit details of an existing event
def edit_event(events, Event):
    try:
        # Get input from the user
        event_id = int(input(f'Enter the {Event.__name__} ID to edit: '))
        for event in events:
            if event.event_id == event_id:
                # Get new details from the user and update the event
                new_name = input(f'Enter new {Event.__name__} Name: ')
                new_date = input(f'Enter new {Event.__name__} Date (YYYY-MM-DD): ')
                new_location = input(f'Enter new {Event.__name__} Location: ')

                event.edit_details(new_name, new_date, new_location)
                print(f'{Event.__name__} details have been updated successfully.')
                break
        else:
            print(f'{Event.__name__} with ID {event_id} not found.')
    except ValueError:
        print('Invalid input. Please enter a valid ID.')

# Function to delete an existing event
def delete_event(events, Event):
    try:
        # Get input from the user
        event_id = int(input(f'Enter the {Event.__name__} ID to delete: '))
        for event in events:
            if event.event_id == event_id:
                # Remove the event from the list
                events.remove(event)
                print(f'{Event.__name__} deleted successfully.')
                break
        else:
            print(f'{Event.__name__} with ID {event_id} not found.')
    except ValueError:
        print('Invalid input. Please enter a valid ID.')

def list_attendees(event_id, events):
    for event in events:
        if event.event_id == event_id:
            # Display attendees for the selected event
            if event.attendees:
                print('Attendees:')
                for attendee in event.attendees:
                    print(f'{attendee.name} - {attendee.phone}')
            else:
                print('No attendees for this event.')
            break
    else:
        print(f'Event with ID {event_id} not found.')

def add_attendee(events):
    try:
        # Get input from the user
        event_id = int(input('Enter the Event ID to add an attendee: '))
        for event in events:
            if event.event_id == event_id:
                # Ask if the user wants to add multiple attendees
                multiple_attendees = input('Do you want to add multiple attendees? (y/n): ').lower() == 'y'
                while True:
                    attendee_id = int(input('Enter Attendee ID: '))
                    name = input('Enter Attendee Name: ')
                    phone = input('Enter Attendee Phone: ')

                    # Create an instance of the Attendee class and add it to the event
                    attendee = Attendee(attendee_id, name, phone)
                    event.add_attendee(attendee)
                    print('Attendee added successfully.')

                    if not multiple_attendees:
                        break

                    add_more = input('Do you want to add another attendee? (y/n): ').lower()
                    if add_more != 'y':
                        break

                break
        else:
            print(f'Event with ID {event_id} not found.')
    except ValueError:
        print('Invalid input. Please enter valid values.')

def delete_attendee(events):
    try:
        # Get input from the user
        event_id = int(input('Enter the Event ID to delete an attendee: '))
        for event in events:
            if event.event_id == event_id:
                attendee_name = input('Enter Attendee Name: ')
                attendee_phone = input('Enter Attendee Phone: ')

                for attendee in event.attendees:
                    if attendee.name == attendee_name and attendee.phone == attendee_phone:
                        # Remove the attendee from the event
                        event.remove_attendee(attendee)
                        print('Attendee deleted successfully.')
                        break
                else:
                    print('Attendee not found.')
                break
        else:
            print(f'Event with ID {event_id} not found.')
    except ValueError:
        print('Invalid input. Please enter valid values.')

# Function to read events and attendees from a CSV file
def read_events_from_csv(eventfile):
    events = []

    try:
        # Try to open the file for reading
        with open(eventfile, mode='r') as file:
            # Create a CSV reader object
            reader = csv.DictReader(file)

            # Iterate over each row in the CSV file
            for row in reader:
                # Extract event details from the row
                event_id = int(row['event_id'])
                event_name = row['event_name']
                date = row['date']
                location = row['location']

                # Create an Event object and append it to the events list
                event = Event(event_id, event_name, date, location)
                events.append(event)

                # Extract attendee details from the row
                attendee_id = int(row['attendee_id'])
                attendee_name = row['attendee_name']
                phone = row['phone']

                # Create an Attendee object and add it to the event's attendees
                attendee = Attendee(attendee_id, attendee_name, phone)
                event.add_attendee(attendee)

    except FileNotFoundError:
        # If the file is not found, create an empty CSV file
        with open(eventfile, mode='w', newline='') as file:
            # Create a CSV writer object
            writer = csv.DictWriter(file, fieldnames=['event_id', 'event_name', 'date', 'location', 'attendee_id',
                                                      'attendee_name', 'phone'])
            # Write the header to the CSV file
            writer.writeheader()

        # Print the events list before returning
    print("Events after reading:", events)

    # Return the list of events
    return events

# Function to write events and attendees to a CSV file
def write_events_to_csv(eventfile, events):
    try:
        # Open the file for writing (newline='' ensures cross-platform compatibility)
        with open(eventfile, 'w', newline='') as file:
            # Create a CSV writer object with the specified fieldnames
            writer = csv.DictWriter(file, fieldnames=['event_id', 'event_name', 'date', 'location', 'attendee_id',
                                                      'attendee_name', 'phone'])

            # Write the header to the CSV file
            writer.writeheader()

            # Iterate over each event in the events list
            for event in events:
                # Iterate over each attendee in the event's attendees list
                for attendee in event.attendees:
                    # Write a row to the CSV file for each event and attendee
                    data = {
                        'event_id': event.event_id,
                        'event_name': event.name,
                        'date': event.date,
                        'location': event.location,
                        'attendee_id': attendee.event_id,
                        'attendee_name': attendee.name,
                        'phone': attendee.phone
                    }
                    print(f'Writing data: {data}')
                    writer.writerow(data)

        print(f'Events written to {eventfile} successfully.')

    except Exception as e:
        print(f'Error writing to {eventfile}: {e}')