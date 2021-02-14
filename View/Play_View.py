class Play_View(Parent_of_Views):

    def __init__(self, background):
        super().__init__(background)

        self.instantiate_the_buttons()

        self.user_profile_picture = None      # The user profile picture!


    def instantiate_the_buttons(self):
        start_button = Button(self.background, text='Start', command=self.boss.ready_to_roll) # Start Button
        start_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary(start_button)
  
        back_button = Button(self.background, text='Back', command=self.boss.back_action_play_view)   # Back Button
        back_button['font'] = font.Font(size=Resources.size_of_text_in_buttons)
        self.registrate_a_button_into_buttons_dictionary(back_button)

        