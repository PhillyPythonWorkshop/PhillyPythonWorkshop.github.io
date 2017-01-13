---
layout: page
title: Saturday Lesson
permalink: /saturdaylesson/
---

## Lecture outline

### review Friday material

* math
* type()
* variables
* strings
* booleans
* if/elif/else
* functions

### lists

* purpose
* initialization
* len() review
* accessing elements
* adding elements
* changing elements
* slicing lists

### tuples

* like lists but immutable
* can perform all the same operations except changing elements
* strings are like tuples - can slice, access elements, can not change elements

### loops and more flow control

* for loops
* if statements inside for loops
* nested for loops
* range()
* while loops
* infinite loops
* if statements inside while loops
* break
* input()

### dictionaries

* purpose
* initialization
* accessing elements
* adding elements
* changing elements
* keys() and values()

### modules

* purpose
* builtins
* imports
    * math
        * math.pi
        * math.sqrt()    
    * random
        * random.randint()
        * random.choice()

###Let's put it all together.

Walk through [state_capitals.py](https://raw.githubusercontent.com/PhillyPythonWorkshop/PhillyPythonWorkshop.github.io/master/misc/state_capitals.py).  Copy and paste this whole file in your text editor and save it as `state_capitals.py`.

* create a dictionary of states & capitals 
* import a module
* write a while loop 
* select a random key and value from the list
* take user input to guess state capital
* evaluate user's input & respond
* allow user to end game


### Practice exercises

#### Exercise 1 (as a class)

Write a function that simulates the roll of two standard six sided die. 
Save it to a file called `dice_roll.py`.  Open a Python interpreter from that same directory and `import dice_roll`.  Run the function inside your Python interpreter.



#### Exercise 2 (individual work)

Write a function that takes one argument.  If the argument is a list, it returns a random item from that list - simulating drawing a person's name from a hat.  If the argument is not a list, it returns the message "The argument must be a list." Save the file and run it inside your Python interpreter.
