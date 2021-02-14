# Each "X_View" will get their own "Controller". While the "X_View" takes care of the Front-End (Beauty), the Controller
# takes care of the functions in background, and is therefore a servant of the "main.py" App
from Resources import Resources
import tkinter as tk

class Account_View_Controller(Parent_of_Controllers):

    def __init__(self, boss_app, account_view, database):
        super().__init__(boss_app, account_view, database)

    
    # Unter Entwicklung!
    def show_account_action(self):
        # The button "Account" is only on when the user is already logged in!
        # Therefore --> This user´s identity will be saved in the "main.py" (ultimate boss)
        # Ask this boss to find which account to show
        current_user_id = self.boss.get_current_user()
        # Use database to get account infos of this user
        users_infos_dict = self.database.get_account_infos_of_a_user(Resources.user_profile_table_name, current_user_id)
        # Show these infos on screen (use "Account View")
        # All the input fields of "Account_View" are Entries
        # Show the name
        name = users_infos_dict.get(Resources.user_profile_table_username_column)
        the_name_entry_and_its_ID_on_screen_list = self.view.get_input_fields_dict.get('Name')
        the_name_entry_and_its_ID_on_screen_list[0].delete(0, tk.END)
        the_name_entry_and_its_ID_on_screen_list[0].insert(0, name)
        self.view.get_background().itemconfigure(the_name_entry_and_its_ID_on_screen_list[1], state='normal')
        # Show the date of birth
        date_of_birth = users_infos_dict.get(Resources.user_profile_table_date_of_birth_column)
        the_date_of_birth_entry_and_its_ID_on_screen_list = self.view.get_input_fields_dict.get(Resources.date_of_birth_keyword)
        the_date_of_birth_entry_and_its_ID_on_screen_list[0].delete(0, tk.END)
        the_date_of_birth_entry_and_its_ID_on_screen_list[0].insert(0, date_of_birth)
        self.view.get_background().itemconfigure(the_date_of_birth_entry_and_its_ID_on_screen_list[1], state='normal')
        # Show the password
        password = users_infos_dict.get(Resources.user_profile_table_password_column)
        the_password_entry_and_its_ID_on_screen_list = self.view.get_input_fields_dict.get(Resources.password_keyword)
        the_password_entry_and_its_ID_on_screen_list[0].delete(0, tk.END)
        the_password_entry_and_its_ID_on_screen_list[0].insert(0, password)
        self.view.get_background().itemconfigure(the_password_entry_and_its_ID_on_screen_list[1], state='normal')

    def edit_account_action(self):
        # "Edit" Button only appears when the current user goes into his/her account settings 
        # --> This action takes place, when the "Account" View is on screen (with profile image, 3 input fields wwith their labels, the 4 Buttons)
        # User has the chance to change his/her password + profile picture
        # Name + Date of Birth, if changed --> new Profile --> invalid !
        # 1. Clear the Account View first
        self.clear_the_account_view() 

        # 2. Show the profile image + "Edit Photo" Button + Password Input Field + Label for configuring!


        # 3. Also show instead "Cancel" + "Save" (for editing the account)
        cancel_button_ID = self.view.get_buttons_dict().get(Resources.cancel_keyword)[1]
        self.view.get_background().itemconfigure(cancel_button_ID, state='normal')
        save_button_ID = self.view.get_buttons_dict().get(Resources.save_keyword)[1]
        self.view.get_background().itemconfigure(save_button_ID, state='normal')


    def delete_account_action(self):
        # "Delete" Button is showed with "Back" + "Edit" Button in Account View
        # 1. Clear the Account View
        self.clear_the_account_view()

        # 2. Show the 2 Yes-No Buttons
        yes_button_ID = self.view.get_buttons_dict().get(Resources.yes_del_keyword)[1]
        self.view.get_background().itemconfigure(yes_button_ID, state='normal')
        no_button_ID = self.view.get_buttons_dict().get(Resources.no_del_keyword)[1]
        self.view.get_background().itemconfigure(no_button_ID, state='normal')

        # 3. Show the warning report (with report_panel from "self.view")


    def change_profile_image(self):
        pass

    def back_action(self):
        # 1. 

    def cancel_action(self):
        pass

    def yes_delete_acc(self):
        pass

    def no_delete_acc(self):
        pass

    def clear_the_account_view(self):
        # This method clears the Account View (View with all the User´s Account Infos listed on screen)
        # 1. Make all the input fields disappear 
        for key, value in self.view.get_input_fields_dict():
            # Also clear the texts in the input fields
            value[0].delete(0, tk.END)
            # Blur the input fields
            self.view.get_background().itemconfigure(value[1], state='hidden')

        # 2. Clear all the associated labels
        for key_la, value_la in self.view.get_labels_dict():
            self.view.get_background().itemconfigure(value_la[1], state='hidden')

        # 3. Clear the profile image!


        # 4. Clear all 4 Buttons: Edit Photo, Back, Delete, Edit
        edit_button_ID = self.view.get_buttons_dict().get(Resources.edit_keyword)[1]
        self.view.get_background().itemconfigure(edit_button_ID, state='hidden')
        back_button_ID = self.view.get_buttons_dict().get(Resources.back_keyword)[1]
        self.view.get_background().itemconfigure(back_button_ID, state='hidden')
        delete_button_ID = self.view.get_buttons_dict().get(Resources.delete_keyword)[1]
        self.view.get_background().itemconfigure(delete_button_ID, state='hidden')
        edit_photo_button_ID = self.view.get_buttons_dict().get(Resources.edit_photo_keyword)[1]
        self.view.get_background().itemconfigure(edit_photo_button_ID, state='hidden')


        

