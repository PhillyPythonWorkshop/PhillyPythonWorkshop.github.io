### Math  
* adding
* subtracting
* multiplying
* dividing – NOTE DIFF b/t 2 & 3 – real & floor
* modulus


### Strings
* enclosed in quotes – single or double, just be consistent
* think of as text but they can hold anything, just get treated as text

#### things you can do with strings
* len()
* concatenate
* multiply

Let's look at documentation – Google is your friend.  Look up “Python string methods” – just like any research, you have to think a little about how to frame your question.  Be sure you're looking at the right version in the Python docs.
* x='hello'
* x.captitalize()
* x.center(15)
* x.center(15,'*')
* x.isalnum()   *we'll get to what that true/false means in a bit

### Variables

* Think of them as names/holders for values
* = is used to assign a variable to value
* can be assigned to any kind of value – strings, numbers, other data types we'll see later
* can be reassigned


### Booleans
* True or False (result of ==, <, >, <=, >=, is, in, not)
* Combine with and/or

### Conditionals

* if/elif/else
* Tell Python to do something based on the condition of something else

~~~
brother_age = 12
sister_age = 9
if brother_age > sister_age:
    print(“Brother is older”)
elif brother_age == sister_age:
    print(“They are the same age”)
else:
    print(“Brother is younger”)
~~~

Things don't have to be relevant:

~~~
if brother_age > sister_age:
    print(“Knock knock”)
~~~

We can have multiple conditions & operations in conditions

~~~
pizza = 10
hoagie = 7

if pizza > 5 and hoagie > 5:
    print(“Both cost more than $5”)

if pizza + hoagie < 20:
    print(“Lunch for two for under 20 bucks!”)
~~~



### Functions

Running one-off scripts is fine, but the whole point of learning to code is reproducibility.  We want to be able to automate things so we don't have to write the same code over and over again. 

~~~
def add_two(x, y):
    return x +  y
~~~

We can have conditionals inside functions

~~~
def lunch_for_two(lunch1, lunch2):
    if lunch1 + lunch2 < 20:
        return “Lunch for two under $20”
    else:
        return “You need more money”
~~~

We can assign results of functions to variables 

~~~
def add_two(x,y):
    return x + y

total = add_two(45, 21)

total + 1
~~~

Difference between print & return

~~~
def mult_two(x,y):
    print(x*y)

def mult_two(x,y):
    return(x*y)
~~~


### Types

Every object in Python has a type.  We've looked at a few types already – string, int, float, function, bool
Python is strongly typed and dynamically typed.  What does this mean?
* Dynamically: type is set at runtime, not in the code
* Strongly typed: Python won't fudge the types to make an operation work

2 + 3 works 

2 + “3” does not

We can use these to test whether certain operations can be performed

~~~
a = 3 
b = '4' 
 
if type(a) == int and type(b) == int: 
    print(a+b) 
else: 
    print("Can't add different types") 
~~~


Try:
~~~
type(5)
type('5')
type('hello')
type(5.2)
type(True)
~~~


### Lists

Purpose

We've looked at single elements, but we often need groups of elements to be useful – new data type called list
* Initialization: enclose comma separated values in square brackets
* We can assign them to a variable, 
* Lists can contain any mix of values

Methods

len()  - just like strings, get count of items in list

Accessing elements

We access elements by their position.  Start from 0. Think of it like your age.  You're not 1 until the second year of your life.  Stay in range.  Start at left with 0.  Start at right with -1

~~~
mylist = ['alligator', 'bat', 'cat', 'dog', 'elephant', 'frog']
mylist[0]
mylist[-2]
mylist[9] #out of range
~~~

Other things to do with lists – look up Python list methods

Adding elements
~~~
mylist.append(x)
mylist.insert(1, 'zebra')
~~~

Removing elements
~~~
mylist.remove('dog')
~~~

How would you remove the item in position 3?  Look up in the docs.

Changing elements
~~~
mylist[2] = 'yak'
~~~

Slicing lists

: to define range – start point is inclusive, stop is not
~~~
mylist[1:3]
~~~

Out of range OK
~~~
mylist[2:10]
~~~


Get the entire list [:] as a copy

What happens when you do this:
~~~
a = ['banana', 'strawberry', 'peach'] 
b = a 
c = a[:] 

a.append['mango']
print(a)
print(b)
print(c)
~~~

Get max & min values
~~~
max(fruits) 
min(fruits) 
~~~

Sorting lists, in place
~~~
fruits.sort()
~~~

		
### Tuples
* defined with parentheses
* like lists but immutable
* can access specific elements but can't change them
* strings are like tuples - can slice, access elements, can not change elements


### Range
range()  

* start (inclusive, 0 if omitted), stop (exclusive), step optional
* A little different in Python 3 – keeps it as a range type
* Python 2 would translate this into a list

~~~
range(10)
range(0,100,5)
~~~


### Loops

#### for loops

We looked at accessing & changing elements at known points.  We can also access & change a series of items in the list

for x in mylist:
    do something



~~~
print(range(10))

for x in range(10):
    print(x+10)

~~~~

* x is assinged at runtime – can have any name
* Just don't use a name you've used elsewhere.  Singular of the list is common, as is 'i'
* Python remembers the last value of x even though it is generally used as a throwaway variable

~~~~
b = [32, 6, 9, 17, 209]
for x in range(len(b)): 
    b[x] = b[x] + 1 
print(b)

c = [2, 4, 1, 8]    
# Why won't this work?
for x in c:
    x = x + 1
~~~~    
    
 
#### if statements inside for loops
We've talked about loops – how to step through things one by one, and conditionals. Let's put it together.  

~~~
for x in range(len(b)): 
    if b[x]%2 == 0: 
        b[x] = b[x] + 5 
print(b)
~~~

Loops can be nested

~~~
# What will this print? 
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
for letter in letters:
    for number in numbers:
        print letter * number
~~~~    

Order matters for nested loops!

~~~
for number in numbers:
   for letter in letters:
       print number * letter
~~~


#### while loops
* With for loops we specify a start and end point
* While loops – do something until a certain condition is met

~~~
x = 0
while x < 100:
    print(x)
    x += 1   #note here's a shortcut
~~~

CAUTON: infinite loops.  What would happen if I didn't increment x?

~~~
x = 0
while x < 100:
    print(x)
~~~

#### if statements inside while loops

~~~
x = 0 
while x < 100: 
    if x%5 != 0: 
        print(x) 
    x+=1 

q = [] 
x = 0 
while x < 100: 
    if x % 5 != 0: 
        q.append(x) 
    x += 1 
~~~


breaking from loops

~~~
x = 0 
while x < 100: 
    print(x) 
        if x == 65: 
            break 
    x += 5 
~~~

### Getting user input

~~~
input() #Python 3
raw_input() #Python 2
~~~

* When you want user input 
* Always a string, can be converted into an int.

~~~
x = input("choose a number from 1 to 10: ") 
type(x)
float(x) 
int(x) 
~~~


### Dictionaries


Initialization: 

* key – value pairs, separated by : .  Unordered.  In curly braces.
* Random is still a type of ordering.  Here order is irrelevant.
* So you can't get elements by position.  You get them by keys.
* Keys must be unique, values don't have to be.

Accessing elements

~~~
scores = {'ali':45, 'bob':34, 'cam':65, 'dev':12, 'eli':21} 
print(scores) 
scores['bob'] 
~~~


Adding elements

* You can't just append – there is no specified beginning or end.
~~~
scores['flo'] = 87 
print(scores) 
~~~

changing elements

~~~
scores[eli] = 88
~~~

keys() and values()

~~~
scores.keys() 
# dict_keys(['eli', 'cam', 'flo', 'dev', 'bob', 'ali']) 
scores.values() 
# dict_values([90, 65, 87, 12, 34, 45]) 
~~~ 

See the order is NOT the same for the keys and values that are returned

You can look up items by key.  There are workarounds to do it by value but we're not getting into that now.  That's not the point of a dictionary.


### Modules

Purpose: Python has a lot of great stuff right out of the box.  Even more through importing modules.  Standard modules can be imported at any time.  Other modules like stat analysis packages need to be installed.

Google 'Python standard library' -- review built in modules and other modules.


Other modules such as `math` and `random`

~~~
import math
import random

math
math.pi
math.sqrt()
random
random.randint()
random.choice()

dir(math)
help(math)
help(math.sqrt)

~~~




#### Let’s put it all together.

Walk through `state_capitals.py`. Copy and paste this whole file in your text editor and save it as `state_capitals.py`.

* create a dictionary of states & capitals
* import a module
* write a while loop
* select a random key and value from the list
* take user input to guess state capital
* evaluate user’s input & respond
* allow user to end game

Run it using python3 state_capitals.py

### Practice exercises

#### Exercise 1 (as a class)

Write a function that simulates the roll of two standard six sided die. Save it to a file called `dice_roll.py`. Open a Python interpreter and `import dice_roll`. Run the function inside your Python interpreter.

Before writing the actual code, write what you want to do in comments in plain English.

~~~

import random

def roll_two():
   #import the random module
   #write the shell of a function
   #get one random number between 1 and 6
   #get another random number between 1 and 6
   #add them together
   #return the result

~~~

#### Exercise 2 (individual work)

Write a function that takes one argument. If the argument is a list, it returns a random item from that list - simulating drawing a person’s name from a hat. If the argument is not a list, it returns the message “The argument must be a list.” Save the file and run it inside your Python interpreter and from your computer's terminal.

#### Exercise 3 (class work)

hilo game

~~~

num_to_guess = random.randint(1, 100)

while True:
    num_guess = int(input("Guess a number between 1 and 100:  "))
    if num_guess == num_to_guess:
        print("You got it!")
        break
    elif num_guess >= num_to_guess:
        print("Too high. Try again")
    elif num_guess <= num_to_guess:
        print("Too low. Try again.") 
~~~

Move on to scrabble

