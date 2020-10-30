from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from Resources import Resources
from Model.Translator import Translator
from Model.Background_Thread_for_the_Translator import Background_Thread_for_the_Translator
from Resources.Database import Database

class Main_App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tue´s Translator")

        self.background = Canvas(self.root, width=Resources.canvas_background_on_gui_width, height=Resources.canvas_background_on_gui_height)

        self.background_jarvis_photo = ImageTk.PhotoImage(
            Image.open('Resources/jarvis.jpg'))

        self.start_button = Button(self.background, text='Start', command=self.build_the_Translator_and_start_having_fun)
        self.start_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)

        self.settings_button = Button(self.background, text='Settings', command=self.display_settings)
        self.settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)

        self.save_settings_button = Button(self.background, text='Save', command=self.save_settings)
        self.save_settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)

        self.back_button = Button(self.background, text='Back', command=self.back_action)
        self.back_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)

        self.clear_settings_button = Button(self.background, text='Clear', command=self.clear_settings)
        self.clear_settings_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)

        self.message_label = Label(self.background, text='Nothing yet', fg='brown', font=font.Font(size=17))

        self.language_1 = Resources.supported_languages_dictionary.get(1) # English as 1st default
        self.language_2 = Resources.supported_languages_dictionary.get(6) # Vietnamese as 2nd default

        self.the_translator = None
        self.background_thread_for_the_translator = None

    def start(self):
        self.background.pack()
        self.root.mainloop()

    def set_up(self):
        self.background.create_image(0, 0, image=self.background_jarvis_photo, anchor=NW)
        self.start_button_id = self.background.create_window(90, 100, width=Resources.standard_width_of_a_button,
                                      height=Resources.standard_height_of_a_button, window=self.start_button)
        self.settings_button_id = self.background.create_window(580, 100, width=Resources.standard_width_of_a_button,
                                      height=Resources.standard_height_of_a_button, window=self.settings_button)
        self.save_settings_button_id = self.background.create_window(580, 550, width=Resources.standard_width_of_a_button,
                                      height=Resources.standard_height_of_a_button, window=self.save_settings_button)
        self.back_button_id = self.background.create_window(90, 550, width=Resources.standard_width_of_a_button,
                                      height=Resources.standard_height_of_a_button, window=self.back_button)
        self.clear_settings_button_id = self.background.create_window(580, 450, width=Resources.standard_width_of_a_button,
                                      height=Resources.standard_height_of_a_button, window=self.clear_settings_button)
        self.message_label_id = self.background.create_window(335, 60, width=630,
                                      height=80, window=self.message_label)
        self.list_of_language_radio_buttons_id = []
        self.list_of_language_associated_pictures = []
        self.int_value_radio_choose = IntVar()
        self.int_value_radio_choose.set('1')

        x = 0
        # Create the first half of the buttons on the left side of the screen
        while x < int(len(Resources.supported_languages_dictionary) / 2):
            a_radio_button = Radiobutton(self.background, variable=self.int_value_radio_choose, value=x + 1)
            associated_image = ImageTk.PhotoImage(
                Image.open(
                    'Resources/' + Resources.supported_languages_dictionary.get(
                        x + 1) + '.jpg'))
            self.list_of_language_associated_pictures.append(associated_image)
            a_radio_button.config(image=associated_image)
            a_radio_button_id = self.background.create_window(230, x * 75 + 170, window=a_radio_button)
            self.list_of_language_radio_buttons_id.append(a_radio_button_id)
            x += 1

        # Create the second half on the right side of the screen
        while x < len(Resources.supported_languages_dictionary):
            a_radio_button = Radiobutton(self.background, variable=self.int_value_radio_choose, value=x + 1)
            associated_image = ImageTk.PhotoImage(
                Image.open(
                    'Resources/' + Resources.supported_languages_dictionary.get(
                        x + 1) + '.jpg'))
            self.list_of_language_associated_pictures.append(associated_image)
            a_radio_button.config(image=associated_image)
            a_radio_button_id = self.background.create_window(440, (x - int(len(Resources.supported_languages_dictionary) / 2)) * 75 + 170, window=a_radio_button)
            self.list_of_language_radio_buttons_id.append(a_radio_button_id)
            x += 1

        self.background.itemconfigure(self.message_label_id, state='hidden')
        self.background.itemconfigure(self.save_settings_button_id, state='hidden')
        self.background.itemconfigure(self.back_button_id, state='hidden')
        self.background.itemconfigure(self.clear_settings_button_id, state='hidden')
        for a_flag_radio_button_id in self.list_of_language_radio_buttons_id:
            self.background.itemconfigure(a_flag_radio_button_id, state='hidden')

    def build_the_Translator_and_start_having_fun(self):
        self.background.itemconfigure(self.start_button_id, state='hidden')
        self.background.itemconfigure(self.settings_button_id, state='hidden')
        self.background.itemconfigure(self.back_button_id, state='normal')
        self.background.itemconfigure(self.message_label_id, state='normal')
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

    def clear_settings(self):
        self.language_1 = None
        self.language_2 = None
        self.message_label.configure(text=Resources.choose_2_languages_to_translate_message)


app = Main_App()
app.set_up()
app.start()



