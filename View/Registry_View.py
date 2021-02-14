from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
from Resources import Resources
import string

class Registry_View(Parent_of_Views):  # A "View", takes care of all Front-End components on screen for "Registry" Purpose

    def __init__(self, background): 
        super().__init__(background)

        self.panel = Label()       # Panel for containing the selected Profile Image!
        self.profile_image = None  # Set the user´s profile picture = Attrribute of this class to avoid Auto Garbage Collection
        self.panel_id = None       # and its ID
        self.profile_image_name = None  # This profile image name represents the picture´s name, which will be saved in the local directory
        # Profile Picture Name = "Path_of_the_directory/Username/Date.Of.Birth/" + a random string + ".png"

        self.instantiate_the_buttons()

        self.input_fields_dictionary = {}   # Manage all Input Fields with a dictionary. Dict = Key --> Name | Value --> List [Input Field, its_ID]
        self.instantiate_the_text_fields()

        self.input_field_labels_dictionary = {} # And the belonging labels!
        self.instantiate_the_text_field_labels() 



    def instantiate_the_buttons(self):
        registry_button = Button(self.background, text='Registry', command=self.boss.registrate_action)  # Registry Button
        registry_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Registry(registry_button)

        registry_ok_button = Button(self.background, text='OK', command=self.boss.confirm_registry_action) # Registry OK Button
        registry_ok_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary_for_Registry(registry_ok_button)


        add_profile_image_button = Button(self.background, text='Upload profile image', command=self.select_profile_image_and_show_it_on_screen) # Select Profile Image Button
        add_profile_image_button['font'] = font.Font(size=Resources.size_of_text_in_selecting_profile_image_button)
        self.registrate_a_button_into_buttons_dictionary_for_Registry(add_profile_image_button)

    
    def instantiate_the_text_fields(self):
        name_input_field = Entry(self.background, width=Resources.text_field_width)     # Name Input Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_Registry(name_input_field, 'Name')
 
        date_of_birth_input_field = Entry(self.background, width=Resources.text_field_width)    # Date of Birth Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_Registry(date_of_birth_input_field, 'Date of Birth')

        password_input_field = Entry(self.background, width=Resources.text_field_width)      # Password Field
        self.registrate_an_input_field_into_input_fields_dictionary_for_Registry(password_input_field, 'Password')


    def instantiate_the_text_field_labels(self):
        name_input_field_label = Label(self.background, text='Name', fg='brown', font=font.Font(size=13))   # Name Input Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_Registry(name_input_field_label)

        date_of_birth_input_field_label = Label(self.background, text='Date of birth', fg='brown', font=font.Font(size=13)) # Date of Birth Input Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_Registry(date_of_birth_input_field_label)

        password_input_field_label = Label(self.background, text='Password', fg='brown', font=font.Font(size=13)) # Password Field Label
        self.registrate_an_input_field_label_into_input_field_labels_dictionary_for_Registry(password_input_field_label)


    def registrate_an_input_field_into_input_fields_dictionary_for_Registry(self, input_field, name):
        self.input_fields_dictionary[name] = []
        self.input_fields_dictionary.get(name).append(input_field)
        

    def registrate_an_input_field_label_into_input_field_labels_dictionary_for_Registry(self, input_field_label):
        self.input_field_labels_dictionary[input_field_label['text']] = []
        self.input_field_labels_dictionary.get(input_field_label['text']).append(input_field_label)


    def set_up(self):
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


    def put_the_input_field_on_screen_and_registrate_its_ID(self, input_field, name, x, y):
        input_field_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=input_field)
        self.input_fields_dictionary.get(name).append(input_field_id)

    
    def put_the_input_field_label_on_screen_and_registrate_its_ID(self, input_field_label, x, y):
        input_field_label_id = self.background.create_window(x, y, width=Resources.text_field_width,
                            height=Resources.text_field_height, window=input_field_label)
        self.input_field_labels_dictionary.get(input_field_label['text']).append(input_field_label_id)        


    def select_profile_image_and_show_it_on_screen(self):
        # open a file chooser dialog and allow the user to select an input image
	    path = tkFileDialog.askopenfilename()
        if len(path) > 0:
            # load the image from disk
		    self.profile_image = cv2.imread(path)
		    # OpenCV represents images in BGR order; however PIL represents
		    # images in RGB order, so we need to swap the channels
		    self.profile_image = cv2.cvtColor(self.profile_image, cv2.COLOR_BGR2RGB)
		    # convert the images to PIL format...
		    self.profile_image = Image.fromarray(self.profile_image)
		    # ...and then to ImageTk format
		    self.profile_image = ImageTk.PhotoImage(self.profile_image)
            # Put the image onto the Panel
            self.panel.configure(image=self.profile_image)
            self.panel.image = self.profile_image    # Also set the Image = Attribute of the GUI Label on screen to avoid Garbage Collection
            self.background.itemconfigure(self.panel_id, state='normal')


    def save_user_profile_picture(self):
        # This function save the user_profile_picture and give the path of the it back, to store in the database!

        # First give the picture a name to save to the local directory!
        # Name Format is mentioned above: "Path_of_the_directory/Username/Date.Of.Birth/" + a random string + ".png"
        username = self.input_fields_dictionary.get('Name')[0].get()
        date_of_birth = self.input_fields_dictionary.get('Date of Birth')[0].get()
        # Create the random string 
        random_string = ''
        letters = string.ascii_letters
        for i in range(10):
            random_string.join(random.choice(letters))
        # The name of the picture would be ...
        name = Resources.path_of_the_users_pictures_directory + "/" + username + "/" + date_of_birth + "/" + random_string + ".png"
        # Now save the picture 
        # If user didn´t choose an image (self.profile_image = None) ---> Set the default image as profile image!
        if self.profile_image = None 
            name = Resources.profile_default_picture_path
            # The default is already saved in the directory --> No need to extra save!
        else
            # Save the picture
            self.profile_image.write(name, format='png')

        # Return the path back to store in the database
        return name