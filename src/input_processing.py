# input_processing.py
# Andy Allard, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.


class Sensor:
    """A class used to create a Sensor object.

        Attributes:
            traffic_light_colour (str): String that represents the traffic light's current colour
            pedestrian_present (str): 'yes' if pedestrian is present, 'no' if not
            vehicle_present (str): 'yes' if vehicle is present, 'no' if not

    """
    def __init__(self, traffic_light_colour = 'green', 
                 pedestrian_present = 'no', 
                 vehicle_present = 'no'
                 ):
        """ 
        Initializes a Sensor instance
        
        Args:
            traffic_light_colour (str): String that represents the traffic light's current colour
            pedestrian_present (str): True if pedestrian is present, False if not
            vehicle_present (str): True if vehicle is present, False if not
        """
        self.traffic_light_colour = traffic_light_colour
        self.pedestrian_present = pedestrian_present
        self.vehicle_present = vehicle_present
        self.update_action_message()

    def __str__(self):
        """
        Return a formatted representation of the Sensor informatio
        
        Returns:
            str: A string describing light colour, and whether a pedestrian or vehicle is present
        """
        s = f'\nLight = {self.traffic_light_colour} , '
        s += f'Pedestrian = {self.pedestrian_present} , '
        s += f'Vehicle = {self.vehicle_present} .'
        return s

    # 
    def update_status(self, change_type, new_status):
        """Receives validated inputs from user and changes the sensor status

        Args:
            change_type (str): User response to first question, either '1', '2', or '3'. 

        """
        
        if change_type == '1':
            self.traffic_light_colour = new_status
        elif change_type == '2':
            self.pedestrian_present = new_status
        elif change_type == '3':
            self.vehicle_present = new_status
        self.update_action_message()

    def update_action_message(self):
        """ Updates action_message based on current observations. """
        if (self.traffic_light_colour == 'red'
                or self.pedestrian_present == 'yes'
                or self.vehicle_present == 'yes'):
            self.action_message = 'STOP'
        elif self.traffic_light_colour == 'yellow':
            self.action_message = 'Caution'
        else:
            self.action_message = 'Proceed'

    def print_action_message(self):
        """ Prints a status update to the console. """
        print()
        print(self.action_message)


def print_message(sensor):
    """ Prints the action message and current status"""
    sensor.print_action_message()
    print(sensor)


def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***")
    sensor = Sensor()
    print(sensor)

    valid_menu_inputs = ('0', '1', '2', '3')
    valid_change_inputs = {
        '1': ('green', 'yellow', 'red'),
        '2': ('yes', 'no'),
        '3': ('yes', 'no')
    }
    user_menu_response = ''
    user_change_response = ''

    while True:
        # Prompt user and collect response
        print('\nAre changes detected in the vision output?')
        print('Select 1 for traffic light, 2 for pedestrian, '
              '3 for vehicle, or 0 to end the program: ', end='')
        user_menu_response = input()

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



if __name__ == '__main__':
    main()

