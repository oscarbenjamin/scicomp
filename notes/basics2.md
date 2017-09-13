---
layout: default
---

# Loops, etc.

Like all programming languages Python has loops, conditionals and functions. I
will briefly write about these here but I don't want to repeat what's already
written better in other places. For more please refer to the [official
python.org tutorial](https://docs.python.org/3/tutorial/controlflow.html).

There are some [exercises](#exercises) below to test your understanding of
these concepts.

## Loops

Python has `while` statements which are more or less the same as in all
programming languages. It also has `for` loops and these are potentially
different from what you would be used to coming from other languages. The key
thing to understand about `for` loops in Python is that we loop over an
*object*:
~~~~ python
>>> stuff = [1, 2, -1, 3]
>>> for x in stuff:
...     print(x)
...
1
2
-1
3
~~~~
In this example the object we loop over a `list` but we can also loop over
many other kinds of objects such as `strings`, `tuples`, `dicts`, `sets`, etc.
If you just want to loop over the numbers say from 0 to 3 we use the `range`
function:
~~~~ python
>>> for x in range(4):
...     print(x)
...
0
1
2
3
~~~~
Note that `range(a, b)` gives a *half-open* range such as mathematically represented with
$$[a,b)$$ meaning the integers $$x$$ such that $$a \le x \lt b$$. When called
with one argument `range(b)` is the same as `range(0, b)`. Observe that there
are similarities between the arguments to `range` and the start, stop and step
indices used when slicing i.e. `range(a, b, c)` gives the indices of the
elements selected by `stuff[a:b:c]`.

## Functions

Python has functions: use them. If you are used to using Matlab you might have
gotten into the habit of not using functions very often because each function
needs a new .m file. In Python we can have as many functions as we like in a
file and it is common to have many small functions in one file. Functions are
good and you should make a habit of composing all your code from small
well-designed functions.

What I do want to say about functions here is that in Python it is possible to
make a function that returns different types of objects at different times
e.g.:
~~~~ python
def f(n):
    if n < 0:
        return 'a string'
    else:
        return -n

print(f(1)) # returns int (-1)
print(f(-1)) # Returns a string ('a string')
~~~~
This is due to the dynamic nature of Python and in *some* situations is
useful. In general though we should not do this. Functions should always
return the same type. For example, a function `f(n)` could be understood as
always taking an integer (`n`) and return an integer. Doc-strings are useful
and can be used to explain the types:
~~~~ python
def absolute_value(n):
    '''absolute_value(n) -> absolute value of number n'''
    if n < 0:
        return -n
    else:
        return n
~~~~
(Why do I say `number` instead of `int`, `float`, etc.?)

Also as much as possible functions should be *pure*. This is an important
programming style that will make your code better and easier to read/debug
etc. To clarify what this means let's divide the world of functions into 4
categories using two different properties.

Our first property is that of having *side-effects*. A function that has
side-effects is one that
