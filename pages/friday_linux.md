---
layout: page
title: Friday Setup - Linux
permalink: /frisetuplinux/
---

Here's what you need to do to set up your Linux machine.

#Download and Install Python

Most Linux machines have both Python 2 and Python 3 pre-installed.  Open a Terminal window and type `python3` at the prompt.  You should see something like the example in the Python shell section below.  If you don't, please see an instructor.

#Prepare a text editor

While you can absolutely write python code in any text editor, it is a lot easier to use one that is aware of code content and provides relevant features. To that end, we'll be using Sublime Text 3. While there are a multitude of other options, Sublime 3 provides a good blend of simplicity and functionality.

[Download it from here](http://www.sublimetext.com/3)

Install as you would any other program.

Be sure that you've set tabs equal to 4 spaces and the tabs to spaces setting is set to True.  Edit the file under "Preferences" -- "Settings - Default": 

~~~
    // The number of spaces a tab is considered equal to
    "tab_size": 4,

    // Set to true to insert spaces when tab is pressed
    "translate_tabs_to_spaces": true,

~~~

This ensures that when you hit the Tab button on your keyboard, your text editor will do the equivalent of typing four spaces.


#Practice starting & exiting the Python shell

* Open a command prompt.
* To start Python, type `python3` at the command prompt and hit enter. You should see something like

~~~
Python 3.4.0 (default, Apr 11 2014, 13:05:11)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

* The `>>>` indicates that you are at a Python prompt.
* Exit the Python prompt by typing `exit()` and hitting enter. 
* Practice doing this a few times until you are comfortable entering and exiting the Python shell.


#Practice navigating the computer from a command prompt

The filesystem on your computer is like a tree made up of folders (also called "directories") and files. The filesystem has a root directory called `/`, and everything on your computer lives in subdirectories of this root directory.
We often navigate the filesystem graphically by clicking on graphical folders. We can do the exact same navigation from the command line.
There are three commands that we'll be using at a command prompt to navigate the filesystem on your computer:

`ls` lists the contents of a directory.
`pwd` gives the full directory path to your current directory (it stands for "print working directory").
`cd` moves you into a new directory (it stands for "change directory").

Let's practice using these commands.

Open a command prompt:
You can find the Terminal application at Applications/Accessories/Terminal, or it may already be on your menu bar.
Practice using ls, pwd, and cd

Type each of these commands and hit enter:

`ls`
This lists all the files in your home directory.

`pwd`
This displays the full directory path to your current directory, which is your home directory.

`cd /`
This will change you into the / root directory.

`ls`
This lists the contents of the / root directory.

`cd home`
This will change you into the home subdirectory of the / root directory.

`ls`
You should see a list of all the files in /home, including the directory for your username -- your home directory.

`pwd`
This displays the full directory path to your current directory, /home.

`cd ..`
.. means "parent directory", so this command moved you up to the parent directory. You were in /home, so now you are in /, the root directory.

`ls`
This lists the contents of the root directory, confirming where you are.

####Tips

You can use Tab to auto-complete directory and file names. So from inside the root directory /, if you type cd ho and hit Tab, the command prompt will auto-complete the directory name, and you can then hit enter to change into the /home directory.
The command prompt maintains a command history. You can use the up arrow to cycle through old commands.

####Check your understanding

Answer these questions. Experiment at the command line if you need to! If you aren't sure about an answer, ask a helper.

* What directory are you in after starting a new command line prompt?
* After starting a new command line prompt, how would you get to the root directory?
* How do you check what files and directories are in your current working directory?
* If you are in directory /home, and you want to get to /home/PythonWork/projects, how would you do that?
* What are 2 ways to avoid typing out a full navigation command? (hint: one requires that you've run the command before)
* What is the difference between a command prompt and a Python prompt?

#### Success!
You've practiced using dir and cd to navigate your computer's filesystem from the command prompt.

#Start learning Python!
Go through this [self-directed tutorial](/fridaytutorial/) to start learning to read and write in Python. These concepts will be reviewed in the Saturday lesson, along with some more advanced topics.

#Get dependencies installed for the projects

Download the [Wordplay Project](https://github.com/PhillyPythonWorkshop/Wordplay/archive/master.zip).

Download the [Colorwall Project](https://github.com/PhillyPythonWorkshop/Colorwall3/archive/master.zip) for Python 3.  

#Practice
Try some [practice exercises](/practice/).  If you've been working on any other tutorials, feel free to go to those too, and ask an instructor to help anywhere you get stuck.

#Checkoff
Have an instructor or assistant [check you off](/fridaycheckoff/).