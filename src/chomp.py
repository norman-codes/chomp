# The open-source "appJar" framework (found in the official Python documentation here: https://wiki.python.org/moin/GuiProgramming)
# is used to generate a GUI simply and easily using Python's native interface toolkit ("TkInter" - https://wiki.python.org/moin/TkInter).
# "appJar"'s complete documentation, referenced throughout the project, is available here: http://appjar.info/
from appJar import gui
# Python has a native library for reading files with the ".json" extension. (https://docs.python.org/3/library/json.html)
# The dataset used for this project is held within a ".json" file, so it is imported here.
import json
# Python has a native library for mathematical operations necessary to calculuate the
# distance between two latitude/longitude pairs.
import math

# CLASS: Location
# This class ontains relevant information for each location within the Yelp dataset, namely:
    # business ID (string),
    # name (string),
    # address (string),
    # city (string),
    # state (string),
    # latitude (float),
    # longitude (float),
    # stars (float),
    # review count (int),
    # categories (array of strings)
class Location:
    # Variables extracted from .json with default values.
    ID = "1"
    name = "name"
    address = "address"
    city = "city"
    state = "none"
    latitude = 123.45
    longitude = 123.45
    stars = 1.2
    numReviews = 1
    categories = []
    


    # "Chompability" - the custom rating of a location based on:
        # distance from UF to the location
            # calculated from longitude/latitude pairs
        # (numReviews / stars)
    chompability = 0

    # "Constructor"
    def __init__(self, _ID, _name, _address, _city, _state, _latitude, _longitude, _stars, _numReviews, _categories):
        # Setting the object's values to the parsed .json's values.
        self.ID = _ID
        self.name = _name
        self.address = _address
        self.city = _city
        self.state = _state
        self.latitude = _latitude
        self.longitude = _longitude
        self.stars = _stars
        self.numReviews = _numReviews
        self.categories = _categories
        
        # Calculating "Chompability":

# DISTANCE CALCULATION:
# The latitude and longitude coordinate pair of the University of Florida, extracted from Google Maps:
# https://www.google.com/maps/place/University+of+Florida/@29.6436325,-82.3636849,15z/data=!4m8!1m2!3m1!2sUniversity+of+Florida!3m4!1s0x88e8a30cfbe49275:0x206fe0de143d9886!8m2!3d29.6436325!4d-82.3549302
UF_latitude = 29.6436325
UF_longitude = -82.3636849
# The Haversine formula (https://en.wikipedia.org/wiki/Haversine_formula)
# is used to calculate the distance between two coordinates in "WGS-84" format.
# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula

def distance(latitude_1, longitude_1, latitude_2, longitude_2):
    p = math.pi / 180 # PI / 180 is to convert degrees to radians.
    a = 0.5 - (math.cos((latitude_2 - latitude_1) * p) / 2) + (math.cos(latitude_1 * p)) * (math.cos(latitude_2 * p)) * ((1 - math.cos((longitude_2 - longitude_1) * p)) / 2)
    return math.ceil(12742 * math.asin(math.sqrt(a))) # Returns distance between two coordinate pairs in KILOMETERS, rounded up to nearest integer (ceiling). (note that 12742 = diameter of the Earth in km.)
# usage: var = distance(obj.latitude, obj.longitude, UF_latitude, UF_longitude)

# READING THE .json FILE
# (and creating Location objects with it, to be pushed into an array.)
# Reference: https://www.geeksforgeeks.org/read-json-file-using-python/

# QUICKSORT
# Reference: https://www.geeksforgeeks.org/python-program-for-quicksort/

# HEAPIFY
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/

# HEAPSORT
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/

# GUI CODE
# Reference: http://appjar.info/
app = gui("Chomp", "1280x720")
app.addLabel("title", "Welcome to appjar")
app.setLabelBg("title", "red")
app.go()