---
layout: page
title: Friday Setup - Windows
permalink: /frisetupwindows/
---

Here's what you need to do to set up your Windows machine.

#Download and Install Python
If you already think you have Python 3 installed, please check with a staff member before completing these instructions.

1.  Click on [this download link](https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi) and choose "run" if you have the option to do so. Otherwise, save it to your computer and double click to start the installer.  Follow the instructions to complete the installation.

2.  Open a command prompt (we will be doing this multiple times, so make a note of how to do this!):
  * On Windows 8 search for "command prompt"
  * On Windows 7 or Vista click on the Start menu (the Windows logo in the lower left of the screen), type cmd into the Search field directly above the Start menu button, and click on "cmd" in the search results above the Search field.
  * On Windows XP click on the Start menu (the Windows logo in the lower left of the screen), click on "Run...", type cmd into the text box, and hit enter.

  You now have what's called a command prompt.  This command prompt is another way of navigating your computer and running programs -- just textually instead of graphically. We are going to be running Python and Python scripts from this command prompt.

3. At the command prompt (it should look like  `C:\`) type 
```
python34\python.exe
```
You should see something that looks like this:

~~~
Python 3.4.0 (default, Apr 11 2014, 13:05:11)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

You just started Python! The `>>>` indicates that you are at a new type of prompt -- a Python prompt. The command prompt lets you navigate your computer and run programs, and the Python prompt lets you write and run Python code interactively.

  * If the number after Python is not 3 or greater, please tell an instructor or assistant.


4. To exit the Python shell, type `exit()` and hit enter.  You'll now be back at the Windows command prompt (the `C:\` that you saw earlier).

# Put Python on the Windows PATH

You might have noticed that you typed a "full path" to the Python application above when launching Python (python.exe is the application, but we typed \Python34\python.exe). In this step, you will configure your computer so that you can run Python without typing the Python34 directory name.

#### Get to System Properties

##### Windows 8

> Search for your "Control Panel" and open it.
> Select the "system" icon. A window labeled "View basic information about your computer" will appear.
> In this window, click "Advanced system settings" and follow the steps below for all versions of Windows.

##### Windows 7 or Vista

> Open up "Computer"  by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to "Computer."
> ''Right-click'' on the empty space in the window, and choose ''Properties''. A window labeled "View basic information about your computer" will appear.
> In this window, click "Advanced system settings" and follow the steps below for all versions of Windows.

##### Windows XP
 
> Open up "My Computer"  by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to "My Computer."
> Right-click on the empty space in the window, and choose ''Properties''.  A window labeled "System Properties" will pop up.
> Click the "Advanced" tab and follow the steps below for all versions of Windows.

The next steps are the same for any version of Windows.

A window with the title "System Properties" will appear.

#### Edit the Path

1. Within System Properties, make sure you are in the tab labeled "Advanced".

2. Click the button labeled "Environment Variables". A window labeled "Environment Variables" will appear.

3. In this window, the screen is split between "User variables" and "System variables". Within "System variables", scroll down and find the one labeled Path. Click the "Edit..." button.

4. A window with the "Variable name" and the "Variable value" should appear. The "Variable value" will already have some text in it; click in the box to unhighlight it (we don't want to accidentally delete that text).

5. In the "Variable value" box, scroll to the end. Add the following text, and hit OK. Make sure to include the semicolon at the start!

`;c:\python34\;c:\python34\scripts`

6. Hit "OK" to close out the system properties window.


#### Test your change:
Open up a new command prompt. 

You do this the same way you did above when installing python. This needs to be a new command prompt because the changes you just made didn't take affect in prompts that were already open.

Type `python3` into the command prompt to start Python

Notice that you now get a Python interpreter, indicated by the change to a `>>>` prompt.

Exit the Python prompt by typing `exit()` and hitting enter. 

Now you're back at the Windows command prompt `(C:\)`.


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
* Exit the Python prompt by typing `exit()` and hitting enter. Now you're back at the Windows command prompt `(C:\)`.
* Practice doing this a few times until you are comfortable entering and exiting the Python shell.


#Practice navigating the computer from a command prompt


The filesystem on your computer is like a tree made up of folders (also called "directories") and files. The filesystem has a root directory called `/`, and everything on your computer lives in subdirectories of this root directory.
We often navigate the filesystem graphically by clicking on graphical folders. We can do the exact same navigation from the command line.
There are two commands that we'll be using at a command prompt to navigate the filesystem on your computer:

`dir`
dir lists the contents of a directory.

`cd`
cd moves you into a new directory (it stands for "change directory").

Let's practice using these commands.

Open a command prompt.

Type each of these commands and hit enter:

`dir`
*This lists all the files in your home directory.*

`cd C:\`
*This will change you into the C:\ directory.*

`dir`
*This lists the contents of the C:\ directory.*

`cd Users`
*This will change you into the Users subdirectory of the C:\ directory.*

`dir`
*You should see the names of all the files and directories in C:\Users.*

`cd ..`
 *The two dots mean "parent directory", so this command moved you up to the parent directory. You were in `C:\Users`, so now you are in `C:\`, the root directory.*

`dir`
*This lists the contents of the current directory (root).*

####Tips

You can use Tab to auto-complete directory and file names. So from inside the root directory, if you type `cd Use` and hit Tab, the command prompt will auto-complete the directory name, and you can then hit enter to change into the `C:\Users` directory.
The command prompt maintains a command history. You can use the up arrow to cycle through old commands.
Note that the text that makes up the command prompt changes as you move around directories. The command prompt will always give the full directory path to your current directory.

####Check your understanding

Answer these questions. Experiment at the command line if you need to! If you aren't sure about an answer, ask a helper.

* What directory are you in after starting a new command line prompt?
* After starting a new command line prompt, how would you get to the root directory?
* How do you check what files and directories are in your current working directory?
* If you are in directory `C:\Users`, and you want to get to `C:\Users\PythonWork\projects`, how would you do that?
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
