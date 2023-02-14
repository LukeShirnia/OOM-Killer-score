#!/usr/bin/python
"""
Python script for obtaining processes and their oom score
"""
from __future__ import print_function

# Standard Library
import os
import sys
from optparse import OptionParser


def getscores():
    """
    Function finds and returns a list of tuples containing:
    (oom_score process_name)
    """
    return [
        (
            int(open(os.path.join(proc.path, "oom_score")).read().strip()),
            open(os.path.join(proc.path, "comm")).read().strip(),
        )
        for proc in os.scandir("/proc")
        if proc.is_dir() and proc.name.isdigit()
    ]


def printscores(oom_scores, show):
    """
    Print oom score and process name
    """
    for process in sorted(oom_scores, key=lambda x: x[0], reverse=True)[:show]:
        print(f"{process[0]} {process[1]}")


def main():
    """
    Usage and help overview
    Option parsing
    """
    parser = OptionParser(usage="usage: %prog [option]")
    parser.add_option(
        "-s",
        "--show",
        action="store",
        dest="show",
        metavar="show",
        help="Number of processes to show",
    )
    (options, _) = parser.parse_args()

    show = int(options.show) if options.show else 10

    try:
        printscores(getscores(), show)
    except ValueError:
        print("Please enter a value number", file=sys.stderr)


if __name__ == "__main__":
    main()
