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

import os.path
import codecs

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

# READING THE .json FILE
# (and creating Location objects with it, to be pushed into an array.)
# Reference: https://www.geeksforgeeks.org/read-json-file-using-python/
# Encoding issues were present, and the "codecs" library was necessary to open the .json file properly.
# Reference for encoding issue fix: https://stackoverflow.com/questions/30598350/unicodedecodeerror-charmap-codec-cant-decode-byte-0x8d-in-position-7240-cha

types_of_encoding = ["utf8", "cp1252"]
for encoding_type in types_of_encoding:
    file1 = codecs.open(os.path.dirname(__file__) + '\\dataset\\yelp_academic_dataset_business.json', encoding=encoding_type, errors='replace')
    Lines = file1.readlines()

    for line in Lines:
        test = json.loads(line)


# QUICKSORT
# Reference: https://www.geeksforgeeks.org/python-program-for-quicksort/

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def partition(location_arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = location_arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if location_arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			location_arr[i], location_arr[j] = location_arr[j], location_arr[i]

	location_arr[i+1], location_arr[high] = location_arr[high], location_arr[i+1]
	return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(location_arr, low, high):
	if len(location_arr) == 1:
		return location_arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(location_arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(location_arr, low, pi-1)
		quickSort(location_arr, pi+1, high)


# Driver code to test above
location_arr = [10, 7, 8, 9, 1, 5]
quickSort(location_arr, 0, len(location_arr)-1)

# HEAPIFY
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(location_arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and location_arr[i] < location_arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and location_arr[largest] < location_arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		location_arr[i],location_arr[largest] = location_arr[largest],location_arr[i] # swap

		# Heapify the root.
		heapify(location_arr, n, largest)

# The main function to sort an array of given size
def heapSort(location_arr):
	n = len(location_arr)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(location_arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		location_arr[i], location_arr[0] = location_arr[0], location_arr[i] # swap
		heapify(location_arr, i, 0)

# Driver code to test above
location_arr = [ 12, 11, 13, 5, 6, 7]
heapSort(location_arr)

# HEAPSORT
# Reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/

# GUI CODE
# Reference: http://appjar.info/
app = gui("Chomp", "1280x720")
app.addLabel("title", "Welcome to appjar")
app.setLabelBg("title", "red")
app.go()