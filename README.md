# Chomp!
The repository for "chomp" - the Yelp-inspired, Gator-friendly restaurant finder.
Norman and Blake's Project 3 for Data Structures &amp; Algorithms (COP3530), Spring 2022.

# Video Demonstration
https://youtu.be/HlQXSDTRO-M

# Description
**Problem: What problem are we trying to solve?**

We are making an easy-to-use application for the residents of Gainesville that can help them find
the perfect restaurant to eat at. The app will take in datasets from Yelp of restaurants, each with a
unique ID (string) as well as a bunch of relevant information (name, location info, # of stars,
review count, etc.) and from certain numerical info (closeness to UF, rating, etc.), then generate a
unique "Chompability" score for each place.

**Motivation: Why is this a problem?**

Locating an optimal restaurant as close as possible to UF is sometimes difficult; and having an
easy way to navigate the available places by preference is extremely convenient. College kids are
sometimes too busy to look up what restaurants provide the cuisine they like at a high level of
satisfaction. So we decided to develop an app that provides the best results based on their
requests.

**Features implemented:**

- GUI with SORTING BY CATEGORY, STATE, AND CITY: a custom-build graphical user
interface that accepts user input for location category, state, and city, as well as a custom display
order.
- CHOMPABILITY: a custom score based on the location’s proximity to UF and popularity (from
its stars and number of reviews).
- CLOSENESS FACTOR: how far a user is willing to travel (on a scale from 1 [closest to UF] to
100 [anywhere at all]). Used to help calculate chompability.

**Description of Data:**

We will be using a dataset provided by Yelp to ensure we implement accurate data into our
application, specifically the data from 150,346 businesses. It is represented by a .json file with
several business-specific categories, namely: unique 22-character **ID** , **name** , **address** , **city** , **state** ,
postal code, **latitude** , **longitude** , **stars** , **review count** ,closed/open status, attributes, and
**categories**. We accessed the bolded values and createda Class to instantiate objects.

**Dataset Links:**

```
https://www.yelp.com/dataset
https://www.yelp.com/dataset/documentation/main
```

**Tools/Languages/APIs/Libraries used:**

Language
- Python

APIs/Libraries
- EXTERNAL: appJar (http://appjar.info/)
- NATIVE: json, math, os.path, sys

**Algorithms implemented:**

The two unique non-trivial algorithms we implemented using are **Quick Sort** & **Heap Sort**.
They will be sorting an array of “Location” objects by their “Chompability” score (an arbitrary
unit calculated from distance to UF and the average number of stars and number of reviews).

**Additional Data Structures/Algorithms used:**

- List (Python equivalent of an array)
- Dictionary (Python equivalent of an ordered map)
- Sets (in Python, they are unordered sets)

**Distribution of Responsibility and Roles: Who did what?**

- Blake: Coordinating the written report, programmingfunctionality of the project (specifically,
the sorting algorithms), and contributing to GUI design concepts.
- Norman: Coordinating programming functionality ofthe project (specifically, reading in the
.json file of the Yelp dataset into the program and coding the GUI), contributing to the written
report, and recording the walkthrough video.

**Any changes the group made after the proposal? The rationale behind the changes.**

- Changing the project name.
“Chomp!” felt more succinct and aesthetically pleasing.
- Changed the language from C++ to Python.
Including external libraries in C++ proved to be extremely cumbersome, so we decided to try
Python out since its interactions with libraries (as well as its syntax) is much simpler.
- Changed distance from user to given restaurant to location from UF to given location.
The distance to UF could be used as a metric to calculate a custom, sortable score.
- Added “Chompability” score as a metric for how locations should be sorted.
To have a target set of numbers for our sorting algorithms, we needed to come up with a custom
scoring system.
- Changed the GUI from a console app (command-line) to a desktop app.
We thought that this would be better for the user experience.
- Changed data structures/algorithms we will compare from a focus on comparing how
data is **STORED** (multimap vs. hash table, with binarysearch & quick sort) to
comparing how data is **SORTED** (using _quick sort_ vs. _heap sort_ ).
This was much more feasible given our team configuration and played to our programming
strengths.


**Complexity analysis of the major functions/features you implemented in terms of Big O for
the worst case:**

Parsing the .json file and creating objects for every location required parsing every line which
yielded 150,346 unique objects. This is our “n”.
TIME COMPLEXITY REFERENCE: TA “Sorting_Review”
**Quick Sort** - O(n^2)
The worst case of Quick Sort is quadratic. Since our “Chompability” was the value which was
being sorted - and because it changed _very_ often (everytime a user changed their “Closeness
Factor”, how far they are willing to travel [on a scale from 1 to 100]) - the locations array being
sorted was often in the worst case.
**Heap Sort** / **Heapify** - O(n log n)
The worst case of Heap Sort / Heapify is linear multiplied by logarithmic (nlog(n)). Building the
heap itself is O(n); extracting is O(log(n)) - removing is O(1) and heapify is O(log(n)). The
sorting algorithm’s efficiency compounded at scale, meaning it was evident that its efficient time
complexity saved time and processing power when compared to quick sort.

```
for n = 150,346:
Quick Sort = O(n^2) for worst case = 22,603,919,716 - twenty two BILLION
vs.
Heap Sort = O(nlog(n)) for worst case = 778,355 - only around 800 thousand
```

**As a group, how was the overall experience for the project?**

Overall, the experience for the project was very engaging and enlightening, especially with the
use of unfamiliar libraries and languages, since both of us had little prior experience with
Python. It was definitely positive because we enjoyed working with a large dataset and putting
our knowledge into practice, as well as approaching the design process for our GUI as a team.

**Did you have any challenges? If so, describe.**

The largest challenge was the downsizing of our group to two members instead of three due to
unforeseen circumstances. We had to reprioritize our goals for the project - specifically how
large-scale we wanted our implementation of the algorithms we chose to be.
Another critical obstacle was the necessity to use external libraries for the project, namely to
parse the .json file as part of integrating Yelp’s dataset and to create an interactive GUI. After
multiple attempts to do so in C++ with both CLion and Visual Studio, we made the decision to
switch entirely to Python despite our relative unfamiliarity with the language and its libraries.
This proved to be an excellent solution and a great learning opportunity.


**If you were to start once again as a group, any changes you would make to the project
and/or workflow?**

We feel that the project is designed to encourage creative freedom while also not being extremely
burdensome in the required implementation of various data structures and algorithms. As such,
we would not change anything about the project itself. If we were to start the project again as a
group, we would start researching the necessary libraries and coding basic implementation of
interactive elements (such as a GUI) much earlier. This way, the obstacles which we faced would
have been visible sooner, giving us more time to find solutions.

- Blake: My knowledge for Github grew exponentiallywhile completing this project. I came in
knowing the basic minimum of Github, but with help from Norman, I feel comfortable going
through and committing files into Github. Through my understanding with sorting algorithms in
C++, I was able to reference the similarities to create sorting methods through Python.

- Norman: Jumping into coding the project in Pythonhelped me dive deep into the many benefits
its interpretive nature and direct syntax provide. Aside from that, I learned a lot about importing
and using both native and external libraries in Python. Aside from technical aspects, I learned a
lot about my preferences for project organization due to the required use of GitHub, which I felt
was extremely helpful.


