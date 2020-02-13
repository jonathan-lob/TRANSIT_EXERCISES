# TRANSIT_EXERCISES
Exercises for Transit System Rail Lines 


Question 1
Write a program that retrieves data representing all, what we'll call "subway" routes: "Light Rail"
(type 0) and “Heavy Rail” (type 1). The program should list their “long names” on the console.
Partial example of long name output: Red Line, Blue Line, Orange Line...
There are two ways to filter results for subway-only routes. Think about the two options below
and choose:
1. Download all results from https://api-v3.mbta.com/routes then filter locally
2. Rely on the server API (i.e., https://api-v3.mbta.com/routes?filter[type]=0,1) to
filter before results are received
Please document your decision and your reasons for it.


To run Question 1 and 2:

a) download subway_lines.py

b) b) if not already installed, install python (version Python 3.6.5) was used for dev 

c) if not installed, install the below module(s) in command window as follows: pip install <module>   

json

urllib

requests



d) in console, type:

   python subway_lines.py








Expected Output Question1 and Question2 first two parts:

c:\py_mbta>python subway_routes.py


################################Question 1 output################################


light rail lines USING FILTER method for efficiency and to minimize load on API server:


Mattapan Trolley
Green Line B
Green Line C
Green Line D
Green Line E


heavy rail lines USING FILTER method for efficiency and to minimize load on API server:


Red Line
Orange Line
Blue Line



################################Question 2 output################################


max stops on a rail line:46  on the following line:Red Line
min stops on a rail line:11  on the following line:Green Line E

c:\py_mbta>

Question 2, part 3 is in development
Design Plan 1:
Traverse all stops in all rail lines. Find the non-unique stop names and these are assumed to be
"gateways" between rail lines. Store these along with associated rail lines. Print them out. 

Design Plan 2:
Similar to  Design Plan 1 but use station coordinates to determine if same stop

################################Question 3 design plan ################################
1. Retreive beginning stop and end stop from user.
2. if both stops on a single rail line. 
       print beginning stop, end stop and rail line
   elif beginning stop rail line and end stop rail line have single common "gateway" as (determined in Question 2, part 3),
           print beginning stop, end stop, rail line of beginning end stop rail line have 
   elif no common "gateway"
      using "gateways" find shortest path and print out associated rai lines
      shortest path could be based off:
         a. least number of stops between beginning stop and end stop
         b. shortest distance of the trip using stop coordinates
         d. shortest time of route traversalusing average time (if available)
        
      
      
   


