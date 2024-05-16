# input_processing.py
# Andy Allard, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    
    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
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






# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

