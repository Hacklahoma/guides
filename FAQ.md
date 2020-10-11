# FAQ

#### I'm not able to run my python script
* It's possible that you have multiple versions of python installed. Try using `python3.6` instead of `python` when you run the program in terminal. If you see `command not found`, it means you don't have that version of python, so follow the instructions [here](https://www.python.org/downloads/release/python-365/) to install Python 3.6.

#### Flask isn't working on Windows
* Make sure you've installed [Cygwin](http://www.cygwin.com), which is a Unix-based command line, similar to Terminal on Mac. It is possible to do everything in Command Prompt, but the syntax for running a python script and setting flask environment variables will be different.

#### I'm getting an error along the lines of "OSError [Errorno 13] Permission Denied" when I try to install Pip!
* Try adding '--user' in the command line when running the pip install file!
