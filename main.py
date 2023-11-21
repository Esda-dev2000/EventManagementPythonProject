# Importing necessary modules
from classes import *
from functions import (
    create_event, list_all_events, list_individual_event,
    edit_event, delete_event, list_attendees,
    add_attendee, delete_attendee, read_events_from_csv,
    write_events_to_csv
)

def main():
    # Reads events and attendees from CSV file
    events = read_events_from_csv('events.csv')

    # While loop for the menu
    while True:
        print('======Finance Event Management System======')
        print('1. Create Event')
        print('2. List All Events')
        print('3. List Individual Event')
        print('4. Edit Event')
        print('5. Delete Event')
        print('6. List Attendees for Event')
        print('7. Add Attendee to Event')
        print('8. Delete Attendee from Event')
        print('9. Exit Application')

        # Asking for user input
        user_choice = input('Enter your choice (1-9): ')

        # If statement for the user's choice
        if user_choice == '1':
            create_event(events, Event)
        elif user_choice == '2':
            list_all_events(events)
        elif user_choice == '3':
            event_id = int(input('Enter the Event ID: '))
            list_individual_event(event_id, events)
        elif user_choice == '4':
            edit_event(events, Event)
        elif user_choice == '5':
            delete_event(events, Event)
        elif user_choice == '6':
            event_id = int(input('Enter the Event ID to list attendees: '))
            list_attendees(event_id, events)
        elif user_choice == '7':
            add_attendee(events)
        elif user_choice == '8':
            delete_attendee(events)
        elif user_choice == '9':
            # Write events and attendees to CSV file before exiting
            write_events_to_csv('events.csv', events)
            print('Exiting the event application... Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')

# conditional block - It Allows  to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
if __name__ == '__main__':
    main()