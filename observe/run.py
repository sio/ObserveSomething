"""
Main executable module of ObserveSomething
"""


import os.path
import re
from collections import defaultdict
from configparser import ConfigParser
from datetime import datetime, timedelta
from time import sleep
from tempfile import TemporaryDirectory
from .com import make_MailItem
from .auto import select_windows, take_screenshot


DEFAULT_CONFIGURATION = {
    "observe": {
        "delay": "30m",
        "send_keys": "{F5}",
        "typing_delay": "1s",
        "image_dir": "",
    },
    "report": {
        "to": "",
        "subject": "New screenshots from ObserveSomething",
        "body": "This report was generated by ObserveSomething",
    },
}


def parse_time(interval):
    """
    Parse time intervals like the ones given to Linux sleep command:
    NUMBER[SUFFIX]

    Example: '3m'    = 3 minutes
             '5h 1m' = 5 hours 1 minutes
             '21'    = 21 seconds

    SUFFIX may be 's' for seconds (the default), 'm' for minutes, 'h' for
    hours 'd' for days or 'w' for weeks.  NUMBER has to be an integer.
    Given two or more whitespace separated words, return the amount of time
    specified by the sum of their values.

    Return datetime timedelta object.
    """
    expanded = {"w": "weeks",
                "d": "days",
                "h": "hours",
                "m": "minutes",
                "s": "seconds",
                "" : "seconds"}
    pattern = re.compile(r"\s*(\d+)([wdhms]?)\s*")

    parsed = defaultdict(int)
    for word in str(interval).split():
        match = pattern.match(word)
        if match:
            number, suffix = match.groups()
            parsed[expanded[suffix]] += int(number)
        else:
            message = "invalid time interval: {}".format(word)
            raise ValueError(message)
    return timedelta(**parsed)


def main(config_path):
    """Command line interface for ObserveSomething"""
    SCREENSHOT_NAME = "{date}_win{window_id}_scr{job_id}.png"
    DATE_FORMAT = "%Y%m%d"

    # Load configuration
    config = ConfigParser()
    config.read_dict(DEFAULT_CONFIGURATION)
    config.read(config_path, encoding="utf-8")

    # Set up the environment for worker
    delay = parse_time(config["observe"]["delay"]).total_seconds()
    key_delay = parse_time(config["observe"]["typing_delay"]).total_seconds()

    address_line = config["report"]["to"]
    while not address_line.strip():
        message = [
            "Recipient addresses not found in {}".upper().format(config_path),
            "Please enter space separated email addresses:\n"
            ]
        address_line = input("\n".join(message))
    addresses = address_line.split()

    image_directory = config["observe"]["image_dir"]
    temp = None
    if not image_directory:
        temp = TemporaryDirectory(prefix="ObserveSomething")
        image_directory = temp.name
    image_name = os.path.join(image_directory, SCREENSHOT_NAME)
    date = datetime.now().strftime(DATE_FORMAT)

    # Main worker loop
    windows = select_windows()
    iter_num = 0
    while True:
        iter_num += 1
        images = list()
        for window_tuple in windows:
            # Bring window to front
            window = window_tuple.specification
            window.minimize()
            window.maximize()
            window.set_focus()
            window.type_keys(
                config["observe"]["send_keys"],
                pause=key_delay)
            sleep(key_delay)

            # Take screenshot
            image = image_name.format(date=date,
                                      window_id=window_tuple.handle,
                                      job_id=iter_num)
            take_screenshot(image)
            images.append(image)

        # Send all screenshots
        mail = make_MailItem(recipients=addresses,
                             subject=config["report"]["subject"],
                             body=config["report"]["body"],
                             attachments=images)
        mail.Send()

        # Show progress in terminal
        info = "\n".join([
            "\rJob #{} done, next job scheduled...".format(iter_num),
            "Press Ctrl+C to exit"])
        print(info, end="")
        try:
            sleep(delay)
        except KeyboardInterrupt:
            print()
            break
    if temp: temp.cleanup()
