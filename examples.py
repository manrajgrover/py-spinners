"""Examples demonstrating various spinners.

Attributes
----------
CLEAR_LINE : str
    To clear the current line
"""
import sys
import time
import cursor

from spinners import Spinners

CLEAR_LINE = '\033[K'


def animate(frames, interval, name, iterations=2):
    """Animate given frame for set number of iterations.

    Parameters
    ----------
    frames : list
        Frames for animating
    interval : float
        Interval between two frames
    name : str
        Name of animation
    iterations : int, optional
        Number of loops for animations
    """
    for i in xrange(iterations):
        for frame in frames:
            output = "\r{0} {1}".format(frame.encode('utf-8'), name)
            sys.stdout.write(output)
            sys.stdout.write(CLEAR_LINE)
            sys.stdout.flush()
            time.sleep(0.001 * interval)

try:
    cursor.hide()
    spinners = [spinner for spinner in Spinners] # pylint: disable=not-an-iterable
    sorted_spinners = sorted(spinners, key=lambda spinner: spinner.name)

    for spinner in sorted_spinners:
        frames = spinner.value['frames']
        interval = spinner.value['interval']
        name = spinner.name
        animate(frames, interval, name)

    print '\n'
finally:
    cursor.show()
