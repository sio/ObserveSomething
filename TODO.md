# Known bugs

# Missing features

# Refactoring
[ ] observe.run:main()
    [x] Use smaller, atomic functions:
        [x] prepare_window(spec, keys, delay)
    [x] Use simpler naming convention for screenshots: window.handle is unreliable
        because it comes from external library (it may contain unacceptable chars
        in future). Replace it with the number of window in windows, add enumerate()
        to the beginning of the `for` loop
    [x] contextmanager log_ignored(*exceptions, logger=None)
    [x] Wrap these smaller functions with try..except
        [x] prepare_window
        [x] take_screenshot
        [x] MailItem.Send
    [ ] Use logging module to log silenced exceptions
[x] Use venv when building with cxFreeze
    [x] Set up virtual environment with all dependencies
