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

    def __str__(self):
        s = f'Light = {self.traffic_light_colour} , '
        s += f'Pedestrian = {self.pedestrian_present} , '
        s += f'Vehicle = {self.vehicle_present} .'
        return s

    # Replace these comments with your function commenting
    def update_status(): # You may decide how to implement the arguments for this function
        pass



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
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


        print('*' * 30, 'MORE STUFF ONLY SEEN IF NO ERROR')
    
    print('\n***Thank you for using the Car Vision Detector Processing Program***')






# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

