# The open-source "appJar" framework (found in the official Python documentation here: https://wiki.python.org/moin/GuiProgramming)
# is used to generate a GUI simply and easily using Python's native interface toolkit ("TkInter" - https://wiki.python.org/moin/TkInter).
# "appJar"'s complete documentation, referenced throughout the project, is available here: http://appjar.info/
from types import NoneType
from appJar import gui
# Python has a native library for reading files with the ".json" extension. (https://docs.python.org/3/library/json.html)
# The dataset used for this project is held within a ".json" file, so it is imported here.
import json
# Python has a native library for mathematical operations necessary to calculuate the
# distance between two latitude/longitude pairs.
import math
# Python's native "OS" library aids in finding the database file by allowing the script to specify the path.
import os.path

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
    
    # Distance to UF, assigned to a variable after being calculated once to optimize processing time.
    distanceToUF = 1.0

    # "Chompability" - the custom rating of a location. See constructor for calculation details.
    chompability = 0.0

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

        # Calculating the distance to UF from the inputted coordinates.
        self.distanceToUF = distance(_latitude, _longitude, UF_latitude, UF_longitude)
        
        # Calculating "Chompability":
        # chompability = (X / distance) + (numReviews / stars)
        # where X is a *USER-INPUTTED* "closeness factor" (default is 1);
        # if it is increased, then the user is okay with traveling a larger distance
        # and as a result, the chompability of restaurants that are further away from UF will increase.
        self.chompability = (1 / self.distanceToUF) + (_numReviews / _stars)

    # "rechompify" recalculates the "Chompability" based on a new closeness factor.
    def rechompify(self, closeness):
        self.chompability = (closeness / self.distanceToUF) + (self.numReviews / self.stars)

# ARRAY
locations = []

# READING THE .json FILE
# (and creating Location objects with it, to be pushed into an array.)
# Reference: https://www.geeksforgeeks.org/read-json-file-using-python/
# Encoding issues fixed by adding "errors="replace"" into open() function.

# Opening the dataset file.
datasetFile = open(os.path.dirname(__file__) + '\\dataset\\yelp_academic_dataset_business.json', errors="replace")
# Reading every line and putting it into a list.
lines = datasetFile.readlines()
# For every line in the file (150,346), load the .json "object" and its variables into a "dictionary" (Reference: https://www.w3schools.com/python/python_dictionaries.asp).
    # Note that the equivalent structure in C++ is an ordered map (Reference: https://stackoverflow.com/questions/2884068/what-is-the-difference-between-a-map-and-a-dictionary).
for line in lines:
    # The JSON object in the current line is parsed.
    locationJSON = json.loads(line)
    # Every relevant variable from the JSON may now be used to instantiate a "Location" object.
    if locationJSON["categories"] != None:
        # Note that the "categories" of a given location are injected into a comma-separated string.
        # It must be changed into a list in order for the assignment to be correct using the ".split("delimiter")" function.
        # Reference: https://www.codespeedy.com/how-to-convert-comma-separated-string-to-list-in-python/
        # If at least one category exists for a given location, then split it into a list and create the object with it.
        category_list = locationJSON["categories"].split(", ")
        currentLocation = Location(locationJSON["business_id"], locationJSON["name"], locationJSON["address"], locationJSON["city"], locationJSON["state"], locationJSON["latitude"], locationJSON["longitude"], locationJSON["stars"], locationJSON["review_count"], category_list)
    else:
        # If no categories exist for a given location, then push "none" into the category list and create he object with it.
        currentLocation = Location(locationJSON["business_id"], locationJSON["name"], locationJSON["address"], locationJSON["city"], locationJSON["state"], locationJSON["latitude"], locationJSON["longitude"], locationJSON["stars"], locationJSON["review_count"], "none")
    
    # The "locations" array is appended with the current location object.
    locations.append(currentLocation)

# QUICKSORT
# Reference: https://www.geeksforgeeks.org/python-program-for-quicksort/

#commit test

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