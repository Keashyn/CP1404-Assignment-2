import csv
"""import csv library in order to read the csv file called places.csv"""
name="places.csv"
"""Constant value for showing the name of the file"""
class PlaceCollection():
    def read(self):
        """This method is used for adding data to the list of data that is being stored in the csv file"""
        with open(name,mode='r')as file:
            """This function opens the file but in read mode only"""
            reader =csv.reader(file)
            """Use the csv function to import the above so that it can read the file"""
            for row in reader:
                """This loop is used for to read the data in the csv file that is based on each line"""
                self.data.append(list(row))
                """The data in each line from the csv file will be added in a data variable"""
        file.close()
        """This function is used when closing files that has been open"""
    def sort(self,sort_by):
        """This method is used for sorting the data that has been already read based on the user choose"""
        """Each choice is already set in dictionary in main file for example: sort by visited function which means that sort by value of 3"""
        if sort_by==0:
            """Sort by City name"""
            self.sorted_data=sorted(self.data,reverse=False,key=lambda row:(row[0],int(row[2])))
            """This variable is for containing the sorted data based on user choice"""
        elif sort_by==1:
            """Sort by Country name"""
            self.sorted_data=sorted(self.data,reverse=False,key=lambda row:(row[1],int(row[2])))
            """This variable is for containing the sorted data based on user choice"""
        elif sort_by==2:
            """"Sort by Priority"""
            self.sorted_data=sorted(self.data,reverse=False,key=lambda row:(int(row[2])))
            """This variable is for containing the sorted data based on user choice"""
        elif sort_by==3:
            """Sort by Visited places"""
            self.sorted_data=sorted(self.data,reverse=False,key=lambda row:(row[3],int(row[2])))
            """This variable is for containing the sorted data based on user choice"""
        elif sort_by==4:
            """Sort by Unvisited places"""
            self.sorted_data=sorted(self.data,reverse=True,key=lambda row:(row[3],int(row[2])))
            """This variable is for containing the sorted data based on user choice [THis one is same as number 3 with special occasion to reverse the value]"""
    def add(self):
        """This method is used for adding places to the data based on user input"""
        self.new_places.append('n')
        """This append function is used to add fixed value for the new places that are unvisited"""
        self.data.append(self.new_places)
        """After all files have been checked and is True it will append or add data to the main data list"""
    def save(self):
        """This method is used for saving data to the list of data that have been modified at the in the on_stop application"""
        with open(name,mode='w',newline="")as file:
            """This function opens the file but in write mode only"""
            writer=csv.writer(file)
            """Use the csv function to import the above so that it can read the file"""
            for row in self.sorted_data:
                """This loop  used to read the data in the csv file that is based on each line and add them one bye one that has been sorted"""
                writer.writerow(row)
                """This writes the list of data in the file"""
        file.close()
        """This function is used when closing files that has been open"""
    def visit_places(self):
        """"The function to count unvisited places and keep track of unvisited places"""
        count_visit=0
        """Variable to make 0 value at start and will be added if the loop data show visit."""
        for row in self.data:
            """This loop is used for reading the data inside the data list"""
            if row[3] == "n":
                """The conditions in data that gets from the data list for checking if its unvisited"""
                count_visit += 1
                """if the conditions are met the variable count_visit is added by 1"""
        return count_visit
        """After the loop ends it will return unvisited places"""
    def check_number(self,user_input):
        """This method is used for checking if there is a number in the user input"""
        data = list(user_input)
        """The data gotten from the user input will be putted into the list"""
        counter = 0
        """This variable is used for counting how many numbers"""
        for i in data:
            """loops for checking  if its a digit or not"""
            x = i.isdigit()
            """With this function it will check if its digit or not"""
            if x:
                """"if its results True it will add the value of count 1"""
                counter += 1
            else:
                """else it will keep the value of the counter"""
                counter = counter
        if counter > 0:
            """if counter is more than 0 or there is number in the user input it will results to False"""
            return False
        else:
            """else if there is no number it will return True and passes the values"""
            return True
    def check_symbol(self,user_input):
        """This method is used for checking  if there is symbol in the user input"""
        data = list(user_input)
        """The data gotten from the user input will be putted  into the list"""
        counter = 0
        """This variable is used for counting how many symbols"""
        for i in data:
            """This loop is used  for checking  if its include with symbol or not"""
            SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
            if i in SPECIAL_CHARACTERS:
                """With this loop it will check every data if its included with the symbol or not , if so it will add counter with 1"""
                counter += 1
            else:
                """else it will keep the value of the counter"""
                counter = counter
        if counter > 0:
            """if counter is more than 0 or there is symbol in the user input it will results to False"""
            return False
        else:
            """else if there is no number it will return True and passess the values"""
            return True
    def priority_check(self, user_input):
        """This method is used for checking the  priority_check inputted by the user"""
        try:
            if int(user_input) <= 0:
                """First its try to check the user_input if its valid which means positive numbers"""
                self.root.ids.status.text = "Priority us be > 0"
                """if it is  it will return the text in status bar in application"""
            elif user_input == "":
                """First its try to check the user_input if its valid which its not empty"""
                self.root.ids.status.text = "All fields must be completed"
                """if it is it will return the text in status bar in application"""
            else:
                return int(user_input)
                """if all conditions are met and there is no error it will returning the user_input"""
        except ValueError:
            """With this except it will check and prevent error of the program if user not inputting integer data types"""
            if user_input == "":
                """First its try to check the user_input if its valid which its not empty"""
                self.root.ids.status.text = "All fields must be completed"
                """if it is it will return the text in status bar in application"""
            else:
                """if users put wrong number mixed with text it will show this"""
                self.root.ids.status.text = "Please enter a valid number"
                """if it is it will return the text in status bar in application"""
    def error_check(self, checking):
        """This method is used for checking  the user_input in city and country that has been inputted by the user"""
        if checking == "":
            """First its try to check the user_input if its valid which its not empty"""
            self.root.ids.status.text = "All field must be completed"
            """if it is it will return the text in status bar in application"""
        elif not self.check_number(checking):
            """This will call the method for checking  if the value consist number or not. if its true then it will ask for input in the correct name"""
            self.root.ids.status.text = "Please input correct name"
            """if it is it will return the text in status bar in application"""
        elif not self.check_symbol(checking):
            """This will call the method for checking  if the value consist number or not. if its true then it will ask for input in the correct name"""
            self.root.ids.status.text = "Please input correct name"
            """if it is it will return the text in status bar in application"""
        else:
            return checking.capitalize()
            """This returns the  value after every error check have been fulfilled and to make sure that is sorted in the correct way and the  user input has been capitalized"""