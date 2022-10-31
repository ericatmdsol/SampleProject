# this file basically allows us to use sibling imports
# also has the advantage that if we have code that we want to
# reuse in other projects we can pip-import from 
from setuptools import setup, find_packages

setup(name='samplestructure', version='1.0', packages=find_packages('src'))