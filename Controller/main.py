from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from Resources import Resources
from Model.Translator import Translator
from Model.Background_Thread_for_the_Translator import Background_Thread_for_the_Translator
from Resources.Database import Database

class Main_App:
    def __init__(self):
        self.language_1 = Resources.supported_languages_dictionary.get(1) # English as 1st default
        self.language_2 = Resources.supported_languages_dictionary.get(6) # Vietnamese as 2nd default

        self.current_user = None    # Show the current logged in user! This is the id column in the database 
                                    # which is unique for every single user 

        self.root = Tk()                # Root
        self.root.title("Tue´s Translator")   # Title
        self.background = Canvas(self.root, width=Resources.canvas_background_on_gui_width, height=Resources.canvas_background_on_gui_height)
        self.background_jarvis_photo = ImageTk.PhotoImage(
            Image.open('F:/pythonProject/Tues_Translator/Resources/jarvis.jpg'))

        self.login_view_verwalter = Login_View_Verwalter(self.background, self)  # The Login View Servant

        self.registry_view_verwalter = Registry_View_Verwalter(self.background, self)  # The Registry View Servant

        self.settings_view_verwalter = Settings_View_Verwalter(self.background, self)   # The Settings View Servant

        self.play_view_verwalter = Play_View_Verwalter(self.background, self)    # The Play View Servant

        self.database_checker = Database_Checker()

        self.the_translator = None
        self.background_thread_for_the_translator = None

        self.message_label = Label(self.background, text='Nothing yet', fg='brown', font=font.Font(size=17))


    def start(self):
        self.background.pack()
        self.root.mainloop()


    def set_up(self):
        self.background.create_image(0, 0, image=self.background_jarvis_photo, anchor=NW)  # Create JARVIS Background

        

        self.background.itemconfigure(self.message_label_id, state='hidden')
        self.background.itemconfigure(self.save_settings_button_id, state='hidden')
        self.background.itemconfigure(self.back_button_id, state='hidden')
        self.background.itemconfigure(self.clear_settings_button_id, state='hidden')
        for a_flag_radio_button_id in self.list_of_language_radio_buttons_id:
            self.background.itemconfigure(a_flag_radio_button_id, state='hidden')

    def get_current_user(self):
        return self.current_user


    def build_the_Translator_and_start_having_fun(self):
        
        self.the_translator = Translator(self.language_1, self.language_2, self.message_label)
        self.background_thread_for_the_translator = Background_Thread_for_the_Translator(self.the_translator)
        self.background_thread_for_the_translator.switch_this_thread_on()
        self.background_thread_for_the_translator.start()

    def save_settings(self):
        if self.language_1 == None:
            if self.language_2 == None:
                language_value = self.int_value_radio_choose.get()
                self.language_1 = Resources.supported_languages_dictionary.get(language_value)
                self.message_label.configure(text='1 Language was set: ' + self.language_1 + '\nChoose the other language then hit "Save"')
            else:
                language_value = self.int_value_radio_choose.get()
                self.language_1 = Resources.supported_languages_dictionary.get(language_value)
                self.message_label.configure(text='All 2 languages were set: ' + self.language_1 + ' + ' + self.language_2
                                             + '\nHit "Clear" for reconfiguring and "Save", if any')
        else:
            if self.language_2 == None:
                language_value = self.int_value_radio_choose.get()
                self.language_2 = Resources.supported_languages_dictionary.get(language_value)
                self.message_label.configure(text='All 2 languages were set: ' + self.language_1 + ' + ' + self.language_2
                                             + '\nHit "Clear" for reconfiguring and "Save", if any')
            else:
                pass


    def back_action(self):
        # "Back" Button can be used to
        # 1. escape the settings, back to the main menu
        # 2. stop the background thread (for the translator), back to the main menu
        # --> Check whether this background thread is there or not. If it´s there --> 2nd use case, if not --> 1st use case

        if self.background_thread_for_the_translator != None:
            self.background_thread_for_the_translator.switch_this_thread_off()

        # The "back to the main menu" common part can be written once only for both of the cases
        self.background.itemconfigure(self.start_button_id, state='normal')
        self.background.itemconfigure(self.settings_button_id, state='normal')
        self.background.itemconfigure(self.save_settings_button_id, state='hidden')
        self.background.itemconfigure(self.back_button_id, state='hidden')
        self.background.itemconfigure(self.clear_settings_button_id, state='hidden')
        self.background.itemconfigure(self.message_label_id, state='hidden')
        for a_flag_radio_button_id in self.list_of_language_radio_buttons_id:
            self.background.itemconfigure(a_flag_radio_button_id, state='hidden')

        self.background_thread_for_the_translator = None
        self.the_translator = None


    def clear_settings(self):
        self.language_1 = None
        self.language_2 = None
        self.message_label.configure(text=Resources.choose_2_languages_to_translate_message)


    def login_action(self):
        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary_for_Logging.get('Login')[0], state='hidden')
        self.background.itemconfigure(self.registry_view_verwalter.buttons_dictionary_for_Registry.get('Registry')[0], state='hidden')

        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary_for_Logging.get('Guest')[0], state='normal')
        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary_for_Logging.get('User')[0], state='normal')


    def login_as_guest_action(self):
        self.login_view_verwalter.login_as_user = False

        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary.get('User')[1], state='hidden')
        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary.get('Guest')[1], state='hidden')

        self.background.itemconfigure(self.login_view_verwalter.input_fields_dictionary.get('Name')[1], state='normal')
        self.background.itemconfigure(self.login_view_verwalter.input_field_labels_dictionary.get('Name')[1], state='normal')

        self.background.itemconfigure(self.login_view_verwalter.buttons_dictionary.get('OK')[1], state='normal')


    def ready_to_roll(self):
        self.background.itemconfigure(self.start_button_id, state='hidden')
        self.background.itemconfigure(self.settings_button_id, state='hidden')
        self.background.itemconfigure(self.back_button_id, state='normal')
        self.background.itemconfigure(self.message_label_id, state='normal')

    def display_settings(self):
        self.background.itemconfigure(self.start_button_id, state='hidden')
        self.background.itemconfigure(self.settings_button_id, state='hidden')
        self.background.itemconfigure(self.save_settings_button_id, state='normal')
        self.background.itemconfigure(self.back_button_id, state='normal')
        self.background.itemconfigure(self.clear_settings_button_id, state='normal')
        for a_flag_radio_button_id in self.list_of_language_radio_buttons_id:
            self.background.itemconfigure(a_flag_radio_button_id, state='normal')
        if self.language_1 == None:
            if self.language_2 == None:
                self.message_label.configure(text=Resources.choose_2_languages_to_translate_message)
            else:
                self.message_label.configure(text='1 Language was set: ' + self.language_2 + '\nChoose the other language then hit "Save"')
        else:
            if self.language_2 == None:
                self.message_label.configure(text='1 Language was set: ' + self.language_1 + '\nChoose the other language then hit "Save"')
            else:
                self.message_label.configure(text='All 2 languages were set: ' + self.language_1 + ' + ' + self.language_2
                                             + '\nHit "Clear" for reconfiguring and "Save", if any')
        self.background.itemconfigure(self.message_label_id, state='normal')

    def user_already_exists_action(self):
        pass

    def display_account(self):
        pass

app = Main_App()
app.set_up()
app.start()



