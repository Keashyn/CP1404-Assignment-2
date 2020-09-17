"""
Name: Keashyn Naidoo
Date: 19 September 2020
Brief Project Description: An application that tracks places that a user has visited or unvisited
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-Keashyn-naidoo
"""
"""Create your main program in this file, using the TravelTrackerApp class"""
from place import Place

"""This is for importing the place file"""
from kivy.app import App

"""This is for importing kivy to build the app"""
from kivy.lang import Builder

""""This is for importing kivy to build the app"""
from kivy.uix.button import Button

"""This is for importing kivy to use the button for the app"""
from kivy.properties import StringProperty

"""THis is for importing kivy so that the spinner is showing string property"""
from kivy.properties import ListProperty

"""This is for importing kivy so that the spinner is displaying a drop down menu"""
OPTIONS = {'Unvisited' : 4, 'Visited' : 3, 'Priority' : 2, 'Country' : 1, 'City' : 1}
"""This is a dictionary that is used for choosing from the user preferences"""
VISITED_COLOR = (1.0, 0.0, 0.0, 1.0)
"""Constant value for visited color"""
UNVISITED_COLOR = (2.0, 1.0, 0.0, 0.5)
"""Constant value for unvisited color"""


class TravelTracker (App, Place) :


if __name__ == "__main__" :
    TravelTracker().run ()
