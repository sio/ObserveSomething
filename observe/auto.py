"""
Code for UI automation
"""


import pywinauto
import re
from collections import namedtuple


Window = namedtuple("Window", "specification title handle pid")
Window.__doc__ = """
    Store pywinauto.application.WindowSpecification along with
    some of its properties frozen at the moment of tuple creation.

    Mostly used to refer to the same WindowSpecification under
    the same title even when in fact window_text could have changed.

    Fields:
    specification
        WindowSpecification object. Convenient reference to the
        actual window.
    title
        Window title at the moment of tuple creation. Does not
        necessarily reflect current title of the window!
    handle
        pywinauto window handle.
    pid
        The process ID that corresponds to the WindowSpecification.
    """


def opened_windows(*a, **kw):
    """
    Generator that yields Window tuples for all visible windows

    All arguments are passed to pywinauto.findwindows.find_windows()
    """
    desktop = pywinauto.Desktop()
    for handle in pywinauto.findwindows.find_windows(*a, **kw):
        spec = desktop.window(handle=handle)
        title = spec.window_text()
        pid = spec.process_id()
        yield Window(spec, title, handle, pid)


def select_windows():
    """
    Terminal UI letting user select one or multiple windows
    from the list of opened windows.

    Accepts any delimiter as numbers separator.

    Returns a list of Window tuples.
    """
    windows = sorted(opened_windows(), key=lambda x: x.pid)
    numbers = re.compile(r"\d+")

    print("\nLIST OF OPEN WINDOWS:")
    max_len = 70
    for num, window in enumerate(windows):
        short_title = "{}..".format(window.title[:max_len]) \
                      if len(window.title) > max_len \
                      else window.title
        if not short_title: short_title = "<Title Unknown>"
        print("{n: >5}: {title}".format(n=num+1, title=short_title))
    selected = list()
    while not (selected and all(n <= len(windows) for n in selected)):
        reply = input("\nPLEASE SELECT WINDOWS (enter their numbers):\n")
        selected = [int(num) for num in re.findall(numbers, reply)]
    return [windows[n-1] for n in selected]
