from abc import ABC, abstractmethod
# This class defines the basic skeleton of all the "X_View" classes, which implement the Front-End
# Each "X_View" takes the one same screen to control the Front-End, and also 1 "Controller"
# While the background is passed to X_View right at the moment of instantiation, the Controller is introduced to it later
# Program´s start: Build the Canvas background, instatiate the "Views", instantiate their "Controllers", introduce the Controllers to their "Views"
# The Controllers guide the functional sides of their "Views"

class Parent_of_Views(ABC):

    def __init__(self, background):
        self.background = background
        self.boss = None         # First just leave "None"
        self.buttons_dict = {}          # Buttons dictionary with Key = Text in the Button | Value = List with [the Button itself, its ID]

    def registrate_a_button_into_buttons_dict(self, button):
        self.buttons_dict[button.cget('text')] = []
        self.buttons_dict.get(button.cget('text')).append(button)

    @abstractmethod
    def set_up(self):
        pass

    def put_the_button_on_screen_and_registrate_its_ID(self, button, x, y):
        button_id = self.background.create_window(x, y, width=Resources.standard_width_of_a_button,
                            height=Resources.standard_height_of_a_button, window=button)
        self.buttons_dict.get(button.cget('text')).append(button_id)

    def get_background(self):
        return self.background

    def get_buttons_dict(self):
        return self.buttons_dict

    # "Introduce" method
    def set_boss_controller(self, boss_controller):
        self.boss = boss_controller


        