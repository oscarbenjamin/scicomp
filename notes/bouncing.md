---
layout: default
---

# Bouncing balls

Download [this script](bouncing.py) which animates a bouncing ball.
Take a look through the code and run it to see what it does. Notice that the
ball keeps bouncing higher and higher - this is due to the instability of
using the Euler method in this simulation.

## Assignment outline

You will provide a code repository demonstrating your solutions to the
problems below. You should also make a short report (in LaTeX) including each
of your figures. The report should explain the mathematical principles behind
your analysis and interpret the numerical results. Take the time to format
your figures nicely.

Your code should be well written and neatly separated into different .py
files. Each should calculate one of the numbers or figures requested by the
sections below. Reduce duplication by putting frequently used code into
separate modules and importing from them. Use comments, doc-strings etc to
make your code easier to read.

## Workflow

1. Create a new git repository (e.g. on bitbucket) called "bouncing".

2. Use `git clone <URL>` to clone the repository to your computer (bitbucket
   provides the command with the URL filled in so that you can paste it into a
   terminal.

3. Go into the folder with `cd` and use `git status` to check that everything
   is setup correctly.

4. For each exercise below you should work through the exercise and then:
   1. Use `git add` to add any new files you've created or files you've
      changed.
   2. Use `git diff` or `git diff --cached` to see changes before you commit
      them.
   3. Commit with a meaningful message using `git commit -m 'meaningful message'`

5. When you're done working on any particular machine (or every now and again)
   use `git push` to send your changes to the git repoistory on your hosting
   service (e.g. bitbucket).

6. As you're going along write a report including your findings (and figures).

7. Submit a zip of your repository (the folder called "bouncing") including
   all files and the .git folder along with a PDF of your report.

## Problems

1. Use the Euler method to solve the ODE $$\dot{x} = x$$ with initial
   condition $$x(0) = 1$$. You should use this to estimate $$x(1)$$ using
   different timesteps. Produce a (nicely formatted) plot with double
   logarithmic scale showing how the error depends on the size of the timestep
   $$\Delta t$$.

2. Repeat part 1 using the [4th-order Runge-Kutta
   method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge.E2.80.93Kutta_method).
   1. How does the error depend on $$\Delta t$$ now? How does this compare
      with the error for the Euler method (put this in the same plot)?
   2. Find step-sizes for each method that give you the same error - how long
      does each method take? (you can use the `time` command when running your
      Python script)

3. Consider the bouncing ball problem referred to above. Using the Euler
   method with the same step-size as in the provided script, show how the
   numerically generated trajectories appear in the *phase-plane* (plot $$y$$
   against $$v$$). How should the trajectories look? Considering the
   phase-plane argue that the Euler method is guaranteed to diverge in the way
   that it does for any initial conditions and any step-size.

4. Improve on the above by using the [SUVAT
   equations](https://en.wikipedia.org/wiki/Equations_of_motion#Uniform_acceleration)
   instead of the Euler method. Using the SUVAT equations you should be able
   to calculate (on pen and paper) exactly what the error from each step of
   the Euler method will be. How does this error depend on $$\Delta t$$ and
   does this agree with your results from part 1?

5. Considering that the ball bouncing problem is fully analytically solvable
   find a formula for the height $$y$$ of the ball at time $$t$$ if the
   initial conditions are that the ball starts on the ground but with an
   upwards velocity of $$5\,\mathrm{ms^{-2}}$$. Use this to plot how the error
   changes with time over approximately 10 bounces in both the SUVAT and Euler
   method cases. Can you improve your collision handling code to make
   the error exactly zero (up to rounding error)?
