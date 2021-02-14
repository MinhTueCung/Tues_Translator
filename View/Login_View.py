from Resources import Resources

class Login_View(Parent_of_Views):     # Front-End components for "Login" purpose

    def __init__(self, background):
        super().__init__(background)
        
        self.instantiate_the_buttons()
        
        self.input_fields_dictionary = {} # The same as "buttons_dictionary_for_Logging"
        self.instantiate_the_text_fields()
        
        self.input_field_labels_dictionary = {}  # The same as "buttons_dictionary_for_Logging"
        self.instantiate_the_text_field_labels()

        self.login_as_user = False  # Boolean to decide whether current user is logged in as Guest (login_as_user = False)
                                    # or as a User (login_as_user = True)

        
    def instantiate_the_buttons(self):
        login_button = Button(self.background, text='Login', command=self.boss.login_action)  # Login Button
        login_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Logging(login_button)

        login_as_guest_button = Button(self.background, text='Guest', command=self.boss.login_as_guest_action) # Login as Guest
        login_as_guest_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Logging(login_as_guest_button)

        login_as_user_button = Button(self.background, text='User', command=self.boss.login_as_user_action) # Login as User
        login_as_user_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Logging(login_as_user_button)

        ok_button = Button(self.background, text='OK', command=self.boss.confirm_login_infos_action) # Confirm the Infos given
        ok_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Logging(ok_button) 


    def instantiate_the_text_fields(self):
        name_input_field = Entry(self.background, width=Resources.text_field_width)     # Name Input Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_logging(name_input_field, 'Name')
 
        date_of_birth_input_field = Entry(self.background, width=Resources.text_field_width)    # Date of Birth Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_logging(date_of_birth_input_field, 'Date of Birth')

        password_input_field = Entry(self.background, width=Resources.text_field_width)      # Password Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_logging(password_input_field, 'Password')


    def instantiate_the_text_field_labels(self):
        name_input_field_label = Label(self.background, text='Name', fg='brown', font=font.Font(size=13))   # Name Input Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_logging(name_input_field_label)

        date_of_birth_input_field_label = Label(self.background, text='Date of birth', fg='brown', font=font.Font(size=13)) # Date of Birth Input Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_logging(date_of_birth_input_field_label)

        password_input_field_label = Label(self.background, text='Password', fg='brown', font=font.Font(size=13)) # Password Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_logging(password_input_field_label)



    def registrate_an_input_field_into_input_fields_dictionary_for_logging(self, input_field, name):
        self.input_fields_dictionary_for_Logging[name] = []
        self.input_fields_dictionary_for_Logging.get(name).append(input_field)
        

    def registrate_an_input_field_label_into_input_field_labels_dictionary_for_logging(self, input_field_label):
        self.input_field_labels_dictionary_for_logging[input_field_label['text']] = []
        self.input_field_labels_dictionary_for_logging.get(input_field_label['text']).append(input_field_label)


    def set_up(self):
        # The buttons
        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('Login')[0], 50, 50)
        self.background.itemconfigure(self.buttons_dictionary.get('Login')[1], state='normal')

        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('Guest')[0], 50, 50)
        self.background.itemconfigure(self.buttons_dictionary.get('Guest')[1], state='hidden')

        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('User')[0], 50, 50)
        self.background.itemconfigure(self.buttons_dictionary.get('User')[1], state='hidden')

        self.put_the_button_on_screen_and_registrate_its_ID(self.buttons_dictionary.get('OK')[0], 100, 100)
        self.background.itemconfigure(self.buttons_dictionary.get('OK')[1], state='hidden')

        # The Input Fields
        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary_for_Logging.get('Name')[0], 'Name', 50, 50)
        self.background.itemconfigure(self.input_fields_dictionary_for_Logging.get('Name')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary_for_Logging.get('Date of Birth')[0], 'Date of Birth', 50, 70)
        self.background.itemconfigure(self.input_fields_dictionary_for_Logging.get('Date of Birth')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_fields_dictionary_for_Logging.get('Password')[0], 'Password', 50, 90)
        self.background.itemconfigure(self.input_fields_dictionary_for_Logging.get('Password')[1], state='hidden')

        # The Input Field Labels
        self.put_the_input_field_label_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary_for_logging.get('Name')[0], 30, 50)
        self.background.itemconfigure(self.input_field_labels_dictionary_for_logging.get('Name')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary_for_logging.get('Date of Birth')[0], 30, 70)
        self.background.itemconfigure(self.input_field_labels_dictionary_for_logging.get('Date of Birth')[1], state='hidden')

        self.put_the_input_field_on_screen_and_registrate_its_ID(self.input_field_labels_dictionary_for_logging.get('Password')[0], 30, 90)
        self.background.itemconfigure(self.input_field_labels_dictionary_for_logging.get('Password')[1], state='hidden')



    def put_the_input_field_on_screen_and_registrate_its_ID(self, input_field, name, x, y):
        input_field_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=input_field)
        self.input_fields_dictionary_for_Logging.get(name).append(input_field_id)

    
    def put_the_input_field_label_on_screen_and_registrate_its_ID(self, input_field_label, x, y):
        input_field_label_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=input_field_label)
        self.input_field_labels_dictionary_for_logging.get(input_field_label['text']).append(input_field_label_id)    



    