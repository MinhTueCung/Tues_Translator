from threading import Thread
import time
from Resources import Resources

class Background_Thread_for_the_Translator(Thread):
    def __init__(self, the_translator):
        super().__init__()
        self.the_translator = the_translator
        self.on_off_boolean_switch_for_this_thread = False
        self.daemon = True # Do not let this thread keep the main program from exiting

    def run(self):
        while self.on_off_boolean_switch_for_this_thread:
            a_boolean = True
            while a_boolean and self.on_off_boolean_switch_for_this_thread:
                input_language_recorded = self.the_translator.request_for_input_language()
                time.sleep(0.05)
                if input_language_recorded:
                    a_boolean = False

            input_text = self.the_translator.take_input()
            time.sleep(0.05)
            translated_input_text = self.the_translator.translate(input_text)
            time.sleep(0.05)
            if len(translated_input_text) > 0:
                self.the_translator.speak_output_out_loud(translated_input_text, Resources.supported_languages_their_encodings_dictionary.get(self.the_translator.temporary_output_language))
            time.sleep(0.2)

    def switch_this_thread_on(self):
        self.on_off_boolean_switch_for_this_thread = True

    def switch_this_thread_off(self):
        self.on_off_boolean_switch_for_this_thread = False