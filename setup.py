from cx_Freeze import setup, Executable

import observe

build_exe_options = {
    "packages": [
        "observe",
        "PIL.ImageGrab",
        "comtypes.client",
        "pywinauto",
        ],
    "excludes": [
        "distutils",
        "email",
        "html",
        "http",
        "numpy",
        "pydoc_data",
        "setuptools",
        "unittest",
        "urllib",
        ],
    }

setup(
    name="ObserveSomething",
    version=observe.__version__,
    description="Send screenshots of progress report at regular time intervals",
    url="https://github.com/sio/ObserveSomething",
    author=observe.__author__,
    author_email="sio.wtf@gmail.com",
    license="GPL-3.0",
    platforms="any",
    executables=[Executable("ObserveSomething.py", base="Console")],  # cx_Freeze
    options={"build_exe": build_exe_options},  # cx_Freeze
    packages=["observe"],
    scripts=["ObserveSomething.py"],
    package_data={},
    include_package_data=True,
    install_requires=[
        "pywinauto>=0.6.3",
        "Pillow>=4.0.0",
        "comtypes>=1.1.3",
        ],
    python_requires=">=3.3",
    zip_safe=True,
    )
