"""
Name: Keashyn Naidoo
Date: 19 September 2020
Brief Project Description: An application that tracks places that a user has visited or unvisited
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-Keashyn-naidoo
"""
"""Create your main program in this file, using the TravelTrackerApp class"""

from place import Place

"""This for importing place class"""
from kivy.app import App

"""This for importing kivy for building the app"""
from kivy.lang import Builder

"""This for importing kivy for building the app"""
from kivy.uix.button import Button

"""This for importing kivy for give button"""
from kivy.properties import StringProperty

"""This for importing kivy for spinner showing string property"""
from kivy.properties import ListProperty

"""This for importing kivy for spinner that will display spinner like dropdown menu"""

OPTIONS = {'Unvisited' : 4, 'Visited' : 3, 'Priority' : 2, 'Country' : 1, 'City' : 0}
"""This dictionary is used for choice and sorting from user preferences"""
VISITED_COLOR = (2.0, 1.0, 0.0, 0.5)
"""Constant value for visited color"""
UNVISITED_COLOR = (1.0, 0.0, 0.0, 1.0)
"""Constant value for unvisited color"""


class TravelTracker (App, Place) :
    current_sort = StringProperty ( )
    """This variable is used for defining first that it will give string property"""
    sort_options = ListProperty ( )
    """This variable is used for defining first that it will resulting list property"""

    def on_stop(self) :
        """This method is used when users quit the app or the app stopped it will run the functions below which is saving the data"""
        Place.save (self)
        """Calling method from place class to save the data list to the data"""

    def show_place(self) :
        """This method is used for displaying the place from the data list"""
        id_count = 0
        """This variable is used for defining each button ids"""
        for a in self.sorted_data :
            """loop for making  sure that all the data list is read and is already sorted"""
            id_count = id_count + 1
            """The variable will be add each loop for giving each place different ids"""
            if a [ 3 ] == "n" :
                """Conditions to check if its unvisited or visited to give different color"""
                entries_box = Button (
                    id=str (id_count),
                    text="{0} in {1}, priority {2}".format (a [ 0 ], a [ 1 ], a [ 2 ]),
                    background_color=UNVISITED_COLOR,
                    on_press=lambda x : Place.mark_place (self, x.id))
                self.root.ids.entries_box.add_widget (entries_box)
            else :
                """Conditions to check if its unvisited or visited to give different color"""
                entries_box = Button (
                    id=str (id_count),
                    text="{0} in {1}, priority {2} (visited)".format (a [ 0 ], a [ 1 ], a [ 2 ]),
                    background_color=VISITED_COLOR,
                    on_press=lambda x : Place.mark_place (self, x.id))
                self.root.ids.entries_box.add_widget (entries_box)

    def sorted(self, sort_choice) :
        """This method is used for sorting based on users choice"""
        self.root.ids.entries_box.clear_widgets ( )
        """To make sure the same button is created the widget will be cleared"""
        Place.sort (self, OPTIONS [ sort_choice ])
        """It will call Place method for sorting based on the choice in the dictionary"""
        self.show_place ( )
        """This method is used for showing the place based on the data in button widget form after its being cleared"""
        self.root.ids.visit.text = "Place to visist: " + str (Place.visit_place (self))
        """After it will be sorted it will show the place needed to visit"""

    def build(self) :
        """This method is used for building the kivy apps"""
        self.title = "Travel Tracker"
        """This is used for showing the title of the app based which is Travel Tracker"""
        self.root = Builder.load_file ('App.kv')
        """This is used for loading the template of the kivy app"""
        self.sort_options = sorted (OPTIONS.keys ( ), reverse=True)
        """This is used to display the dictionary of choice in reverse"""
        self.current_sort = self.sort_options [ 0 ]
        """This is used for automatically sort the default by first options sort"""
        return self.root
        """It will return the application in kivy template that made before"""

    def clear_text(self) :
        """This method is used for clearing the text input and status bar that will be used after add place and press clear button"""
        self.root.ids.city_name.text = ""
        """Change city name text editor value or clear it"""
        self.root.ids.country_name.text = ""
        """Change country name text editor value or clear it"""
        self.root.ids.priority_num.text = ""
        """Change priority text editor value or clear it"""
        self.root.ids.status.text = ""
        """Change status name text editor value or clear it"""

    def add(self) :
        """This method is used for adding new places and pass value from the app to place collections"""
        have_error = False
        """Variable to check if its have an error or not"""
        count = 0
        """Variable to help check if there is an error"""
        self.new_place.append (Place.error_check (self, self.root.ids.city_name.text))
        """It will be append the value in text editor  and check if its true it will return the value , else will return None"""
        self.new_place.append (Place.error_check (self, self.root.ids.country_name.text))
        """It will be append the value in text editor  and check if its true it will return the value , else will return None"""
        self.new_place.append (Place.priority_check (self, self.root.ids.priority_num.text))
        """It will be append the value in text editor  and check if its true it will return the value , else will return None"""
        for xyt in self.new_place :
            """Loop for read through the new place to check if there is none value"""
            if xyt == None :
                """Condition to check if its None value it will increase the value of count by one"""
                count += 1
            else :
                """else will be return its self"""
                count = count
        if count > 0 :
            """Conditions to check if the count is more than 0 it will return true which mean have an error in the text editor"""
            have_error = True
        if not have_error :
            """Conditon to check if its False or means not having any error"""
            Place.add (self)
            """Calling the method from add to add more value and add the new place in data list"""
            self.clear_text ( )
            """Calling the method for clear the text editor and status bar"""
            self.root.ids.status.text = (
                "{0} in {1} priority {2} added".format (self.new_place [ 0 ], self.new_place [ 1 ], self.new_place [
                    2 ]))
            """This will displaying tht the place is added in status bar"""
            self.new_place = [ ]
            """To make sure its not double input , the variable will be replaced to nothing"""
            self.sorted (self.root.ids.spinners.text)
            """Ater the new button is added i make sure to sort the button backs"""
        else :
            """If conditions not met to make sure the value is empty not containing the none value the variable will be replaced to nothing"""
            self.new_place = [ ]


if __name__ == "__main__" :
    TravelTracker ( ).run ( )
    """To make sure it will run the applications by calling the class and . run() and make sure kivy is already imported"""
