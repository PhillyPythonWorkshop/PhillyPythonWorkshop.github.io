---
layout: page
title: Friday Setup - Mac
permalink: /frisetupmac/
---

While Macs come with Python 2.7.x pre-installed, we'll be working with Python 3 during this session so there's some light installation ahead of us. This will require administrative priveleges to your computer since the Python installation is usually done to protected directories.

Along the way, we'll also set up a more advanced text editor that will help us by providing some really specific programming features.

# Installing Python 3.6 for Mac

To install Python 3 for Mac:

* Download the package available here: [Python 3.6.0 Installation Package for Mac](https://www.python.org/ftp/python/3.6.0/python-3.6.0-macosx10.6.pkg)
* Double click the downloaded file to start the installation process.
* Click through the wizard. The default settings are all fine to use. Close the wizard when complete.
  * Note: by default, the package installs into a central location which will require you to enter your system username and password during the process.

# Testing the installation

You can test that your installation went well by running the `python3` interpreter in the `Terminal`. 

Enter the following into the terminal and press `enter`:

    python3

You should then see something like this:

    Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> quit()

While inside the python interpreter:

* The `>>>` indicates that you are at a Python prompt.
* You can exit the Python prompt by typing `quit()` and pressing enter or by using `CTRL+d`. 
* Practice doing this a few times until you are comfortable entering and exiting the Python shell.

# Installing a Text Editor (Sublime)

While you can absolutely write Python code in any text editor, it is a lot easier to use one that is aware of code content and provides relevant features. To that end, we'll be using Sublime Text 3. While there are a multitude of other options, Sublime 3 provides a good blend of simplicity and functionality.

[Download it from here](http://www.sublimetext.com/3)

Once downloaded, install it as you would any other OS X application. Being explicit, this means double-clicking the downloaded `dmg` file, letting it open up, and subsequently dragging the `Sublime Text` application into your `Applications` folder.

Be sure that you've set tabs equal to 4 spaces and the tabs to spaces setting is set to True.  In the Sublime Text Menu, add content below Preferences > Settings - User. Make sure that it is inside the curly braces at the top of your file.

~~~
{
    // The number of spaces a tab is considered equal to
    "tab_size": 4,

    // Set to true to insert spaces when tab is pressed
    "translate_tabs_to_spaces": true,

    ... rest of file
}
~~~

# Practice navigating the computer from a Terminal

The way your computer organizes storage is called a filesystem. This filesystem is organized like a tree with folders (also called `directories`) and `files`. The highest point in the tree is the _root_ directory located at `/`. Everything you can access on your computer lives within the sub-directories of this root directory.

We often navigate the filesystem graphically (using Finder) where we can click and move deeper and across this directory tree. We can do that exact same navigation from the command line.

To do this, there are three commands that we'll be using:

  * `ls`  lists the contents of a directory
  * `pwd`  shows you the full path to your current directory (it stands for "print working directory")
  * `cd`  moves you into a new directory (it stands for "change directory").

## Let's practice using these commands.

Open up a Terminal. (hint: it's in `Applications/Utilities`)

Type each of these commands and hit `enter`:

{% highlight bash %}
ls
{% endhighlight %}
This lists all the files in your home directory.

{% highlight bash %}
pwd
{% endhighlight %}
This displays the full directory path to your current directory, which is your home directory.

{% highlight bash %}
cd /
{% endhighlight %}
This will change you into the `/` (root) directory.

{% highlight bash %}
ls
{% endhighlight %}
This lists the contents of the `/` (root) directory.

{% highlight bash %}
cd Users
{% endhighlight %}
This will change you into the home subdirectory of the `/` (root) directory.

{% highlight bash %}
ls
{% endhighlight %}
You should see a list of all the computer's users' home directories (and possibly a Shared folder).

{% highlight bash %}
pwd
{% endhighlight %}
This displays the full directory path to your current directory, which in this case is `/Users`.

{% highlight bash %}
cd ..
{% endhighlight %}
`..` is a relative location meaning "parent directory". You were in `/Users`, so now you have moved up to your "parent", `/`, the root directory.

{% highlight bash %}
ls
{% endhighlight %}
This lists the contents of the root directory, confirming where you are.

{% highlight bash %}
cd ~
{% endhighlight %}

Just like how `..` means "parent directory", `~` means "home" directory. When you execute this command, you'll change back to your home directory, where all your user files are.


#### Tips

1. You can use `tab` to auto-complete directories, files, and programs. So from inside the root directory `/`, if you type `cd Us` and press the `tab` key, the command prompt will auto-complete the directory name, and you can then hit `enter` to change into the `/Users` directory.

2. The command prompt maintains a command history. You can use the up arrow to cycle through old commands. You can also see a list of your history by using the `history` command.

3. If you'd like to open a Finder window wherever you are in the Terminal, you can use the `open .` command. Turns out `.` is another "special place" that means "the current directory". So this command opens the current directory, which OS X generally does with the help of Finder.

4. If you'd like to change to a specific location in the Terminal, and you have a Finder window open already to that place, you can type in `cd ` to the Terminal, drag the little blue folder at the top of the Finder window into the Terminal, and then press `enter`.

#### Check your understanding

Answer these questions. Experiment at the command line if you need to! If you aren't sure about an answer, ask a helper.

* What directory are you in after starting a new command line prompt?
* After starting a new command line prompt, how would you get to the root directory?
* How do you check what files and directories are in your current working directory?
* If you are in directory `/`, and you want to get to `/Users/Shared/`, how would you do that?
* What are 2 ways to avoid typing out a full navigation command? (hint: one requires that you've run the command before)
* What is the difference between a command prompt and a Python prompt?


#### Success!

You've practiced using `ls` and `cd` to navigate your computer's filesystem using Terminal.

# Start learning Python!

Go through this [self-directed tutorial](/fridaytutorial/) to start learning to read and write in Python. These concepts will be reviewed in the Saturday lesson, along with some more advanced topics.

# Get dependencies installed for the projects

Download the [Wordplay Project](https://github.com/PhillyPythonWorkshop/Wordplay/archive/master.zip).

Download the [Colorwall Project](https://github.com/PhillyPythonWorkshop/Colorwall3/archive/master.zip) for Python 3.  

# Practice
Try some [practice exercises](/practice/).  If you've been working on any other tutorials, feel free to go to those too, and ask an instructor to help anywhere you get stuck.

# Checkoff
Have an instructor or assistant [check you off](/fridaycheckoff/).

