#Python App
Python App is a template Python application configured for python-ness!


# Installation on OS X

##Install Homebrew:
- ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

##Install Python2.7:
This is necessary purely to run the Fabric tool as it has not been ported to Python3 yet!

- brew install python2.7

## Install Fabric:
- pip-2.7 install fabric

##Install Pythonbrew:
- sudo easy_install pythonbrew 
- pythonbrew_install

Instructions from: http://www.howopensource.com/2011/05/how-to-install-and-manage-different-versions-of-python-in-linux/
						
##Build the Life project:
- fab install


# Running Python App

## Command Usage
fab run

### Help
- fab run:args="--help"

### Example
fab run:args="'Hello World\!'"


# Configuring Python App
Run-time configuration is made using the command-line arguments.

Edit the settings.py file to change the starting configuration of the program.