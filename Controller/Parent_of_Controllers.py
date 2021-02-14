# This class defines the skeleton of all "Controllers" (for the UI "X_View"), which are responsible for all the "functional"
# sides of the "Views". All the Controllers work under the reign of "main.py" (Main-App)
# The "View" is introduced to the Controller right at the moment of the Controller´s instantiation
# Every Controller must be able to communicate with the database, to get and to store informations

class Parent_of_Controllers:

    def __init__(self, boss_app, its_view, database):
        self.boss = boss_app
        self.view = its_view
        self.database = database

    
