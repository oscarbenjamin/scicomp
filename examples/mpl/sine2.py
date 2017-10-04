#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(filename=None):
    '''Plot sine function and show on screen or save to file'''

    # Set the figure size in inches
    # and manually control the axes size
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_axes([0.20, 0.20, 0.70, 0.70])

    # Have a function to do the actual plotting to the axes object
    plot_sine(ax)

    # Show on screen or save to file if filename is provided
    if filename is None:
        plt.show()
    else:
        fig.savefig(filename) # Format chosen by extension


def plot_sine(ax):
    numpoints = 100
    x = np.linspace(0, 2*np.pi, numpoints)
    y = np.sin(x)

    ax.plot(x, y, color='black', linewidth=3)
    ax.set_xlim([0, np.pi])
    ax.set_ylim([-1, 1])

    # Use LaTeX for text
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$\sin{x}$', rotation=0)

    # Manually control axes ticks
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels([
        r'$0$',
        r'$\frac{\pi}{2}$',
        r'$\pi$',
        r'$\frac{3\pi}{2}$',
        r'$2\pi$',
    ], fontsize='large')
    ax.set_yticks([-1, 0, 1])


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
