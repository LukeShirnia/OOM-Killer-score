#!/usr/bin/python
"""
Python script for obtaining processes and their oom score
"""
import __future__  # pylint: disable=unused-import
import os
from optparse import OptionParser    # pylint: disable=deprecated-module


def getscores():
    """
    Function finds and returns a list of tuples containing:
    (oom_score process_name)
    """
    oom_scores = []

    for pid in os.listdir("/proc/"):
        if os.path.exists("/proc/{}/oom_score".format(pid)):
            with open(os.path.join(
                    "/proc/{}/oom_score".format(pid))) as oom_score:
                oom = int(oom_score.read().strip())
            with open(os.path.join(
                    "/proc/{}/comm".format(pid))) as proc_name:
                name = proc_name.read().strip()
            oom_scores.append(tuple((oom, name)))

    oom_scores = sorted(oom_scores, key=lambda x: x[0], reverse=True)

    return oom_scores


def printscores(oom_scores, show):
    """
    Print oom score and process name
    """
    for process in oom_scores[:show]:
        if process[0] != 0:
            print("{0} {1}".format(process[0], process[1]))


def main():
    """
    Usage and help overview
    Option pasring
    """
    parser = OptionParser(usage="usage: %prog [option]")
    parser.add_option(
        "-s",
        "--show",
        action="store",
        dest="show",
        metavar="show",
        help="Number of process to show",
    )
    (options, _) = parser.parse_args()

    show = 10

    if options.show:
        show = options.show

    try:
        printscores(getscores(), int(show))
    except ValueError:
        print("Please enter a value number")


if __name__ == "__main__":
    main()
