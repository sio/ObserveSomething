"""
ObserveSomething launcher
"""

import sys
from observe.run import main

if __name__ == "__main__":
    args = sys.argv + ["observe.ini"]
    main(args[1])
