try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import observe

if "install" in sys.argv \
and "--process-dependencies-links" not in sys.argv:
    warn = ("WARNING: Use pip with `--process-dependencies-links` if you want\n"
            "to install GitHub dependencies automatically")
    print(warn, file=sys.stderr)

setup(
    name="ObserveSomething",
    version=observe.__version__,
    description="Send screenshots of progress report at regular time intervals",
    url="https://github.com/sio/ObserveSomething",
    author=observe.__author__,
    author_email="sio.wtf@gmail.com",
    license="GPL-3.0",
    platforms="any",
    packages=["observe"],
    scripts=["ObserveSomething.py"],
    package_data={},
    include_package_data=True,
    install_requires=[
        "toolpot<=99",
        "Pillow",
        "comtypes",
        "pywinauto",
        ],
    dependency_links=["git+git://github.com/sio/toolpot.git#egg=toolpot-99"],
    python_requires=">=3.3",
    zip_safe=False,
    )
