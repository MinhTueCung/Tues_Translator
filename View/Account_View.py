class Account_View(Parent_of_Views):  # Front-End View of all "Account" Functions (Check account, account settings,...)

    def __init__(self, background):
        super().__init__(background)

        self.instantiate_all_buttons()

        self.labels_dictionary = {}
        self.instantiate_all_labels()

        self.input_fields_dictionary = {}
        self.instantiate_all_input_fields()

        self.panel = Label()       # Panel for containing the selected Profile Image!
        self.profile_image = None  # Set the user´s profile picture = Attrribute of this class to avoid Auto Garbage Collection
        self.panel_id = None       # and its ID

        self.report_panel = Label()   # This panel is for showing some important messages (deleting an account,...)



    def instantiate_all_buttons(self):
        # The texts themselves of the buttons will be used as keys in "buttons_dict"
        # --> All Buttons should have unique text names
        account_button = Button(self.background, text='Account', command=self.boss.show_account_action)  # Account Button
        account_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(account_button)

        edit_account_button = Button(self.background, text='Edit', command=self.boss.edit_account_action) # Edit Account Button
        edit_account_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(edit_account_button)

        back_button = Button(self.background, text='Back', command=self.boss.back_action) # Back Button: switches the screen from "Account Profile" to "Play Menu"
        back_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(back_button)

        cancel_button = Button(self.background, text='Cancel', command=self.boss.cancel_action) # Cancel Button: cancel editing Account
        cancel_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(cancel_button)

        save_button = Button(self.background, text='Save', command=self.boss.save_action)  # Save the new Account Configurations
        save_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(save_button)

        delete_account_button = Button(self.background, text='Delete', command=self.boss.delete_account_action)  # Delete Account
        delete_account_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(delete_account_button)

        edit_profile_image_button = Button(self.background, text='Edit Photo', command=self.boss.change_profile_image)  # Change Profile Image
        edit_profile_image_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(edit_profile_image_button)

        yes_delete_acc_button = Button(self.background, text='Yes', commmand=self.boss.yes_delete_acc)  # This Button to confirm the "Delete Account" Decision from the User
        yes_delete_acc_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(yes_delete_acc_button)

        no_delete_acc_button = Button(self.background, text='No', commmand=self.boss.no_delete_acc)  # And No!
        no_delete_acc_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dict(no_delete_acc_button)

    

    def instantiate_all_labels(self):
        name_label = Label(self.background, text='Name', fg='brown', font=font.Font(size=13))   # Name Input Field Label
        self.registrate_a_label_into_labels_dictionary(name_label)

        date_of_birth_label = Label(self.background, text='Date of birth', fg='brown', font=font.Font(size=13)) # Date of Birth Input Field Label
        self.registrate_a_label_into_labels_dictionary(date_of_birth_label)

        password_label = Label(self.background, text='Password', fg='brown', font=font.Font(size=13)) # Password Field Label
        self.registrate_a_label_into_labels_dictionary(password_label)


    def instantiate_the_input_fields(self):
        name_input_field = Entry(self.background, width=Resources.text_field_width)     # Name Input Field
        self.registrate_an_input_field_into_input_fields_dictionary(name_input_field, 'Name')
 
        date_of_birth_input_field = Entry(self.background, width=Resources.text_field_width)    # Date of Birth Field
        self.registrate_an_input_field_into_input_fields_dictionary(date_of_birth_input_field, 'Date of Birth')

        password_input_field = Entry(self.background, width=Resources.text_field_width)      # Password Field
        self.registrate_an_input_field_into_input_fields_dictionary(password_input_field, 'Password')


    def registrate_a_label_into_labels_dictionary(self, label):
        self.labels_dictionary[label['text']] = []
        self.labels_dictionary.get(label['text']).append(label)

    def registrate_an_input_field_into_input_fields_dictionary(self, input_field, name):
        self.input_fields_dictionary[name] = []
        self.input_fields_dictionary.get(name).append(input_field)


    def put_the_input_field_on_screen_and_registrate_its_ID(self, input_field, name, x, y):
        input_field_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=input_field)
        self.input_fields_dictionary.get(name).append(input_field_id)

    
    def put_the_label_on_screen_and_registrate_its_ID(self, label, x, y):
        label_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=label)
        self.labels_dictionary.get(label['text']).append(label_id)        


    def set_up(self):
        # Put all the elements on screen!
        # The buttons
        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('Registry')[0], 50, 60)
        self.background.itemconfigure(self.buttons_dictionary.get('Registry')[1], state='normal')

        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('OK')[0], 100, 100)
        self.background.itemconfigure(self.buttons_dictionary.get('OK')[1], state='hidden')

        # The Input Fields
        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary.get('Name')[0], 'Name', 50, 50)
        self.background.itemconfigure(self.input_fields_dictionary.get('Name')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary.get('Date of Birth')[0], 'Date of Birth', 50, 70)
        self.background.itemconfigure(self.input_fields_dictionary.get('Date of Birth')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary.get('Password')[0], 'Password', 50, 90)
        self.background.itemconfigure(self.input_fields_dictionary.get('Password')[1], state='hidden')

        # The Input Field Labels
        self.put_the_input_field_label_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary.get('Name')[0], 30, 50)
        self.background.itemconfigure(self.input_field_labels_dictionary.get('Name')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary.get('Date of Birth')[0], 30, 70)
        self.background.itemconfigure(self.input_field_labels_dictionary.get('Date of Birth')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary.get('Password')[0], 30, 90)
        self.background.itemconfigure(self.input_field_labels_dictionary.get('Password')[1], state='hidden')

        # The Panel for Profile Image
        panel_id = self.background.create_window(Resources.x_position_of_the_selected_profile_image, 
                                                    Resources.y_position_of_the_selected_profile_image,   
                                                    width=Resources.standard_width_of_a_button,
                                                    height=Resources.standard_height_of_a_button, window=self.panel)
        self.panel_id = panel_id
        self.background.itemconfigure(self.panel_id, state='hidden')

    def get_input_fields_dict(self):
        return self.input_fields_dictionary

    def get_labels_dict(self):
        return self.labels_dictionary

    def get_report_panel(self):
        return self.report_panel

    


