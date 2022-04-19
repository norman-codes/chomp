# The open-source "appJar" framework (found in the official Python documentation here: https://wiki.python.org/moin/GuiProgramming)
# is used to generate a GUI simply and easily using Python's native interface toolkit ("TkInter" - https://wiki.python.org/moin/TkInter).
# "appJar"'s complete documentation, referenced throughout the project, is available here: http://appjar.info/
from appJar import gui
# Python has a native library for reading files with the ".json" extension. (https://docs.python.org/3/library/json.html)
# The dataset used for this project is held within a ".json" file, so it is imported here.
import json

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