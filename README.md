# BROADIE_EXERCISES
Exercises for Broad Institute 


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


To run Question 1:

a) download subway_lines.py

b) if not installed, install the below module(s) in command window as follows: pip install <module>   

json

urllib

requests

b) if not already installed, install python (version Python 3.6.5) was used for dev 

c) in console, type:

   python subway_lines.py

