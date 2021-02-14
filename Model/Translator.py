from gtts import gTTS
import playsound
import speech_recognition as sr
from Resources import Resources
import random
import os
from googletrans import Translator as GT

class Translator:
    def __init__(self, language_1, language_2, message_label_on_GUI):
        self.language_1 = language_1
        self.language_2 = language_2
        self.temporary_input_language = language_1 # the temporary input language when one talks into the translator
        self.temporary_output_language = language_2 # the temporary, translated to, output language
        self.recognizer = sr.Recognizer()
        self.translator = GT()
        self.message_label_on_GUI = message_label_on_GUI

    def speak_output_out_loud(self, text_string, output_language):
        tts = gTTS(text=text_string, lang=output_language, slow=False)
        a_random_number = random.randint(1, 10000000)
        audio_file_name = 'audio-' + str(a_random_number) + '.mp3'
        tts.save(audio_file_name)
        self.message_label_on_GUI.configure(text=text_string)
        playsound.playsound(audio_file_name)
        os.remove(audio_file_name)

    def request_for_input_language(self):
        input_language_understood_and_recorded = False
        with sr.Microphone(sample_rate=16000) as source:
            self.message_label_on_GUI.configure(text=Resources.ask_for_the_input_language_message)
            audio = self.recognizer.record(source, duration=2.5)

            print("Has recorded something!")

            try:
                voice_data = self.recognizer.recognize_google(audio)

                print("Voice data from 'request input language': " + voice_data)

                if self.language_1 in voice_data:
                    self.speak_output_out_loud(self.language_1 + ' detected! Please say something!', Resources.supported_languages_their_encodings_dictionary.get('English'))
                    self.temporary_input_language = self.language_1
                    self.temporary_output_language = self.language_2
                    input_language_understood_and_recorded = True
                elif self.language_2 in voice_data:
                    self.speak_output_out_loud(self.language_2 + ' detected! Please say something!', Resources.supported_languages_their_encodings_dictionary.get('English'))
                    self.temporary_input_language = self.language_2
                    self.temporary_output_language = self.language_1
                    input_language_understood_and_recorded = True
                else:
                    self.speak_output_out_loud(Resources.language_not_match_settings_message, Resources.supported_languages_their_encodings_dictionary.get('English'))

            except sr.UnknownValueError:
                self.speak_output_out_loud(Resources.incomprehensible_input_message, Resources.supported_languages_their_encodings_dictionary.get('English'))

            except sr.RequestError:
                self.speak_output_out_loud(Resources.system_defected_message, Resources.supported_languages_their_encodings_dictionary.get('English'))

        return input_language_understood_and_recorded


    def take_input(self):
        with sr.Microphone(sample_rate=16000) as source:
            audio = self.recognizer.record(source, duration=8)
            input_text = ''
            try:
                voice_data = self.recognizer.recognize_google(audio, language=Resources.supported_languages_their_encodings_dictionary.get(self.temporary_input_language))

                print(voice_data)
                self.message_label_on_GUI.configure(text='Recorded: ' + voice_data)

                input_text = voice_data
            except sr.UnknownValueError:
                print('UnknownValueError in "take_input()"')
                self.message_label_on_GUI.configure(text='???')
                input_text = ''
            except sr.RequestError:
                print('RequestError in "take_input()"')
                self.message_label_on_GUI.configure(text='???')
                input_text = ''

        return input_text

    def translate(self, input_text):
        translated_input_text = ''
        if len(input_text) > 0:

            print('Input_text to Translate: ' + input_text);

            text_to_translate = self.translator.translate(input_text, src=Resources.supported_languages_their_encodings_dictionary.get(self.temporary_input_language), dest=Resources.supported_languages_their_encodings_dictionary.get(self.temporary_output_language))
            translated_input_text = text_to_translate.text

        return translated_input_text



