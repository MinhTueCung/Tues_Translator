class Settings_View(Parent_of_Views):   # Another View, in charge of all Front-End "Settings" Components

    def __init__(self, background):
        super().__init__(background)

        self.int_value_radio_choose = IntVar()   # This will decide which button was chosen --> Desired Languages !
        self.int_value_radio_choose.set('1')    # English chosen as Default! Check the "supported_languages_dictionary"

        self.instantiate_all_buttons()

        self.list_of_radio_buttons = []     # List of "language choice" radio buttons!
        self.instantiate_all_radio_buttons()

        self.list_of_radio_buttons_asscociated_pictures = [] # This list stores the asscociated_pictures of the radio buttons
                                            # to avoid auto garbage collection (due to lack of reference)

        self.list_of_radio_buttons_id = []   # and their IDs, for supervision by the background 
        


    def instantiate_all_radio_buttons(self):
        # Instantiate the "flag" (language choices) radio buttons
        x = 0     # Counter! We will go through all the languages supported in Resources: supported_languages_dictionary

        # Instantiate and add the button into the list_of_radio_buttons
        while x < len(Resources.supported_languages_dictionary):
            a_radio_button = Radiobutton(self.background, variable=self.int_value_radio_choose, value=x + 1)
            associated_image = ImageTk.PhotoImage(
                Image.open(
                    'F:/pythonProject/Tues_Translator/Resources/' + Resources.supported_languages_dictionary.get(
                        x + 1) + '.jpg'))
            a_radio_button.config(image=associated_image)
            self.list_of_radio_buttons.append(a_radio_button)



    def instantiate_all_buttons(self):
        settings_button = Button(self.background, text='Settings', command=self.boss.display_settings) # Settings Button
        settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary(settings_button)

        save_settings_button = Button(self.background, text='Save', command=self.boss.save_settings_action) # Save Settings Button
        save_settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary(save_settings_button)

        clear_settings_button = Button(self.background, text='Clear', command=self.boss.clear_settings_action)  # Clear Settings Button
        clear_settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary(clear_settings_button)



    def set_up(self):
        self.put_the_radio_buttons_on_screen_and_registrate_its_ID()
        


    def put_the_radio_buttons_on_screen_and_registrate_its_ID(self):
        x = 0  # Counter! We´ll go through all the list_of_radio_buttons

        # Create the first half of the buttons on the left side of the screen
        while x < int(len(Resources.supported_languages_dictionary) / 2):
            a_radio_button_id = self.background.create_window(230, x * 75 + 170, window=self.list_of_radio_buttons[x])
            self.list_of_language_radio_buttons_id.append(a_radio_button_id)
            x += 1

        # Create the second half on the right side of the screen
        while x < len(Resources.supported_languages_dictionary):        
            a_radio_button_id = self.background.create_window(440, (x - int(len(Resources.supported_languages_dictionary) / 2)) * 75 + 170, window=self.list_of_radio_buttons[x])
            self.list_of_language_radio_buttons_id.append(a_radio_button_id)
            x += 1