# input_processing.py
# Andy Allard, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


class Sensor:
    
    def __init__(self, traffic_light_colour = 'green', 
                 pedestrian_present = 'no', 
                 vehicle_present = 'no'
                 ):
        self.traffic_light_colour = traffic_light_colour
        self.pedestrian_present = pedestrian_present
        self.vehicle_present = vehicle_present
        self.update_action_message()

    def __str__(self):
        s = f'\nLight = {self.traffic_light_colour} , '
        s += f'Pedestrian = {self.pedestrian_present} , '
        s += f'Vehicle = {self.vehicle_present} .'
        return s

    # Receives validated inputs from user and changes the sensor status
    def update_status(self, change_type, new_status):
        if change_type == '1':
            self.traffic_light_colour = new_status
        elif change_type == '2':
            self.pedestrian_present = new_status
        elif change_type == '3':
            self.vehicle_present = new_status
        
        # # debug. REMOVE LATER
        # print(change_type, new_status)

        self.update_action_message()

    def update_action_message(self):
        if (self.traffic_light_colour == 'red'
                or self.pedestrian_present == 'yes'
                or self.vehicle_present == 'yes'):
            self.action_message = 'STOP'
        elif self.traffic_light_colour == 'yellow':
            self.action_message = 'Caution'
        else:
            self.action_message = 'Proceed'

    def print_action_message(self):
        print()
        print(self.action_message)


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    sensor.print_action_message()
    print(sensor)


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***")
    sensor = Sensor()
    print(sensor)

    valid_menu_inputs = ['0', '1', '2', '3']
    valid_change_inputs = {
        '1': ['green', 'yellow', 'red'],
        '2': ['yes', 'no'],
        '3': ['yes', 'no']
    }
    user_menu_response = ''
    user_change_response = ''

    while True:
        # Prompt user and collect response
        print('\nAre changes detected in the vision output?')
        print('Select 1 for traffic light, 2 for pedestrian, '
              '3 for vehicle, or 0 to end the program: ', end='')
        user_menu_response = input()

        # debugging... REMOVE LATER!
        # print('user_menu_response', user_menu_response, type(user_menu_response))

        # Validate user input for first question
        try:
            if user_menu_response not in valid_menu_inputs:
                raise ValueError('Invalid menu entry.')
        except ValueError as err:
            print('You must select 1, 2, 3, or 0.')
            continue

        # Exit program if user enters '0'
        if user_menu_response == '0':
            break

        # Ask second question
        user_change_response = input('What change has been identified? : ')
        
        # Validate user input for second question

        # debugging... REMOVE LATER!
        # print('valid change inputs', valid_change_inputs[user_menu_response])

        try:
            if user_change_response not in valid_change_inputs[user_menu_response]:
                raise ValueError('Invalid menu entry.')
        except ValueError as err:
            print('Invalid vision change.')
            continue

        # Handle valid user input by updating status and issuing an action message
        sensor.update_status(user_menu_response, user_change_response)
        print_message(sensor)
    
    print('\n***Thank you for using the Car Vision Detector Processing Program***')






# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

