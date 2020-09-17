"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests() :
    """Test Place class."""

    # Test empty place (defaults)
    print ("Test empty place:")
    default_place = Place ( )
    print (default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print ("Test initial-value place:")
    new_place = Place ("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    print ("Test aleranate method for marking visited places")
    """This is the visited value that has changed from boolean to str; oupost should still be the same"""
    new_places = place ("Malagar", "spain", 1, "n")
    print (new_places)

    # TODO: Add more tests, as appropriate, for each method
    print (new_places)
    """String is representation of place"""
    print (new_places.check_visited ( ))
    """Check if place has been visited or not"""
    print (new_places.is_important ( ))
    """Important that place is added to the list"""


run_tests ( )
