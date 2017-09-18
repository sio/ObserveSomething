# ObserveSomething
Stay updated on the progress of some long running job you've launched at the
office while you're away.


# What this application does
For each of the windows user asked to monitor, ObserveSomething repeats the
following steps at regular intervals:
- Bring window to focus
- Send a sequence of keys to initiate a status update
- Email a screenshot of updated window to the user


# When in Rome...
Most corporate computer setups restrict the amount of UI automation the user
can do. That's why this application relies on the simplest GUI automation
possible (SendKeys) and uses the mail app most office PCs have preconfigured
(Microsoft Outlook).


# Installation and usage
This application requires no installation, just download a zip archive of the
latest release and extract it anywhere you like. ObserveSomething does not
store any persistent data outside the application directory, so it can be
installed on the thumb drive and used as a portable application.

To launch the application, double click on `ObserveSomething.exe`


# System requirements
ObserveSomething works on modern *Windows* operating systems (Windows 7, 8, 10)
and requires *Microsoft Outlook* to be installed and configured to be able to
send e-mails.


# Configuration
Configuration is done via INI file (`observe.ini` or the first command
line argument). Upon launch user is asked to provide the list of windows
to monitor. After that ObserveSomething runs on its own until stopped.

Refer to the [sample file](docs/observe-sample.ini) for more information.


# Contributing
All contributions are welcome!
Please check [CONTRIBUTING.md](CONTRIBUTING.md) for details


# License and copyright
Copyright © 2017 Vitaly Potyarkin
```
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
