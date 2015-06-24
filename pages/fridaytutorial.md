---
layout: page
title: Friday Self-guided Tutorial
permalink: /fridaytutorial/
---

This is the self-guided, self-paced tutorial for Friday evening.  We've included a break in the middle, but remember to take a break to stretch, get some water, take a moment to relax any time you need to.

As you go through this tutorial, any time you see something like this:

`a = "Hello"`

it's something that you can type in at the `>>>` prompt in your Python shell.  Hit Return or Enter after every line and note the output (although sometimes there won't be any!).  Don't copy and paste -- you'll learn much better if you take the time to type everything yourself.

###Math

Math in Python looks a lot like math with a calculator.

####Addition

`2 + 2`

`1.65 + 2.15`

####Subtraction

`12 - 5`

`45.9 - 25.3`

`45.9 - 61.7`

####Multiplication
Multiplication uses the `*` (asterisk or star) symbol.

`6 * 7`

`5.6 * 4.3`

####Division
Division uses the `/` symbol.

`12/3`

`16/5`

> Note: If you've used Python 2, you'll see that division works differently in Python 3.  Python 2 uses floor division for integers, meaning it will return only the whole number part of the answer. Python 3 performs true division, returning the real or true value of the division.

####Order of Operations

Order of operations works just like you may have learned in math class - Multiplication, Division, Addition, Subtraction. You can also use parentheses.

`5 + 4 * 3`

`(5 + 4) * 3`

###Types

There's a helpful function (more on what a function is later) called `type` that tells you what kind of thing -- what data type -- Python thinks something is. We can check for ourselves that Python considers '1' and '1.0' to be different data types:

`type(1)`
`type(1.0)`

So now we've seen two data types: *integers* and *floats*.  We'll see more data types as we work through the lesson.

We used the term 'function' without explaining what it is -- we'll talk about functions more in a bit, and write our own, but for now know these things:

* Functions encapsulate some useful bit of work. We save that useful bit of work inside the function so we don't have to type it over and over again every time we want to use it. So, for example, some nice person decided that being able to determine the type of an object was useful, so he or she put the Python code that figures out an object's type into the function `type()`, and now we all get to use it, instead of having to write it ourselves.
* Functions are sort of like functions in math class. You provide input to a function and it produces output. The `type()` function takes data as an input, and produces what type of data the data is (e.g. an integer or a float) as output.
* To use a function, write the name of the function followed by an open parenthesis, what the function takes as input (we call that input the arguments to the function), and then a close parenthesis.

So in this case 'type' is the name of the function, and it takes one argument; in the example we first give type an argument of 1 and then give it an argument of 1.0.


*Stop for a moment here and try pressing the up arrow on your keyboard a few times.  The Python interpreter saves a history of what you've entered, so you can arrow up to old commands and hit Return to re-run them -- just like your computer's command prompt!  (Note, however, tab completion is not built into the Python shell.)*{: style="color: blue"}

###Variables

A lot of work gets done in Python using variables. Variables are like names that are assigned to a value -- any kind of value, not just a number.

`type(4)`

`x = 4`

`x`

`type(x)`

`2 * x`

Giving a name to something, so that you can refer to it by that name, is called assignment. Above, we assigned the name 'x' to 4, and after that we can use x wherever we want to use the number 4.

The space between the variable name, the equal sign, and its value does not matter.  The following are the same.  You should be consistent in your code.

`x = 5`

`x=5`

Variables can be re-assigned.

`x = 3`

`x`

`x = 7`

`x`

Be careful when you do this though... accidentally re-assigning a variable can cause bugs in your code.

Variables can be made of letters, numbers, and underscores. They must start with a letter and can not contain any other special characters.  Here are some valid variable names:

`magic_number = 1500`

`amountOfFlour = .75`

`my_name = "Jessica"`

Projects develop naming conventions: multi-word variable names may use underscores (like `magic_number`), or "camel case" (like `amountOfFlour`). The most important thing is to be consistent within a project, because it makes the code more readable.


###Strings

So far we've seen two data types: *integers* and *floats*. Another useful data type is a *string*, which is just what Python calls a bunch of characters (like numbers, letters, whitespace, and punctuation) put together. Strings are indicated by being surrounded by quotes:

`"Hello"`

`"Python, I'm your #1 fan!"`

Like with the numeric data types, we can check the type of a string:

`type("Hello")`

`type(1)`

`type("1")`

You can assign a string value to a variable:

`my_car = "Toyota"`


####String Concatenation

You can concatenate, or join strings together using the `+` sign:

`"Hello" + "World"`

`"I drive a " + my_car`

You can not concatenate a string with another data type.

`"Hello" + 123`

will give you a *traceback*:

~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
~~~

A traceback provides details on what was happening when Python encounters an Exception or Error -- something it doesn't know how to handle.
There are many kinds of Python errors, with descriptive names to help us humans understand what went wrong. In this case we are getting a `TypeError`: we tried to do some operation on a data type that isn't supported for that data type.
Python gives us a helpful error message as part of the `TypeError`:
`"cannot concatenate 'str' and 'int' objects"`.

We can, however, use the `str()` function to convert a number to a string.  Like the `type()` function we've been using, `str()` takes one argument as input and outputs it as a string.

`str(4)`

`str(5.34)`

`str("Ice cream")`

####String Length

There's another useful function that works on strings called `len()`.  This returns the length of a string as an integer.

`len("Hello")`

`len("")`

`president = "Obama"`

`len(ice_cream)`

####Quotes

We've been using double quotes around your strings, but either double or single quotes are valid in Python:

`"Hello world"`

`'Hello world'`

You do have to be careful about using quotes inside strings:

`'Let's learn Python together!'`

will give you another `traceback`, for a `SyntaxError`.  When Python evaluates this expression, it starts at the first single quote as the start of the string, and to the next single quote as the end of the string.  Then it doesn't know what to do with the rest of the stuff that follows.

There are a few ways to solve this problem.  One is to use double quotes:

`"Let's learn Python together!"`

or we can *escape* the quote with a backslash.  The backslash is a special character that tells Python to treat the next character literally, not as part of the syntax or code.

`'Let\'s learn Python together!'`

Let's take a break.  We've covered a lot!