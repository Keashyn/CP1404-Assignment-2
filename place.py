from placecollection import Placecollection as pc

"""import placecollection classes as name pc that constains all the functions like read data and save data"""


class Place(pc) :
    def __inti__(self) :
        """This method is automatically initialised when place class is called"""
        self.data = [ ]
        """This variable in Place is  used for contain the data that reads  from the csv file."""
        self.new_places = [ ]
        """This variable in  Place  is used for contain correct user input that passed from main and give it to the place collection that will be add later."""
        pc.read(self)
        """This calling method in place collection is  for containing the data from csv file."""

    def mark_places(self, xy) :
        """This method is used for marking place when the button of place has been pressed"""
        x = int(xy) - 1
        """This variable is used to constarate the str to int and since list start from 0 the value will be minus one"""
        if self.sorted_data [ x ] [ 3 ] != "v" :
            """This condition checks if the selected data is visited or not and if  not it will change to visited"""
            self.sorted_data [ x ] [ 3 ] = "v"
            """Changed the value of unvisited to visited"""
            if self.priority_place(x) :
                """This checks if the place is important or not and if its True it will give a different print out in the status bar"""
                self.root.ids.status.text = "You visited {0} in {1}. Great travelling!".format(
                    self.sorted_data [ x ] [ 0 ], self.sorted_data [ x ] [ 1 ])
                """if its important or True it will print this"""
            else :
                self.root.ids.status.text = "You visited {0} in {1}.".format(self.sorted_data [ x ] [ 0 ],
                                                                             self.sorted_data [ x ] [ 1 ])
                """if its important or False it will print this"""
        else :
            """This checks the condition of the selected data that is visited or not and if not it will change to visited """
            self.sorted_data [ x ] [ 3 ] = "n"
            """Changed the value of unvisited to visited"""
            if self.sorted_data(x) :
                """This checks if the place is important or not and if its True it will give a different print out in the status bar"""
                self.root.ids.status.text = "You need to visit {0} in {1}. Get going!".format(
                    self.sorted_data [ x ] [ 0 ], self.sorted_data [ x ] [ 1 ])
                """if its important or True it will print this"""
            else :
                self.root.ids.status.text = "You need to visit {0} in {1}.".format(self.sorted_data [ x ] [ 0 ],
                                                                                   self.sorted_data [ x ] [ 1 ])
                """if its important or False it will print this"""
        self.sorted(self.root.ids.spinners.text)
        """After the place has been marked it will call to be sorted using the function and then sort again after the data list has been modifed"""

    def priority_places(self, x) :
        """This method is used for checking if the priority is important or not"""
        if int(self.sorted_data [ 0 ] [ 2 ]) <= 2 :
            """if the conditions are met it will return True"""
            return True
        else :
            """if its False it will return the False value that will give a different input"""
            return False

    def __str__(self) :
        """This method is used for test place"""
        for x in self.data :
            """This a loop that loops the data"""
            return "{},{},{},{]".format(x [ 3 ], x [ 0 ], x [ 1 ].x [ 2 ])
