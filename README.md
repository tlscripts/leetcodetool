## Leetcode Github solutions organizer and separator by easy, medium, hard rated questions.

___

I know alot of people as well as myself are studying and learning from leetcode examples and solutions. There are fantastic resources on github that gives examples on how to solve them. A few of us in our group (I'm looking at you Alvin and Dom) wished some of these repositories would separate the solutions by degree of difficulty (easy, medium, hard).

Hence the need for this tool. 
(Tools is catered to Unix based OS's)
___

### What this script does
* Clones this repository https://github.com/kamyu104/LeetCode-Solutions to the directory where script is ran.
* Pulls the Python folder from inside the initial folder to where script is ran.
* Creates 3 directories easy, medium, hard.
* Uses leetcode.com's api to get a list of all current questions in json
* Compares the 'slug' key from the json to the names of the python files with an added ".py" extension
* Matches up names of files and their difficulty levels and moves to appropriate folder

While it misses a few files (I think this may be due to the it not being in the repo itself), out of 1034 files it moved all but few for me.

![](https://github.com/tlscripts/leetcodetool/blob/master/leetcode.png)




