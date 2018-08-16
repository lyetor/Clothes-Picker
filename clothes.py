import numpy as np

class clothe():
    red = None
    blue = None
    green = None
    name = None
    def __init__(self, name, red, blue, green):
        self.name = name
        self.red = red
        self.blue = blue
        self.green = green

    def change_color(self, new_red, new_blue, new_green):
        self.red = new_red
        self.blue = new_blue
        self.green = new_green

    def calculate_color_similarity(first_clothe, second_clothe):
        red_state = False
        blue_state = False
        green_state = False

        if(-50<= second_clothe.red-first_clothe.red <= 50):
            red_state = True  
        if(-50<= second_clothe.blue-first_clothe.blue <= 50):
            blue_state = True  
        if(-50<= second_clothe.green-first_clothe.green <= 50):
            green_state = True  

        if(red_state and blue_state and green_state):
            print("Red, blue, green")
            return 3
        elif(red_state and blue_state):
            print("Red, blue")
            return 2
        elif(green_state and blue_state):
            print("Green, blue")
            return 2
        elif(red_state and green_state):
            print("Red, green")
            return 2
        elif(red_state):
            print("Red")
            return 1
        elif(blue_state):
            print("Blue")
            return 1
        elif(green_state):
            print("Green")
            return 1
        else:
            print("No issue")
            return 0
           

class my_clothes():
    jacket_one = clothe("Grey Jacket", 105, 105, 105)
    jacket_two = clothe("Debate Hoodie", 204, 0, 0)
    jacket_three = clothe("Robotics Hoodie", 255, 51, 0)
    jacket_array = [jacket_one, jacket_two, jacket_three]

    sweater_one = clothe("Red Sweater", 255, 80, 80)
    sweater_two = clothe("Blue Sweater", 51, 102, 255)
    sweater_three = clothe("Orange Sweater", 244, 146, 66)
    sweater_four = clothe("Grey Sweater", 104, 99, 95)
    sweater_five = clothe("Purple Sweater", 80, 1, 114)
    sweater_six = clothe("Green Sweater", 16, 144, 1)
    sweater_array = [sweater_one, sweater_two, sweater_three,
                     sweater_four, sweater_five, sweater_six]

print(clothe.calculate_color_similarity(my_clothes.jacket_one, my_clothes.sweater_one))
   
