import mysql.connector as sql
import Resources

class Database():
    def __init__(self):
        self.the_database = sql.connect(
            host='localhost',
            user='root',
            passwd='EDITH1609',
            database='database_for_tues_translator'
        )
        self.cursor = self.the_database.cursor()


    def create_table(self, table_name, all_entries_and_their_data_types_list, primary_key_entry, foreign_keys_their_reference_tables_and_keys_dict):
        # This method creates a new table with entries and their datatypes, with 1 primary key and 1...* foreign keys, if needed
        # If primary key, or foreign keys are not needed --> pass "None"
        # The foreign keys are passed as a dictionary; dictionary´s key = foreign key, dictionary´s value = a list with [reference_table, reference_column]
        if self.table_already_exists(table_name):
            print("This table already exists! Choose another name for the table if you don't want to edit this table")
        else:
            # First registrate all the entries and their datatypes into the sql query
            add_table_string_order = 'CREATE TABLE ' + table_name + ' (' 
            i = 0
            while i < len(all_entries_and_their_data_types_list):
                add_table_order_string += all_entries_and_their_data_types_list[i] + ' ' + all_entries_and_their_data_types_list[i + 1]
                i += 2
                if i < len(all_entries_and_their_data_types_list):
                    add_table_order_string += ', '
            # Now check if a primary key is needed 
            if primary_key_entry != None:
                # then add the primary key 
                add_table_order_string += ', '
                primary_key_string = 'PRIMARY KEY (' + primary_key_entry + ')'
                add_table_order_string += primary_key_string
            # Now check if foreign keys are also needed
            if foreign_keys_their_reference_tables_and_keys_dict != None
                # then add these foreign keys
                # Loop through all these "to add" keys
                for key in foreign_keys_their_reference_tables_and_keys_dict:
                    add_table_order_string += ', '
                    a_foreign_key_string = 'FOREIGN KEY (' + key + ') REFERENCES '
                    reference_table_with_the_reference_column_string = foreign_keys_their_reference_tables_and_keys_dict[key][0] + '(' 
                                                                + foreign_keys_their_reference_tables_and_keys_dict[key][1] + ')'
                    a_foreign_key_string += reference_table_with_the_reference_column_string
                    add_table_order_string += a_foreign_key_string

            # Close the sql query string
            add_table_order_string += ')'
            # Execute the sql string query
            self.cursor.execute(add_table_order_string)
            self.the_database.commit()



    def insert_item_into_a_table(self, table_name, list_of_tuples_of_column_name_and_its_to_insert_item):
        if self.table_already_exists(table_name):
            insert_order_string = 'INSERT INTO ' + table_name + ' ('
            index = 0
            while index < len(list_of_tuples_of_column_name_and_its_to_insert_item):
                insert_order_string += list_of_tuples_of_column_name_and_its_to_insert_item[index][0]
                index += 1
                if index < len(list_of_tuples_of_column_name_and_its_to_insert_item):
                    insert_order_string += ', '
            insert_order_string += ') VALUES ('
            index = 0
            while index < len(list_of_tuples_of_column_name_and_its_to_insert_item):
                insert_order_string += '%s'
                index += 1
                if index < len(list_of_tuples_of_column_name_and_its_to_insert_item):
                    insert_order_string += ','
            insert_order_string += ')'
            list_of_to_insert_items = []
            for a_tuple_of_column_name_and_its_to_insert_item in list_of_tuples_of_column_name_and_its_to_insert_item:
                list_of_to_insert_items.append(a_tuple_of_column_name_and_its_to_insert_item[1])
            tuple_of_to_insert_items = tuple(list_of_to_insert_items)
            self.cursor.execute(insert_order_string, tuple_of_to_insert_items)
            self.the_database.commit()
        else:
            print('This table does not exist yet!')

    def print_all_the_items_in_a_table(self, table_name):
        print_order_string = 'SELECT * FROM ' + table_name
        self.cursor.execute(print_order_string)
        for x in self.cursor:
            print(x)

    def add_a_new_entry_to_a_table(self, table_name, entry_name, datatype):
        if self.table_already_exists(table_name):
            order_string = 'ALTER TABLE ' + table_name + ' ADD COLUMN ' + entry_name + ' ' + datatype
            self.cursor.execute(order_string)
        else:
            print('This table does not exist yet!')

    def delete_an_entry_in_a_table(self, table_name, entry_name):
        if self.table_already_exists(table_name):
            order_string = 'ALTER TABLE ' + table_name + ' DROP ' + entry_name
            self.cursor.execute(order_string)
        else:
            print('This table does not exist yet!')

    def change_the_name_of_an_entry_in_a_table(self, table_name, entry_previous_name, entry_new_name, entry_new_datatype):
        if self.table_already_exists(table_name):
            order_string = 'ALTER TABLE ' + table_name + ' CHANGE ' + entry_previous_name + ' ' + entry_new_name + ' ' + entry_new_datatype
            self.cursor.execute(order_string)
        else:
            print('This table does not exist yet!')

    def describe_table(self, table_name):
        if self.table_already_exists(table_name):
            describe_table_order_string = 'DESCRIBE ' + table_name
            self.cursor.execute(describe_table_order_string)
            for an_entry in self.cursor:
                print(an_entry)
        else:
            print('This table does not exist yet!')

    def table_already_exists(self, table_name):
        a_boolean = False
        SQL_order = """SHOW TABLES"""
        self.cursor.execute(SQL_order)
        list_of_all_tables_in_form_of_tuple = self.cursor.fetchall()
        list_of_all_table_names = [one_table_tuple[0] for one_table_tuple in list_of_all_tables_in_form_of_tuple]  # Conversion to list of str
        if table_name in list_of_all_table_names:
            a_boolean = True
        return a_boolean

    def delete_a_table(self, table_name):
        if self.table_already_exists(table_name):
            order_string = 'DROP TABLE ' + table_name
            self.cursor.execute(order_string)
        else:
            print("The table didn´t exist in the first place")

    def search_for_an_user(self, table_name, username, date_of_birth, password):
        if self.table_already_exists(table_name):
            b = False  # Boolean Search Result
            # First search for the username
            SQL_order = "SELECT * FROM %s WHERE %s LIKE %s" % (table_name, Resources.user_profile_table_username_column, username)
            self.cursor.execute(SQL_order)
            list_of_rows_found = self.cursor.fetchAll()
            if len(list_of_rows_found) == 0:
                b = False
            else:
                for row in list_of_rows_found:
                    # Now that the username is similar: check whether date of birth + password also similar --> User found!
                    index_of_date_of_birth_column = Resources.column_names_and_their_index_number_dict_of_user_profile_table.get(Resources.user_profile_table_date_of_birth_column)
                    index_of_password_column = Resources.column_names_and_their_index_number_dict_of_user_profile_table.get(Resources.user_profile_table_password_column)
                    if row[index_of_date_of_birth_column] == date_of_birth:
                        # 2 Dates of birth are identical, check for the password
                        if row[iindex_of_password_columnn] == password
                            # User found! Cut the loop!
                            b = True
                            break
            return b
                
        else:
            print('This table does not exist yet!')
            return False

    def get_account_infos_of_a_user(self, table_name, userID):
        if self.table_already_exists(table_name):
            # The "Users' Profiles" Table contains Account Infos of every registrated users
            # Each user gets a unique ID. We´ll use this ID to get the user´s account infos
            # Returns user´s infos: Name, Date of Birth, Password in the form of a dictionary
            sql_query_string = 'SELECT * FROM ' + table_name + ' WHERE ' + Resources.user_profile_table_userID_column + ' LIKE ' + userID
            self.cursor.execute(sql_query_string)
            list_of_rows_found = self.cursor.fetchAll()
            # There should only be one result, due to the unique ID + the user must already be logged in to click the "Account" Button
            # (See "Account View Controller")
            index_of_name_column = Resources.column_names_and_their_index_number_dict_of_user_profile_table.get(Resources.user_profile_table_username_column)
            index_of_date_of_birth_column = Resources.column_names_and_their_index_number_dict_of_user_profile_table.get(Resources.user_profile_table_date_of_birth_column)
            index_of_password_column = Resources.column_names_and_their_index_number_dict_of_user_profile_table.get(Resources.user_profile_table_password_column)
            
            the_infos_dictionary = {}
            # The User´s name
            the_infos_dictionary[Resources.user_profile_table_username_column] = list_of_rows_found[0][index_of_name_column]
            # The date of birth 
            the_infos_dictionary[Resources.user_profile_table_date_of_birth_column] = list_of_rows_found[0][index_of_date_of_birth_column]
            # The password
            the_infos_dictionary[Resources.user_profile_table_password_column] = list_of_rows_found[0][index_of_password_column]

            return the_infos_dictionary
        else:
            print('This table does not exist yet!')
            return None

    def delete_an_user_profile(self, userID):
        # This method will delete an user profile, completely, in all 3 tables (Users' Profiles, Users' Profile Picture, Languages Profiles)
        # We don´t have to check whether the account exists or not, because "Delete" Account Button only appears in the "Account Profile" View
        sql_query_string_1 = 'DELETE FROM ' + Resources.user_profile_table_name + ' WHERE ' + Resources.userID_column + ' = ' + userID
        sql_query_string_2 = 'DELETE FROM ' + Resources.user_pictures_table_name + ' WHERE ' + Resources.userID_column + ' = ' + userID
        sql_query_string_3 = 'DELETE FROM ' + Resources.language_profile_table_name + ' WHERE ' + Resources.userID_column + ' = ' + userID

        self.cursor.execute(sql_query_string_1)
        self.cursor.execute(sql_query_string_2)
        self.cursor.execute(sql_query_string_3)


    # Unter Entwicklung!
    def create_an_user_profile(self, username, date_of_birth, password, profile_picture_link):
        search_for_the_user_result = self.database.search_for_an_user(Resources.user_profile_table_name, username, date_of_birth, password)
        if(search_for_the_user_result): 
            # User already exists
            self.boss_app.user_already_exists_action()
        else:
            # User doesn´t exist yet! Create profile
            entry_list_of_tuples = []
            username_tuple = (Resources.user_profile_table_username_column, username)
            date_of_birth_tuple = (Resources.user_profile_table_date_of_birth_column, date_of_birth)
            password_tuple = (Resources.user_profile_table_password_column, password)
            entry_list_of_tuples.extend(username_tuple, date_of_birth_tuple, password_tuple)
            # First add these Infos into the "Users´ Profile" Table
            self.databasse.insert_item_into_a_table(Resources.user_profile_table_name, entry_list_of_tuples)
            # Then add the profile picture local link to the table "Users´ Pictures"
            # Just store the link! The image itself is saved in a special directory