# The open-source "appJar" framework (found in the official Python documentation here: https://wiki.python.org/moin/GuiProgramming)
# is used to generate a GUI simply and easily using Python's native interface toolkit ("TkInter" - https://wiki.python.org/moin/TkInter).
# "appJar"'s complete documentation, referenced throughout the project, is available here: http://appjar.info/
from appJar import gui
# Python has a native library for reading files with the ".json" extension. (https://docs.python.org/3/library/json.html)
# The dataset used for this project is held within a ".json" file, so it is imported here.
import json
# Python has a native library for mathematical operations (https://docs.python.org/3/library/math.html); here, it is necessary to calculuate the
# distance between two latitude/longitude pairs.
import math
# Python has a native library for operating system-related functionality (https://docs.python.org/3/library/os.html);
# here, it aids in finding the database file by allowing the script to specify the path to it relative to the user's file system.
import os.path
# Python has a native library for time acccess and conversions (https://docs.python.org/3/library/time.html);
# here, it allows us to track the time at which a function starts and ends to compare and display the execution speeds of each sorting algorithm.
import time

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
        self.numFactor = (_numReviews / (5.0 / _stars))
        # Calculating "Chompability":
        # chompability = (X / distance) + (numReviews / stars)
        # where X is a *USER-INPUTTED* "closeness factor" (default is 1);
        # if it is increased, then the user is okay with traveling a larger distance
        # and as a result, the chompability of restaurants that are further away from UF will increase.

        self.chompability = round((((100 / 1) * (1000 / self.distanceToUF)) + (self.numFactor / (100 - 1))), 4)
    # "chompify" calculates the "Chompability" based on a closeness factor.
    def chompify(self, closenessFactor):
        if (closenessFactor == 100):
            self.chompability = round(self.numFactor, 4)
        else:
            self.chompability = round((((100 / closenessFactor) * (1000 / self.distanceToUF)) + (self.numFactor / (100 - closenessFactor))), 4)

# Initializing the array of Location objects. This array will be sorted based on the "Chompability" of each location.
locations = []
# Initializing sets of Categories, States, and Cities. These sets will be populated as the .json file is read (why sets? no duplicates!).
# The array will be populated from the sets and will be used for dropdown menus & checking input validity in the GUI.
# Sets can be typecast into lists (arrays), which will be done for the dropdown menus & for checking input validity in the GUI.
# Reference: https://www.geeksforgeeks.org/python-convert-set-into-a-list/

# Note that the number of categories is very large (1300+): https://blog.yelp.com/businesses/yelp_category_list/
categories = set()
states = set()
cities = set()

# READING THE .json FILE (and creating Location objects with it, to be pushed into an array).
# Reference: https://www.geeksforgeeks.org/read-json-file-using-python/
# Encoding issues fixed by adding "errors="replace"" into open() function.

# Opening the dataset file.
datasetFile = open(os.path.dirname(__file__) + '\\dataset\\yelp_academic_dataset_business.json', errors="replace")
# Reading every line and putting it into a list.
lines = datasetFile.readlines()
# For every line in the file (150,346 lines!), load the .json "object" and its variables into a "dictionary" (Reference: https://www.w3schools.com/python/python_dictionaries.asp).
    # Note that the equivalent structure in C++ is an ordered map (Reference: https://stackoverflow.com/questions/2884068/what-is-the-difference-between-a-map-and-a-dictionary).
for line in lines:
    # The JSON object in the current line is parsed.
    locationJSON = json.loads(line)

    # Adding the state and city of the current location into their respective sets.
    states.add(locationJSON["state"])
    cities.add(locationJSON["city"])

    # Every relevant variable from the JSON may now be used to instantiate a "Location" object.
    if locationJSON["categories"] != None:
        # Note that the "categories" of a given location are injected into a comma-separated string.
        # It must be changed into a list in order for the assignment to be correct using the ".split("delimiter")" function.
        # Reference: https://www.codespeedy.com/how-to-convert-comma-separated-string-to-list-in-python/
        # If at least one category exists for a given location, then split it into a list and create the object with it.
        category_list = locationJSON["categories"].split(", ")

        # Adding each category in the list of categories of this location into the Categories set.
        for category in category_list:
            categories.add(category)
        
        currentLocation = Location(locationJSON["business_id"], locationJSON["name"], locationJSON["address"], locationJSON["city"], locationJSON["state"], locationJSON["latitude"], locationJSON["longitude"], locationJSON["stars"], locationJSON["review_count"], category_list)
    else:
        # If no categories exist for a given location, then push "none" into the category list and create the object with it.
        currentLocation = Location(locationJSON["business_id"], locationJSON["name"], locationJSON["address"], locationJSON["city"], locationJSON["state"], locationJSON["latitude"], locationJSON["longitude"], locationJSON["stars"], locationJSON["review_count"], "None")
        # Adding "None" to the list of categories if the user wishes to not specify no particular category while searching.
        categories.add("None")
    
    # The "locations" array is appended with the current location object.
    locations.append(currentLocation)

# QUICKSORT - called with "quickSort(locations, 0, len(locations) - 1)".
# Reference: https://www.geeksforgeeks.org/python-program-for-quicksort/
def rearrange(locationArray, low, high):
    # Defining the index of the smaller element.
	smallerElementIndex = (low - 1) # Note that this is equal to the "up" pointer, and "high" is equivalent to the "down" pointer.
    # Defining the pivot as the LAST element in the array.
	pivot = locationArray[high].chompability
    # For every element in the array:
	for i in range(low, high):
        # If the current element is less than or equal to the pivot:
		if locationArray[i].chompability <= pivot:
			# Increment index of the smaller element.
			smallerElementIndex += 1
            # Swap the original smallest element with the next smallest element. 
			locationArray[smallerElementIndex], locationArray[i] = locationArray[i], locationArray[smallerElementIndex]

    # Swap the current pivot location (locationArray[high]) with the index one greater than the next element smaller than it.
    # (found by the for loop above).
	locationArray[smallerElementIndex + 1], locationArray[high] = locationArray[high], locationArray[smallerElementIndex + 1]
    # Return the sorted element's index.
	return (smallerElementIndex + 1)

def quickSort(locationArray, low, high):
    # If the array passed in is 1 element long, it is sorted and will be returned.
	if len(locationArray) == 1:
		return locationArray
	if low < high:
        # The array must be rearranged such that all elements <= the pivot
        # (in this case, the last element), are in the left sub-array and
        # all elements > pivot are in the right sub-array.

		# The integer at sortedElementIndex represents the location of the pivot AFTER
        # one pass of QuickSort, as "rearrange" moves it.
		sortedElementIndex = rearrange(locationArray, low, high)
        # Recursively calling the function on the left sub-array.
		quickSort(locationArray, low, sortedElementIndex - 1)
        # Recursively calling the function on the right sub-array.
		quickSort(locationArray, sortedElementIndex + 1, high)

# HEAPIFY
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/
def heapify(locationArray, heapSize, root):
    # The index of the largest value is initialized as the root.
    largestIndex = root
    # The left child in array notation is equal to 2 * index + 1.
    left = 2 * root + 1
    # The right child in array notation is equal to 2 * index + 2.
    right = 2 * root + 2

    # If a left child exists for the root AND if it is greater than the root:
    if left < heapSize and locationArray[left].chompability > locationArray[root].chompability:
        # The index of the largest value is reassigned to be the left child.
        largestIndex = left

    # If a right child exists for the root AND if it is greater than the root:
    if right < heapSize and locationArray[right].chompability > locationArray[largestIndex].chompability:
        largestIndex = right
    
    # If the index of the largest value is NOT equal to the inputted root, swap them.
    if largestIndex != root:
        locationArray[root], locationArray[largestIndex] = locationArray[largestIndex], locationArray[root]

        # Heapify with the new (larger) root index.
        heapify(locationArray, heapSize, largestIndex)

# HEAPSORT - called with "heapSort(locations)".
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/
def heapSort(locationArray):
    # Finding the length of the inputted array.
    arrayLength = len(locationArray)
    # Defining the last parent index as the floor of the array length divided by two, minus one.
    lastParentIndex = arrayLength // 2 - 1
    # For every element starting from the last parent index and decrementing to index 0:
    for i in range(lastParentIndex, -1, -1):
        # Heapify the inputted array.
        heapify(locationArray, arrayLength, i)
    # The array itself is now a max heap.

    # Now, each element is extracted.
    # For every element in the max heap, starting from the final element and decrementing to index 1:
    for j in range(arrayLength - 1, 0, -1):
        # Swap the first and last elements of the array.
        locationArray[j], locationArray[0] = locationArray[0], locationArray[j]
        # Heapify the altered array.
        heapify(locationArray, j, 0)

# GUI CODE

# Reference: http://appjar.info/
app = gui("Chomp", "850x500", showIcon=False)

# Crocodile icon from flaticon.com.
app.setIcon((os.path.dirname(__file__) + '\\images\\crocodile.gif'))

# TOP FRAME
app.setStretch("both")
app.setSticky("news")
app.startScrollPane("TOP")

app.addLabel("locationPosition", "#\t", row=0, column=0).config(font="Helvetica 12 underline")
app.addLabel("locationScore", "\"Chompability\"\t\t", row=0, column=1).config(font="Helvetica 12 underline")
app.addLabel("locationName", "Name\t\t", row=0, column=2).config(font="Helvetica 12 underline")
app.addLabel("locationAddress", "Address\t\t", row=0, column=3).config(font="Helvetica 12 underline")
app.addLabel("locationCity", "City\t\t", row=0, column=4).config(font="Helvetica 12 underline")
app.addLabel("locationState", "State\t\t", row=0, column=5).config(font="Helvetica 12 underline")
app.addLabel("locationDistance", "Distance to UF\t\t", row=0, column=6).config(font="Helvetica 12 underline")
app.addLabel("locationStars", "Stars\t\t", row=0, column=7).config(font="Helvetica 12 underline")
app.addLabel("locationReviews", "Reviews\t\t", row=0, column=8).config(font="Helvetica 12 underline")
app.addLabel("locationCategories", "Categories", row=0, column=9).config(font="Helvetica 12 underline")
app.stopScrollPane()

# BOTTOM FRAME
app.setStretch("column")
app.setSticky("esw")
app.startFrame("BOT")

app.addLabel("AlgorithmLabel", "Sort Type", row=0, column=1).config(font="Helvetica 12 underline")
app.addOptionBox("AlgorithmInput", ["Quick Sort", "Heap Sort"], row=1, column=1)

app.addLabel("CategoryLabel", "Category", row=0, column=2).config(font="Helvetica 12 underline")
app.addEntry("CategoryInput", row=1, column=2)

# Converting the states set into a list.
states_list = list(states)
# Using Python's built-in sorting algorithm to put the list in lexicographical order.
# https://blog.finxter.com/python-list-sort/
states_list.sort()
# Inserting "Any" at the beginning.
states_list.insert(0, "Any")
app.addLabel("StateLabel", "State", row=0, column=3).config(font="Helvetica 12 underline")
app.addOptionBox("StateInput", states_list, row=1, column=3)

app.addLabel("CityLabel", "City", row=0, column=4).config(font="Helvetica 12 underline")
app.addEntry("CityInput", row=1, column=4)

app.addLabel("OrderLabel", "Order", row=0, column=5).config(font="Helvetica 12 underline")
app.addOptionBox("OrderInput", ["Top 10", "Top 25", "Top 50", "Top 100", "Bottom 10", "Bottom 25", "Bottom 50", "Bottom 100", "Custom"], row=1, column=5)

app.addLabel("ClosenessLabel", "Closeness", row=0, column=6).config(font="Helvetica 12 underline")
app.addScale("ClosenessInput", row=1, column=6)
app.setScaleRange("ClosenessInput", 1, 100, curr=1)
app.showScaleValue("ClosenessInput", show=True)

def chomp(btn):
    selected_algorithm = app.getOptionBox("AlgorithmInput")
    print(selected_algorithm)

    selected_categories = app.getEntry("CategoryInput").split(", ")
    for category in selected_categories:
        # If the category does not exist in the set, pop up an error message and do not proceed.
        if category not in categories:
            app.errorBox("noCategoryError", "This category does not exist!")
            return
        elif category == '' or category == "None":
            print(category)
            # If the category is equal to '' or "None"
            # then proceed to NOT SORT BY CATEGORY.


        # if it does, continue.
        # if not, error pop-up.
    
    selected_state = app.getOptionBox("StateInput")
    print(selected_state)
    
    selected_city = app.getEntry("CityInput")
    print(selected_city)

    selected_order = app.getOptionBox("OrderInput")
    print(selected_order)
    # if custom, then pop up with entry.

    closenessFactor = app.getScale("ClosenessInput")
    print(closenessFactor)

app.addButton("Chomp!", chomp, row=0, column=0, rowspan=2).config(font="Castellar 14")

app.stopFrame()
app.go()

