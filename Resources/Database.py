import mysql.connector as sql

class Database():
    def __init__(self):
        self.the_database = sql.connect(
            host='localhost',
            user='root',
            passwd='    ',
            database='   '
        )
        self.cursor = self.the_database.cursor()

    def create_table(self, table_name, all_entries_and_their_data_types_list):
        if self.table_already_exists(table_name):
            print("This table already exists! Choose another name for the table if you don't want to edit this table")
        else:
            i = 0
            add_table_order_string = 'CREATE TABLE ' + table_name + ' ('
            while i < len(all_entries_and_their_data_types_list):
                add_table_order_string += all_entries_and_their_data_types_list[i] + ' ' + all_entries_and_their_data_types_list[i + 1]
                i += 2
                if i < len(all_entries_and_their_data_types_list):
                    add_table_order_string += ', '
            add_table_order_string += ')'
            self.cursor.execute(add_table_order_string)

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