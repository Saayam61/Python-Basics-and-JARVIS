# install a package
# pip install pandas

# old versions
# pip install pandas==5.3.2

# virtual environment is created if you want to use different (old versions) or avoid version conflicts
# it is same as 'node_modules' in nodejs. it has 'requirements.txt' similar to 'package.json'

# A virtual environment in Python is a self-contained directory that contains a Python installation for a 
# specific version of Python, plus a number of additional packages. It helps to manage dependencies for 
# your projects and avoid conflicts between packages.

# Why Use Virtual Environments?
# Dependency Management: Each project can have its own dependencies, regardless of what dependencies 
# every other project has.
# Isolation: Different projects can use different versions of the same package without conflict.
# Reproducibility: Ensure that everyone working on the project is using the same versions of packages. 

# Steps:
# pip install virtualenv
# virtualenv env ; second env is name and can be anything
# .\env\Scripts\activate ; now you are inside virtual environment
# install package using pip install package_name (only works within this env)
# pip freeze > requirements.txt ; Save dependencies to a file
# deactivate ;exits virtual env

# pip install –r requirements.txt ; installs package from shared requirements.txt file

