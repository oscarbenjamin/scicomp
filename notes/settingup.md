---
---

# Getting set up with Python

## Basics

This unit is aimed at students who have seen Python before but are perhaps a
bit rusty with it. If you've never seen Python before then I recommend to you
to follow a more detailed tutorial such as [the one at
python.org](https://docs.python.org/3/tutorial/index.html). Here we will
quickly run through some of the basic features of Python to remind everyone
what it is about. The python.org tutorial has more detail on the basics of
Python if you're unfamiliar with any of the topics discussed here.

## Installing Python

Python is many different things. Firstly it is programming language in which
we can write Python code. Secondly it is a *program* which we used to run our
Python code. This program is called the *interpreter*. In fact there are a
number of different interpreters that you can install and use for running your
Python code or that you can use in different environments.

The standard Python interpreter is known as "CPython" (when we need to
distinguish it from the others). The "C" in CPython is for the C programming
language in which the interpreter is written: the interpreter is actually a C
program.  There are other interpreters, notably PyPy (which is itself written
in a Python-like language) and Jython (written in Java), MicroPython for
embedded systems and Brython (for running in browsers). You don't need to
use/install any of these different interpreters but it is worth mentioning
their existence at this point.

In order to install Python here we want to install the CPython interpreter.
We can install this using the [official installers from
python.org](https://www.python.org/downloads/) however it
would not come with all of the bits and pieces that we want. CPython is the
interpreter for the basic Python language which is a generic programming
language used in many different areas. It comes with an interpreter and the
"standard library" ("stdlib" for short) which is a set of modules for doing
common things. Usually though when we use Python for something - in our case
for *scientific* purposes - we will want to install some additional libraries.

Installing Python and then separately installing each of the different
libraries we want can be a pain for beginners to setup which is why installers
are provided that can bundle Python with other commonly used libraries. For
this reason I recommend to install the [Anaconda Python distribution from
continuum](https://www.continuum.io/downloads). In addition to the interpreter
and the stdlib this will install a large number of commonly used scientific
libraries such as `numpy` for Matlab-style arrays and `matplotlib` for
plotting that we are going to need to use in this unit.

However you install Python and these additional libraries it is important to
ensure that you can run Python from terminal. Pay careful attention to any
options in the installer that refer to "adding Python to the PATH environment
variable" since this is the key to getting this set up right. If this isn't
right then you'll see something like "Unrecognised command: python". It's
possible to manually alter your `PATH` environment variable after installation
if necessary so that you can add the directory containing the Python
executable to it. If you are able to run Python in some way (e.g. using IDLE)
but the `python` command does not work in the terminal then you can see where
the executable is with

~~~~ python
>>> import sys
>>> print(sys.executable)
/usr/bin/python
~~~~

This tells me that the executable is in the `/usr/bin/` directory so that's
the directory that needs to be on `PATH`.

Another confusion can occur here for OSX users. OSX comes with a version of
CPython preinstalled but that is the "system python" and you shouldn't mess
with it. Install a *different* Python using Anaconda as above (or homebrew if
that's what you're used to). You now need to make sure that you can run this
new version of Python when desired or otherwise you won't be able to access
the scientific Python libraries that you install along with it. See below for
checking the scientific libraries.

## Running Python

There are actually many different ways to run Python so this is not a trivial
topic. Many of you will have prior experience using Python from
[IDLE](https://en.wikipedia.org/wiki/IDLE) which is
a graphical IDE (integrated development environment) having both an editor and
an interactive terminal. Typically when Python is installed IDLE will also be
installed along with some kind of shortcut that you can use to run IDLE. There
are also other IDEs used by Python programmers e.g.
[spyder](https://pythonhosted.org/spyder/) is popular with scientific
programmers. Some people also like to write scientific code in the form of
[Jupyter notebooks](http://jupyter.org/).

### Interactive mode

All of those ways of running Python are useful in various different
situations. None of them can completely replace being able to run Python using
a command line though. That is why we are going to begin by running Python
from the system terminal by typing the command `"python"`:

~~~~ terminal
$ python
Python 2.7.3 (default, Oct 26 2016, 21:01:49)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 2
>>> a + a
4
>>> print(a)
2
>>> for x in range(4):
...     print(x)
...
0
1
2
3
~~~~

The above is how a quick terminal session on my computer looks where I run
Python and type a few interactive commands. Note the conventions that will be
used through these notes for a terminal session - I will assume that you
understand these throughout these notes. The commands that I type in the
terminal are on the lines that begin with a `$` symbol. This is the standard
terminal prompt on unixy (non-Windows) systems telling me that the terminal
expects a command line to be entered. On Windows the prompt may look different
but within the notes I will always use `$` to indicate a terminal prompt.

The command I run here is simply `"python"` with no arguments. This invokes
the Python interpreter in *interactive mode* so that after printing a startup
message I see the Python interactive prompt `>>>` which is the prompt for me
to enter some Python code. I can type a piece of Python code such as `a = 2`
and when I hit enter the interpreter will execute that code. If I type a
*statement* such as `a = 2` then the terminal will not usually output
anything. If I type an *expression* such as `a + a` then the terminal will print
the value of that expression i.e. `4` (the exception to this rule is that the
terminal will not print the special value `None`).

We can type a multiline piece of code such as the `for`-loop shown above. The
interpreter shows `...` to indicate that some lines are continuations of the
command.

The Python interpreter in interactive mode is also called the Python *shell*.
However the normal non-Python terminal also has a different shell (called
`bash` on my machine) so this terminology can be a little confusing. The main
thing to take away from this - which is a common cause of confusion for
beginners - is that there are two different shells:

* The system shell has a `$` prompt and is for command lines
* The Python shell has a `>>>` prompt and is for Python code

Make sure that you don't get mixed up and type Python code into the system
shell or vice-versa - this will never achieve anything sensible.

### Normal mode

We can also add our code to a Python file with the extension `.py`.  Then we
can run the code file using the same interpreter but giving the filename on
the command line. This way of running the interpreter so that it reads code
from a file is called "normal-mode" to contrast with "interactive-mode".

Using whatever code editor you like create a file called `mystuff.py` and
insert the same code as was typed in the above interactive session i.e.:

~~~~ python
a = 2
a + a
print(a)
for x in range(4):
    print(x)
~~~~

Now I'm assuming that your terminal is in the same folder that you saved the
file in - use `cd` to move to that folder if not. You can now run that Python
file with the command `python mystuff.py`:

~~~~ terminal
$ python mystuff.py
2
0
1
2
3
~~~~

This is the normal way to use the Python interpreter to run your code. The
interactive prompt is useful for testing small pieces of code out but once
tested you should be putting all of your code into `.py` files and running
them like so. One important difference between the output above and
interactive mode is that the line `a + a` no longer prints anything out. This
is because expressions are only printed in interactive mode. When running
normally the interpreter will only print something if you tell it to with the
`print` function (contrast this with Matlab and its semicolon `;` output control).

### Check the scientific libraries

Please check at this point that you have the scientific libraries installed
using the interactive terminal:

~~~~ python
>>> import numpy
>>> import matplotlib
~~~~

If all goes well these commands will not do anything. If you see something like
~~~~ python
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named numpy
~~~~
then you don't have the scientific libraries installed. Or it could mean that
you're running the wrong Python since it is possible to have many installed...

Either way at this point you need to sort it out so that you can run Python
and have the scientific libraries installed.

## Summary

At this point I am assuming that

* You have Python (and scientific libraries) installed.
* You have a text-editor suitable for programming installed.
* You can run Python using the `python` command from the terminal.
* You can create a Python file and run it using `python myfile.py` from the
  terminal.
* You understand the difference between the system shell and the Python shell
* You understand the notation used in showing the terminal sessions above.

If so then we're ready to move into the basics of Python the language!
